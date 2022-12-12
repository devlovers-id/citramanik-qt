import os
import shutil
import subprocess
import sys
import tempfile
import traceback


from PyQt6.QtWidgets import QMainWindow, QMessageBox, QFileDialog

from citramanik.ui.Ui_Citramanik import Ui_Citramanik
from citramanik.ui.Ui_ProgressDialog import Ui_CitramanikProgressBar
from citramanik.utils.svgparser import SVGParser

from citramanik.handler.console import CitramanikOptions
from citramanik.handler.configs import CitramanikConfigs
from citramanik.handler.dialogs import *
from citramanik.handler.process import CitraManikThread
from citramanik.handler.updater import CitramanikUpdater


class CitramanikWindow(QMainWindow, Ui_Citramanik):
    def __init__(self, *args, **kwargs):
        self.options = CitramanikOptions()
        self.appconfigs = CitramanikConfigs().load_from_file()

        self.local_version = self.appconfigs.get_current_version()
        super(CitramanikWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # check inkscape from console argument
        if not self.options.inkscape_path:
            if not self.appconfigs.get_inkscape_path():
                show_message(QMessageBox.Icon.Critical, "Inkscape not detected, if you're using AppImage/Portable version of Inkscape, please configure it on the Settings tab")
                # print("No Internal Inkscape")
                self.options.inkscape_path = ""
            else:
                self.options.inkscape_path = self.appconfigs.get_inkscape_path()

        # check ghostscript from console argument
        if not self.options.ghostscript_path:
            if not self.appconfigs.get_ghostscript_path():
                show_message(QMessageBox.Icon.Warning, "Ghostscript not detected, please configure it in the Settings tab, otherwise you can't do BOOKLET/PDF/JPG/EPS exports with CMYK mode")
                # print("No Internal Ghostscript")
                self.options.ghostscript_path = ""
            else:
                self.options.ghostscript_path = self.appconfigs.get_ghostscript_path()

        # check pngquant from console argument
        if not self.options.pngquant_path:
            if not self.appconfigs.get_pngquant_path():
                show_message(QMessageBox.Icon.Warning, "Pngquant not detected! Please configure it in the Settings tab, otherwise you can't use PNG optimized feature. \n\nGet Pngquant from your distro repository, or download at https://pngquant.org/")
                # print("No Internal Pngquant")
                self.options.pngquant_path = ""
            else:
                self.options.pngquant_path = self.appconfigs.get_pngquant_path()

        # initialize gui data
        self.__initialize_gui()
        self.__tmp_exportsdir = None

        self.updater = CitramanikUpdater(self)

        # register events
        self.btn_extratools.clicked.connect(self.__on_btn_extratools_clicked)
        self.btn_browse_inkscape.clicked.connect(self.__on_btn_browse_inkscapepath_clicked)
        self.btn_browse_ghostscript.clicked.connect(self.__on_btn_browse_ghostscriptpath_clicked)
        self.btn_browse_pngquant.clicked.connect(self.__on_btn_browse_pngquantpath_clicked)
        self.btn_opensvg.clicked.connect(self.__on_btn_opensvg_clicked)
        self.btn_export.clicked.connect(self.__on_btn_export_clicked)
        self.btn_browse_outputdir.clicked.connect(self.__on_btn_browse_outputdir)

        self.use_flatpak = False

        self.options.pageOnly = False

        self.checkbox_flatpak.toggled.connect(self.__on_flatpak_toggled)

        self.combo_export_mode.currentIndexChanged.connect(self.handlePAGE)
        self.checkBox_JPG.toggled.connect(self.__on_jpg_toggled)
        self.checkBox_PNG.toggled.connect(self.__on_png_toggled)

    def handlePAGE(self):
        if self.combo_export_mode.currentIndex() == 0:
            self.options.pageOnly = False
            self.field_pattern.setDisabled(False)
        else:
            self.options.pageOnly = True
            self.field_pattern.setDisabled(True)

    def __initialize_gui(self):

        self.options.is_progressive = False
        self.options.optimize_png = False

        if self.options.inputfile:
            self.field_svginput.setText(self.options.inputfile)
        if self.options.outputdir:
            self.field_exportdir.setText(self.options.outputdir)
        if self.options.pattern:
            self.field_pattern.setText(self.options.pattern)
        if self.options.with_jpg:
            self.checkBox_JPG.setChecked(True)
            self.checkBox_JPGProgressive.setEnabled(True)
        if self.options.with_png:
            self.checkBox_PNG.setChecked(True)
        if self.options.with_eps:
            self.checkBox_EPS.setChecked(True)
        if self.options.with_pdf:
            self.checkBox_PDF.setChecked(True)
        if self.options.with_booklet:
            self.checkBox_BOOK.setChecked(True)
        if self.options.with_svg:
            self.checkBox_SVG.setChecked(True)

        if self.options.with_webp:
            self.checkBox_WEBP.setChecked(True)
        if self.options.with_zip:
            self.checkBox_ZIP.setChecked(True)

        if self.options.colorspace == "cmyk":
            self.combo_colorspace.setCurrentIndex(0)
        else:
            self.combo_colorspace.setCurrentIndex(1)

        if self.options.dpi:
            self.field_dpi.setValue(self.options.dpi)
        else:
            self.field_dpi.setValue(self.appconfigs.get_dpi())

        if self.options.quality:
            self.field_quality.setValue(self.options.quality)
        else:
            self.field_quality.setValue(self.appconfigs.get_quality())

        if self.options.inkscape_path:
            self.field_inkscape_path.setText(self.options.inkscape_path)
        else:
            self.field_inkscape_path.setText(self.appconfigs.get_inkscape_path())

        if self.options.ghostscript_path:
            self.field_ghostscript_path.setText(self.options.ghostscript_path)
        else:
            self.field_ghostscript_path.setText(self.appconfigs.get_ghostscript_path())

        if self.options.pngquant_path:
            self.field_pngquant_path.setText(self.options.pngquant_path)
        else:
            self.field_pngquant_path.setText(self.appconfigs.get_pngquant_path())

        self.spinBox_Threads.setValue(self.appconfigs.get_threads_config())
        self.tabWidget.setCurrentIndex(0)
        self.banner_update.hide()

    def __on_flatpak_toggled(self, status):
        self.use_flatpak = status
        self.field_inkscape_path.setEnabled(not(status))
        self.btn_browse_inkscape.setEnabled(not(status))

    def __on_jpg_toggled(self, status):
        self.options.with_jpg = status
        self.checkBox_JPGProgressive.setEnabled(status)
        if not status:
            self.checkBox_JPGProgressive.setChecked(False)

    def __on_png_toggled(self, status):
        self.options.with_png = status
        self.checkBox_Optimize_PNG.setEnabled(status)
        if not status:
            self.checkBox_Optimize_PNG.setChecked(False)

    def __on_btn_extratools_clicked(self):
        ''' Extra tools button click handler '''
        show_message(QMessageBox.Icon.Information, "Whoops! Coming Soon :*")
        return

    def __on_btn_opensvg_clicked(self):
        ''' Open svg button click handler '''
        opened_file, _ = QFileDialog.getOpenFileName(self, "Open SVG Image", "", "SVG Images (*.svg)")
        if opened_file:
            self.options.inputfile = opened_file
            self.field_svginput.setText(opened_file)

    def __on_btn_browse_inkscapepath_clicked(self):
        ''' Browse Inkscape path button click handler '''
        opened_file, _ = QFileDialog.getOpenFileName(self, "Inkscape Path", "", "Executable Files (*)")
        if opened_file:
            if os.path.isfile(opened_file) and os.access(opened_file, os.X_OK):
                self.options.inkscape_path = opened_file
                self.field_inkscape_path.setText(opened_file)
            else:
                show_message(QMessageBox.Icon.Critical, "Invalid Inkscape Executable File")
                self.btn_browse_inkscape.clicked.emit()

    def __on_btn_browse_ghostscriptpath_clicked(self):
        ''' Browse Ghostscript path button click handler '''
        opened_file, _ = QFileDialog.getOpenFileName(self, "Ghostscript Path", "", "Executable Files (*)")
        if opened_file:
            if os.path.isfile(opened_file) and os.access(opened_file, os.X_OK):
                self.options.ghostscript_path = opened_file
                self.field_ghostscript_path.setText(opened_file)
            else:
                show_message(QMessageBox.Icon.Critical, "Invalid Ghostscript Executable File")
                self.btn_browse_ghostscript.clicked.emit()

    def __on_btn_browse_pngquantpath_clicked(self):
        ''' Browse Pngquant path button click handler '''
        opened_file, _ = QFileDialog.getOpenFileName(self, "Pngquant Path", "", "Executable Files (*)")
        if opened_file:
            if os.path.isfile(opened_file) and os.access(opened_file, os.X_OK):
                self.options.pngquant_path = opened_file
                self.field_pngquant_path.setText(opened_file)
            else:
                show_message(QMessageBox.Icon.Critical, "Invalid Pngquant Executable File")
                self.btn_browse_pngquant.clicked.emit()

    def __on_btn_browse_outputdir(self):
        ''' Browse output directory button click handler '''
        output_dir = QFileDialog.getExistingDirectory(self, "Select Output Directory", "", QFileDialog.ShowDirsOnly)
        if output_dir:
            self.options.outputdir = output_dir
            self.field_exportdir.setText(output_dir)

    def __on_btn_export_clicked(self):
        ''' Button export click handler '''

        self.__prepare_export_data()

        if not self.is_valid_inkscape():
            return

        if self.options.with_booklet or (self.options.with_pdf and self.options.colorspace.upper() == "CMYK") or (self.options.with_eps and self.options.colorspace.upper() == "CMYK"):
            if not self.is_valid_ghostscript():
                return

        if not self.options.inputfile:
            show_message(QMessageBox.Icon.Critical, "No SVG specified!")
            return

        # check if inputfile is exists
        if not os.path.exists(self.options.inputfile):
            show_message(QMessageBox.Icon.Critical, f"SVG File: {self.options.inputfile} is not exist, export aborted!")
            return

        if not self.options.pattern and not self.options.pageOnly:
            show_message(QMessageBox.Icon.Critical, "Id pattern not specified, export aborted!")
            return
        if not self.__check_options():
            show_message(QMessageBox.Icon.Critical, "You're not selecting any of export choices, export aborted!")
            return

        if self.options.with_zip:
            # check if outputdir is empty, otherwise abort!
            self.export_formats.append("ZIP")
            if not self.is_outputdir_confirmed():
                return

        if self.options.optimize_png:
            if not self.is_valid_pngquant():
                return

        try:
            if os.name == "nt":
                sys.stdout = open(f'{tempfile.gettempdir()}/citramanik.log', 'w')
            else:
                sys.stdout = open(f'{self.get_tmp_exportdir()}/citramanik.log', 'w')

            parser = SVGParser(self.options.inputfile)
            if self.options.pageOnly:
                dir, filename = os.path.split(self.field_svginput.text())
                self.ids_to_process = [filename.replace(".svg", "")]
            else:
                self.ids_to_process = parser.get_objects_by_id(self.options.pattern)
            num_of_ids = len(self.ids_to_process)

            if num_of_ids < 1 :
                show_message(QMessageBox.Icon.Critical, f"Cannot find any object with id pattern {self.options.pattern}. Aborting export...")
                return

            self.process_to_finished = 0
            self.use_bitmapPNG = False
            self.use_vectorPDF = False
            self.eps_useCMYK = False
            # BITMAP-PNG
            if self.checkBox_PNG.isChecked():
                self.use_bitmapPNG = True
                self.process_to_finished += num_of_ids
                OUTDIR = f"{self.options.outputdir}{os.sep}PNG"
                if self.options.optimize_png:
                    OUTDIR = f"{self.options.outputdir}{os.sep}PNG_OPTIMIZED"
                if not os.path.exists(OUTDIR):
                    os.makedirs(OUTDIR)

            if self.checkBox_JPG.isChecked():
                self.use_bitmapPNG = True
                self.process_to_finished += num_of_ids
                OUTDIR = f"{self.options.outputdir}{os.sep}JPG"
                if self.options.is_progressive:
                    OUTDIR = f"{self.options.outputdir}{os.sep}JPG_PROGRESSIVE"
                if self.options.colorspace.upper() == "CMYK":
                    OUTDIR = f"{self.options.outputdir}{os.sep}JPG-CMYK"
                    if self.options.is_progressive:
                        OUTDIR = f"{self.options.outputdir}{os.sep}JPG_PROGRESSIVE-CMYK"
                if not os.path.exists(OUTDIR):
                    os.makedirs(OUTDIR)

            if self.checkBox_WEBP.isChecked():
                self.use_bitmapPNG = True
                self.process_to_finished += num_of_ids
                OUTDIR = f"{self.options.outputdir}{os.sep}WEBP"
                if not os.path.exists(OUTDIR):
                    os.makedirs(OUTDIR)

            # VECTOR-EPS
            if self.checkBox_EPS.isChecked():
                if self.options.colorspace == "CMYK":
                    self.use_vectorPDF = True
                    self.eps_useCMYK = True
                    OUTDIR = f"{self.options.outputdir}{os.sep}EPS-CMYK"
                    self.process_to_finished += num_of_ids
                else:
                    self.process_to_finished += num_of_ids
                    OUTDIR = f"{self.options.outputdir}{os.sep}EPS"

                if not os.path.exists(OUTDIR):
                    os.makedirs(OUTDIR)

            # VECTOR-PDF
            if self.checkBox_PDF.isChecked() or self.checkBox_BOOK.isChecked() or self.eps_useCMYK:
                self.use_vectorPDF = True
                self.process_to_finished += num_of_ids

                if self.checkBox_PDF.isChecked():
                    OUTDIR = f"{self.options.outputdir}{os.sep}PDF"
                    if self.options.colorspace == "CMYK":
                        self.process_to_finished += num_of_ids
                        OUTDIR = f"{self.options.outputdir}{os.sep}PDF-CMYK"
                    if not os.path.exists(OUTDIR):
                        os.makedirs(OUTDIR)

                if self.checkBox_BOOK.isChecked():
                    self.process_to_finished += 1
                    OUTDIR = f"{self.options.outputdir}{os.sep}BOOKLET"
                    if self.options.colorspace == "CMYK":
                        OUTDIR = f"{self.options.outputdir}{os.sep}BOOKLET-CMYK"
                    if not os.path.exists(OUTDIR):
                        os.makedirs(OUTDIR)

            # VECTOR-SVG
            if self.checkBox_SVG.isChecked():
                self.process_to_finished += num_of_ids
                OUTDIR = f"{self.options.outputdir}{os.sep}SVG"
                if not os.path.exists(OUTDIR):
                    os.makedirs(OUTDIR)

            if self.checkBox_ZIP.isChecked():
                self.process_to_finished += 1
                OUTDIR = f"{self.options.outputdir}{os.sep}ZIP"
                if not os.path.exists(OUTDIR):
                    os.makedirs(OUTDIR)

            # print(f"Number of process must be finished: {self.process_to_finished}")

            self.ourprogressbar = ProgressDialog(self)
            self.ourprogressbar.initialize_dialog(self.process_to_finished)

            # our main thread executor
            mainexports = CitraManikThread(self, self.get_tmp_exportdir())
            # connect each export format emit signal to update progressbar function
            mainexports.export_format_complete.connect(self.ourprogressbar.update_export_progression)
            # connect cancel button at progressbar to stop executor
            self.ourprogressbar.process_canceled.connect(mainexports.stop)
            # connect finish exporting process to handler
            mainexports.export_finished.connect(self.export_finished_handler)
            self.ourprogressbar.show()
            mainexports.start()

        except:
            show_message(QMessageBox.Icon.Critical, traceback.format_exc())

    def __prepare_export_data(self):
        ''' Prepare export information from user. '''
        self.options.only_booklet = False
        self.options.only_jpg = False
        self.options.only_webp = False

        self.options.inputfile = self.field_svginput.text()
        self.options.inkscape_path = self.field_inkscape_path.text()
        self.options.outputdir = self.field_exportdir.text()
        self.options.pattern = self.field_pattern.text()
        self.options.dpi = self.field_dpi.value()
        self.options.quality = self.field_quality.value()
        self.options.colorspace = self.combo_colorspace.currentText()
        self.options.with_png = self.checkBox_PNG.isChecked()
        self.options.with_jpg = self.checkBox_JPG.isChecked()
        self.options.is_progressive = self.checkBox_JPGProgressive.isChecked()
        self.options.optimize_png = self.checkBox_Optimize_PNG.isChecked()

        if self.options.with_jpg and not self.options.with_png:
            self.options.only_jpg = True

        self.options.with_eps = self.checkBox_EPS.isChecked()
        self.options.with_pdf = self.checkBox_PDF.isChecked()
        self.options.with_svg = self.checkBox_SVG.isChecked()
        self.options.with_webp = self.checkBox_WEBP.isChecked()
        if self.options.with_webp and not self.options.with_png:
            self.options.only_webp = True
        self.options.with_booklet = self.checkBox_BOOK.isChecked()
        if self.options.with_booklet and not self.options.with_pdf:
            self.options.only_booklet = True
        self.options.with_zip = self.checkBox_ZIP.isChecked()
        self.options.threads = self.spinBox_Threads.value()

    def __check_options(self):
        ''' Check if user has selected at least 1 export format '''
        choices = 0
        self.export_formats = []
        if self.options.with_svg:
            choices +=1
            self.export_formats.append("SVG")
        if self.options.with_pdf:
            choices +=1
            self.export_formats.append("PDF")
        if self.options.with_png:
            choices +=1
            self.export_formats.append("PNG")
        if self.options.with_eps:
            choices +=1
            self.export_formats.append("EPS")
        if self.options.with_webp:
            choices +=1
            self.export_formats.append("WEBP")
        if self.options.with_jpg:
            choices +=1
            self.export_formats.append("JPG")
        if self.options.with_booklet:
            choices +=1
            self.export_formats.append("BOOKLET")
        if choices > 0:
            return True
        return False

    def is_valid_inkscape(self):
        ''' Check if inkscape path provided by user or autodetected inkscape is valid. '''
        if not self.options.inkscape_path:
            self.options.inkscape_path = self.field_inkscape_path.text()

        if self.options.inkscape_path == "":
            show_message(QMessageBox.Icon.Critical, "Please set Inkscape path first. It usually in /usr/bin/inkscape for Linux or C:/Program File/Inkscape/Inkscape.exe for Windows")
            self.Settings.setFocus(True)
            return False
        res = b""
        try:
            if os.name == "nt":
                stinfo = subprocess.STARTUPINFO()
                stinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                res = subprocess.check_output([self.options.inkscape_path,"--version"], stderr=subprocess.STDOUT, startupinfo=stinfo)
            else:
                # check if user prefer to use flatpak
                if self.checkbox_flatpak.isChecked():
                    res = subprocess.check_output(["flatpak", "run", "org.inkscape.Inkscape", "--version"], stderr=subprocess.STDOUT)
                else:
                    res = subprocess.check_output([self.options.inkscape_path,"--version"], stderr=subprocess.STDOUT)
        except FileNotFoundError:
            show_message(QMessageBox.Icon.Critical, "Specified path doesn't exists! Please provide valid Inkscape path. It usually in /usr/bin/inkscape for Linux or C:/Program File/Inkscape/Inkscape.exe for Windows")
            self.Settings.setFocus(True)
            return False
        if "Inkscape" in res.decode("utf-8"):
            return True
        # check again if inkscape is found, otherwise turn exception
        show_message(QMessageBox.Icon.Critical, "Invalid Inkscape Binary! Please provide valid Inkscape path. It usually in /usr/bin/inkscape for Linux or C:/Program File/Inkscape/Inkscape.exe for Windows")
        self.Settings.setFocus(True)
        return False

    def is_valid_ghostscript(self):
        ''' Check if ghostscript path provided by user or autodetected ghostscript is valid. '''
        if not self.options.ghostscript_path:
            self.options.ghostscript_path = self.field_ghostscript_path.text()

        if self.options.ghostscript_path == "":
            show_message(QMessageBox.Icon.Critical, "Please set Ghostscript path first. It usually in /usr/bin/gs for Linux or C:/Program Files/Ghostscript/bin/gswin32c.exe for Windows")
            self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.Settings))
            return False
        res = b""
        try:
            if os.name == "nt":
                stinfo = subprocess.STARTUPINFO()
                stinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                res = subprocess.check_output([self.options.ghostscript_path,"--help"], stderr=subprocess.STDOUT, startupinfo=stinfo)
            else:
                res = subprocess.check_output([self.options.ghostscript_path,"--help"], stderr=subprocess.STDOUT)
        except FileNotFoundError:
            show_message(QMessageBox.Icon.Critical, "Specified path doesn't exists! Please provide valid Ghostscript path. It usually in /usr/bin/gs for Linux or C:/Program Files/Ghostscript/bin/gswin32c.exe for Windows")
            self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.Settings))
            return False
        if "Ghostscript" in res.decode("utf-8"):
            return True
        # check again if ghostscript is found, otherwise turn exception
        show_message(QMessageBox.Icon.Critical, "Invalid Ghostscript Binary! Please provide valid Ghostscript path. It usually in /usr/bin/gs for Linux or C:/Program Files/Ghostscript/bin/gswin32c.exe for Windows")
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.Settings))
        return False

    def is_valid_pngquant(self):
        ''' Check if pngquant path provided by user or autodetected pngquant is valid '''
        if not self.options.pngquant_path:
            self.options.pngquant_path = self.field_pngquant_path.text()

        if self.options.pngquant_path == "":
            show_message(QMessageBox.Icon.Critical, "Please set Pngquant path first. It usually in /usr/bin/pngquant for Linux")
            self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.Settings))
            return False
        res = b""
        try:
            if os.name == "nt":
                stinfo = subprocess.STARTUPINFO()
                stinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                res = subprocess.check_output([self.options.pngquant_path, "--help"], stderr=subprocess.STDOUT, startupinfo=stinfo)
            else:
                res = subprocess.check_output([self.options.pngquant_path, "--help"], stderr=subprocess.STDOUT)
        except FileNotFoundError:
            show_message(QMessageBox.Icon.Critical, "Invalid Pngquant Binary! Please provide valid Pngquant path. It usually in /usr/bin/pngquant for Linux")
            self.tabWiget.setCurrentIndex(self.tabWidget.indexOf(self.Settings))
            return False
        if "pngquant," in res.decode("utf-8"):
            return True
        # check again if pngquant is found, otherwise turn exception
        show_message(QMessageBox.Icon.Critical, "Invalid Pngquant Binary! Please provide valid Pngquant path. It usually in /usr/bin/pngquant for Linux")
        self.tabWiget.setCurrentIndex(self.tabWidget.indexOf(self.Settings))
        return False

    def is_outputdir_confirmed(self):
        ''' Confirm user to continue using selected directory that not empty '''
        if os.listdir(self.options.outputdir):
            userchoice = QMessageBox.question(self,"Warning",
                  "Your destination folder is not empty when zip option selected. "+
                  "Citramanik will read all file in your destionation folder and zip them together. "+
                  "You can choose empty directory for zipping current export only. Export anyway?",
                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
            if userchoice == QMessageBox.StandardButton.Yes:
                return True
            show_message(QMessageBox.Icon.Information, "Export aborted")
            return False
        return True

    def export_finished_handler(self, failedjobs, elapsed_time):
        ''' Handler for completing all exports '''
        # remove temporary directory
        if len(failedjobs) > 0:
            shutil.copy2(f'{self.get_tmp_exportdir()}/citramanik.log', self.options.outputdir)
        shutil.rmtree(self.get_tmp_exportdir())
        self.__tmp_exportsdir = None
        # show failed jobs if exists
        if len(failedjobs) < 1:
            # all exports was successful
            export_formats = ", ".join(self.export_formats)
            if self.options.pageOnly:
                dir, filename = os.path.split(self.field_svginput.text())
                self.ids_to_process = [filename.replace(".svg", "")]
                msg = f"{filename} was successfully exported as {export_formats} in {self.options.outputdir} in {elapsed_time}"
            else:
                msg = f"{len(self.ids_to_process)} objects with pattern {self.options.pattern} was successfully exported as {export_formats} in {self.options.outputdir} in {elapsed_time}"
            show_message(QMessageBox.Icon.Information, msg)
            return
        self.ourprogressbar.close()
        self.centralwidget.setEnabled(True)
        unexported = ", ".join(i for i,o in failedjobs)
        msg = f"Problem occured when exporting these object with id: {unexported}.\nFailed Jobs: {len(failedjobs)}\nTotal Process: {self.process_to_finished}\nSee citramanik.log in your output directory for details"
        show_message(QMessageBox.Icon.Critical, msg, True)

    def get_tmp_exportdir(self):
        ''' Get temporary directory path for exporting. It will be removed after exports. The prefix is CITRAMANIK_TEMP '''
        if self.__tmp_exportsdir:
            return self.__tmp_exportsdir
        self.__tmp_exportsdir = tempfile.mkdtemp(prefix="CITRAMANIK_TEMP_")
        return self.__tmp_exportsdir

    def closeEvent(self, event):
        ''' Fired when user close window through close button '''
        # save last config to user config dir
        self.appconfigs.set_dpi(self.field_dpi.value())
        self.appconfigs.set_ghostscript_path(self.field_ghostscript_path.text())
        self.appconfigs.set_inkscape_path(self.field_inkscape_path.text())
        self.appconfigs.set_pngquant_path(self.field_pngquant_path.text())
        self.appconfigs.set_threads_config(self.spinBox_Threads.value())
        self.appconfigs.set_output_dir(self.field_exportdir.text())
        self.appconfigs.set_quality(self.field_quality.value())
        self.appconfigs.set_use_flatpak(self.checkbox_flatpak.isChecked())
        self.appconfigs.write_to_file()
