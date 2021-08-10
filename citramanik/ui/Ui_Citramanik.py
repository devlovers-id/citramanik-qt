# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dev-ui/citramanik.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from citramanik.ui.citramanik_resources_rc import *
from citramanik import get_versions, __donate_url__, __website_url__

class Ui_Citramanik(object):
    versions = get_versions()
    def setupUi(self, Citramanik):
        Citramanik.setObjectName("Citramanik")
        Citramanik.resize(481, 491)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Citramanik.sizePolicy().hasHeightForWidth())
        Citramanik.setSizePolicy(sizePolicy)
        Citramanik.setMinimumSize(QtCore.QSize(481, 491))
        Citramanik.setMaximumSize(QtCore.QSize(481, 491))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/imgs/citramanik-qt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Citramanik.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Citramanik)
        self.centralwidget.setObjectName("centralwidget")
        self.topframe = QtWidgets.QFrame(self.centralwidget)
        self.topframe.setGeometry(QtCore.QRect(0, 0, 481, 131))
        self.topframe.setAutoFillBackground(False)
        self.topframe.setStyleSheet("background-color: rgba(234, 56, 159, 0.7);\n"
"background-image: url(:/image/imgs/img-bg-sections.png);")
        self.topframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topframe.setObjectName("topframe")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.topframe)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.banner_update = QtWidgets.QLabel(self.topframe)
        self.banner_update.setMinimumSize(QtCore.QSize(0, 32))
        self.banner_update.setMaximumSize(QtCore.QSize(16777215, 32))
        self.banner_update.setStyleSheet("background: rgba(208, 123, 187, 0.3)")
        self.banner_update.setAlignment(QtCore.Qt.AlignCenter)
        self.banner_update.setOpenExternalLinks(True)
        self.banner_update.setObjectName("banner_update")
        self.verticalLayout_6.addWidget(self.banner_update)
        self.wrapper_topframe = QtWidgets.QHBoxLayout()
        self.wrapper_topframe.setObjectName("wrapper_topframe")
        self.btn_opensvg = QtWidgets.QToolButton(self.topframe)
        self.btn_opensvg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_opensvg.setAutoFillBackground(False)
        self.btn_opensvg.setStyleSheet("border:0px solid;\n"
"background:none;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/imgs/ic_Add.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_opensvg.setIcon(icon1)
        self.btn_opensvg.setIconSize(QtCore.QSize(48, 48))
        self.btn_opensvg.setCheckable(False)
        self.btn_opensvg.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_opensvg.setObjectName("btn_opensvg")
        self.wrapper_topframe.addWidget(self.btn_opensvg)
        spacerItem = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.wrapper_topframe.addItem(spacerItem)
        self.btn_extratools = QtWidgets.QToolButton(self.topframe)
        self.btn_extratools.setEnabled(True)
        self.btn_extratools.setAutoFillBackground(False)
        self.btn_extratools.setStyleSheet("border:0px solid;\n"
"background:none;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/imgs/ic_extension.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_extratools.setIcon(icon2)
        self.btn_extratools.setIconSize(QtCore.QSize(48, 48))
        self.btn_extratools.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_extratools.setObjectName("btn_extratools")
        self.wrapper_topframe.addWidget(self.btn_extratools)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.wrapper_topframe.addItem(spacerItem1)
        self.btn_export = QtWidgets.QToolButton(self.topframe)
        self.btn_export.setStyleSheet("border:0px solid;\n"
"background:none;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/image/imgs/ic_Export.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_export.setIcon(icon3)
        self.btn_export.setIconSize(QtCore.QSize(48, 48))
        self.btn_export.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_export.setObjectName("btn_export")
        self.wrapper_topframe.addWidget(self.btn_export)
        self.verticalLayout_6.addLayout(self.wrapper_topframe)
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setGeometry(QtCore.QRect(0, 130, 481, 361))
        self.mainFrame.setStyleSheet("")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.tabWidget = QtWidgets.QTabWidget(self.mainFrame)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 480, 361))
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setObjectName("tabWidget")
        self.MainSetting = QtWidgets.QWidget()
        self.MainSetting.setStyleSheet("")
        self.MainSetting.setObjectName("MainSetting")
        self.layoutWidget = QtWidgets.QWidget(self.MainSetting)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 431, 294))
        self.layoutWidget.setObjectName("layoutWidget")
        self.wrapper_main = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.wrapper_main.setContentsMargins(0, 0, 0, 0)
        self.wrapper_main.setObjectName("wrapper_main")
        self.wrapper_svg = QtWidgets.QVBoxLayout()
        self.wrapper_svg.setObjectName("wrapper_svg")
        self.label_svgprocess = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_svgprocess.setFont(font)
        self.label_svgprocess.setStyleSheet("")
        self.label_svgprocess.setObjectName("label_svgprocess")
        self.wrapper_svg.addWidget(self.label_svgprocess)
        self.field_svginput = QtWidgets.QLineEdit(self.layoutWidget)
        self.field_svginput.setEnabled(False)
        self.field_svginput.setMinimumSize(QtCore.QSize(0, 30))
        self.field_svginput.setAutoFillBackground(False)
        self.field_svginput.setObjectName("field_svginput")
        self.wrapper_svg.addWidget(self.field_svginput)
        self.wrapper_idpattern = QtWidgets.QHBoxLayout()
        self.wrapper_idpattern.setObjectName("wrapper_idpattern")
        self.combo_export_mode = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_export_mode.setMinimumSize(QtCore.QSize(0, 0))
        self.combo_export_mode.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.combo_export_mode.setObjectName("combo_export_mode")
        self.combo_export_mode.addItem("")
        self.combo_export_mode.addItem("")
        self.wrapper_idpattern.addWidget(self.combo_export_mode)
        self.label_idpattern = QtWidgets.QLabel(self.layoutWidget)
        self.label_idpattern.setStyleSheet("")
        self.label_idpattern.setObjectName("label_idpattern")
        self.wrapper_idpattern.addWidget(self.label_idpattern)
        self.field_pattern = QtWidgets.QLineEdit(self.layoutWidget)
        self.field_pattern.setMinimumSize(QtCore.QSize(0, 30))
        self.field_pattern.setText("")
        self.field_pattern.setObjectName("field_pattern")
        self.wrapper_idpattern.addWidget(self.field_pattern)
        self.wrapper_svg.addLayout(self.wrapper_idpattern)
        self.wrapper_main.addLayout(self.wrapper_svg)
        spacerItem2 = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.wrapper_main.addItem(spacerItem2)
        self.wrapper_exports = QtWidgets.QVBoxLayout()
        self.wrapper_exports.setObjectName("wrapper_exports")
        self.label_exportformats = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_exportformats.setFont(font)
        self.label_exportformats.setStyleSheet("")
        self.label_exportformats.setObjectName("label_exportformats")
        self.wrapper_exports.addWidget(self.label_exportformats)
        self.wrapper_exportcheckbox = QtWidgets.QHBoxLayout()
        self.wrapper_exportcheckbox.setObjectName("wrapper_exportcheckbox")
        self.checkBox_PNG = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_PNG.setObjectName("checkBox_PNG")
        self.wrapper_exportcheckbox.addWidget(self.checkBox_PNG)
        self.checkBox_JPG = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_JPG.setObjectName("checkBox_JPG")
        self.wrapper_exportcheckbox.addWidget(self.checkBox_JPG)
        self.checkBox_EPS = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_EPS.setObjectName("checkBox_EPS")
        self.wrapper_exportcheckbox.addWidget(self.checkBox_EPS)
        self.checkBox_PDF = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_PDF.setObjectName("checkBox_PDF")
        self.wrapper_exportcheckbox.addWidget(self.checkBox_PDF)
        self.checkBox_SVG = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_SVG.setObjectName("checkBox_SVG")
        self.wrapper_exportcheckbox.addWidget(self.checkBox_SVG)
        self.checkBox_WEBP = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_WEBP.setObjectName("checkBox_WEBP")
        self.wrapper_exportcheckbox.addWidget(self.checkBox_WEBP)
        self.checkBox_BOOK = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_BOOK.setObjectName("checkBox_BOOK")
        self.wrapper_exportcheckbox.addWidget(self.checkBox_BOOK)
        self.wrapper_exports.addLayout(self.wrapper_exportcheckbox)
        self.wrapper_main.addLayout(self.wrapper_exports)
        spacerItem3 = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.wrapper_main.addItem(spacerItem3)
        self.wrapper_extraparams = QtWidgets.QVBoxLayout()
        self.wrapper_extraparams.setObjectName("wrapper_extraparams")
        self.label_extraparams = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_extraparams.setFont(font)
        self.label_extraparams.setStyleSheet("")
        self.label_extraparams.setObjectName("label_extraparams")
        self.wrapper_extraparams.addWidget(self.label_extraparams)
        self.wrapper_extramaparamsfield = QtWidgets.QHBoxLayout()
        self.wrapper_extramaparamsfield.setObjectName("wrapper_extramaparamsfield")
        self.label_dpi = QtWidgets.QLabel(self.layoutWidget)
        self.label_dpi.setStyleSheet("")
        self.label_dpi.setObjectName("label_dpi")
        self.wrapper_extramaparamsfield.addWidget(self.label_dpi)
        self.field_dpi = QtWidgets.QSpinBox(self.layoutWidget)
        self.field_dpi.setMinimumSize(QtCore.QSize(100, 30))
        self.field_dpi.setMaximum(200000)
        self.field_dpi.setObjectName("field_dpi")
        self.wrapper_extramaparamsfield.addWidget(self.field_dpi)
        self.label_quality = QtWidgets.QLabel(self.layoutWidget)
        self.label_quality.setStyleSheet("")
        self.label_quality.setObjectName("label_quality")
        self.wrapper_extramaparamsfield.addWidget(self.label_quality)
        self.field_quality = QtWidgets.QSpinBox(self.layoutWidget)
        self.field_quality.setMinimumSize(QtCore.QSize(80, 30))
        self.field_quality.setObjectName("field_quality")
        self.wrapper_extramaparamsfield.addWidget(self.field_quality)
        self.label_colorspace = QtWidgets.QLabel(self.layoutWidget)
        self.label_colorspace.setStyleSheet("")
        self.label_colorspace.setObjectName("label_colorspace")
        self.wrapper_extramaparamsfield.addWidget(self.label_colorspace)
        self.combo_colorspace = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_colorspace.setObjectName("combo_colorspace")
        self.combo_colorspace.addItem("")
        self.combo_colorspace.addItem("")
        self.wrapper_extramaparamsfield.addWidget(self.combo_colorspace)
        self.wrapper_extraparams.addLayout(self.wrapper_extramaparamsfield)
        self.wrapper_main.addLayout(self.wrapper_extraparams)
        spacerItem4 = QtWidgets.QSpacerItem(17, 228, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.wrapper_main.addItem(spacerItem4)
        self.wrapper_zips = QtWidgets.QHBoxLayout()
        self.wrapper_zips.setObjectName("wrapper_zips")
        self.checkBox_ZIP = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_ZIP.setStyleSheet("")
        self.checkBox_ZIP.setObjectName("checkBox_ZIP")
        self.wrapper_zips.addWidget(self.checkBox_ZIP)
        spacerItem5 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.wrapper_zips.addItem(spacerItem5)
        self.wrapper_saveto = QtWidgets.QHBoxLayout()
        self.wrapper_saveto.setObjectName("wrapper_saveto")
        self.label_saveto = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_saveto.setFont(font)
        self.label_saveto.setStyleSheet("")
        self.label_saveto.setObjectName("label_saveto")
        self.wrapper_saveto.addWidget(self.label_saveto)
        self.field_exportdir = QtWidgets.QLineEdit(self.layoutWidget)
        self.field_exportdir.setEnabled(False)
        self.field_exportdir.setMinimumSize(QtCore.QSize(65, 30))
        self.field_exportdir.setStyleSheet("")
        self.field_exportdir.setReadOnly(False)
        self.field_exportdir.setObjectName("field_exportdir")
        self.wrapper_saveto.addWidget(self.field_exportdir)
        self.btn_browse_outputdir = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_browse_outputdir.setMinimumSize(QtCore.QSize(80, 28))
        self.btn_browse_outputdir.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_browse_outputdir.setStyleSheet("QPushButton{\n"
"background-color: rgba(234, 56, 159, 0.7);\n"
"border:none;\n"
"border-radius: 2px;\n"
"}")
        self.btn_browse_outputdir.setObjectName("btn_browse_outputdir")
        self.wrapper_saveto.addWidget(self.btn_browse_outputdir)
        self.wrapper_zips.addLayout(self.wrapper_saveto)
        self.wrapper_main.addLayout(self.wrapper_zips)
        self.tabWidget.addTab(self.MainSetting, "")
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.layoutWidget_2 = QtWidgets.QWidget(self.Settings)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 25, 431, 161))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.wrapper_settings = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.wrapper_settings.setContentsMargins(0, 0, 0, 0)
        self.wrapper_settings.setObjectName("wrapper_settings")
        self.wrapper_threads = QtWidgets.QHBoxLayout()
        self.wrapper_threads.setObjectName("wrapper_threads")
        self.label_threads = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_threads.setStyleSheet("")
        self.label_threads.setObjectName("label_threads")
        self.wrapper_threads.addWidget(self.label_threads)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.wrapper_threads.addItem(spacerItem6)
        self.spinBox_Threads = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.spinBox_Threads.setStyleSheet("")
        self.spinBox_Threads.setMinimum(1)
        self.spinBox_Threads.setMaximum(16)
        self.spinBox_Threads.setObjectName("spinBox_Threads")
        self.wrapper_threads.addWidget(self.spinBox_Threads)
        self.wrapper_settings.addLayout(self.wrapper_threads)
        self.wrapper_inkscape = QtWidgets.QHBoxLayout()
        self.wrapper_inkscape.setObjectName("wrapper_inkscape")
        self.label_inkscape = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_inkscape.setStyleSheet("")
        self.label_inkscape.setObjectName("label_inkscape")
        self.wrapper_inkscape.addWidget(self.label_inkscape)
        spacerItem7 = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.wrapper_inkscape.addItem(spacerItem7)
        self.field_inkscape_path = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.field_inkscape_path.setMinimumSize(QtCore.QSize(0, 28))
        self.field_inkscape_path.setObjectName("field_inkscape_path")
        self.wrapper_inkscape.addWidget(self.field_inkscape_path)
        self.btn_browse_inkscape = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btn_browse_inkscape.setMinimumSize(QtCore.QSize(80, 28))
        self.btn_browse_inkscape.setStyleSheet("QPushButton{\n"
"background-color: rgba(234, 56, 159, 0.7);\n"
"border-radius: 2px;\n"
"}")
        self.btn_browse_inkscape.setObjectName("btn_browse_inkscape")
        self.wrapper_inkscape.addWidget(self.btn_browse_inkscape)
        self.wrapper_settings.addLayout(self.wrapper_inkscape)
        self.wrapper_ghostscript = QtWidgets.QHBoxLayout()
        self.wrapper_ghostscript.setObjectName("wrapper_ghostscript")
        self.label_ghostscript = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_ghostscript.setStyleSheet("")
        self.label_ghostscript.setObjectName("label_ghostscript")
        self.wrapper_ghostscript.addWidget(self.label_ghostscript)
        spacerItem8 = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.wrapper_ghostscript.addItem(spacerItem8)
        self.field_ghostscript_path = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.field_ghostscript_path.setMinimumSize(QtCore.QSize(0, 28))
        self.field_ghostscript_path.setObjectName("field_ghostscript_path")
        self.wrapper_ghostscript.addWidget(self.field_ghostscript_path)
        self.btn_browse_ghostscript = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btn_browse_ghostscript.setMinimumSize(QtCore.QSize(80, 28))
        self.btn_browse_ghostscript.setStyleSheet("QPushButton{\n"
"background-color: rgba(234, 56, 159, 0.7);\n"
"border-radius: 2px;\n"
"}")
        self.btn_browse_ghostscript.setObjectName("btn_browse_ghostscript")
        self.wrapper_ghostscript.addWidget(self.btn_browse_ghostscript)
        self.wrapper_settings.addLayout(self.wrapper_ghostscript)
        self.darkTheme = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.darkTheme.setEnabled(False)
        self.darkTheme.setStyleSheet("")
        self.darkTheme.setObjectName("darkTheme")
        self.wrapper_settings.addWidget(self.darkTheme)
        spacerItem9 = QtWidgets.QSpacerItem(20, 236, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.wrapper_settings.addItem(spacerItem9)
        self.tabWidget.addTab(self.Settings, "")
        self.About = QtWidgets.QWidget()
        self.About.setObjectName("About")
        self.layoutWidget1 = QtWidgets.QWidget(self.About)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 451, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.wrapper_logocitramanik = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.wrapper_logocitramanik.setContentsMargins(0, 0, 0, 0)
        self.wrapper_logocitramanik.setObjectName("wrapper_logocitramanik")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.label_logocitramanik = QtWidgets.QLabel(self.layoutWidget1)
        self.label_logocitramanik.setEnabled(True)
        self.label_logocitramanik.setMaximumSize(QtCore.QSize(128, 16777215))
        self.label_logocitramanik.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_logocitramanik.setText("")
        self.label_logocitramanik.setPixmap(QtGui.QPixmap(":/image/imgs/citramanik-qt.png"))
        self.label_logocitramanik.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logocitramanik.setObjectName("label_logocitramanik")
        self.horizontalLayout.addWidget(self.label_logocitramanik)
        self.wrapper_title_3 = QtWidgets.QVBoxLayout()
        self.wrapper_title_3.setObjectName("wrapper_title_3")
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.wrapper_title_3.addItem(spacerItem11)
        self.label_title_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_title_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans [MONO]")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_3.setFont(font)
        self.label_title_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_title_3.setStyleSheet("color: rgba(234, 56, 159, 1);")
        self.label_title_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_title_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_3.setObjectName("label_title_3")
        self.wrapper_title_3.addWidget(self.label_title_3)
        self.label_slug_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Noto Sans [MONO]")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_slug_3.setFont(font)
        self.label_slug_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_slug_3.setStyleSheet("color: rgba(234, 56, 159, 1);")
        self.label_slug_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slug_3.setObjectName("label_slug_3")
        self.wrapper_title_3.addWidget(self.label_slug_3)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.wrapper_title_3.addItem(spacerItem12)
        self.horizontalLayout.addLayout(self.wrapper_title_3)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem13)
        self.wrapper_logocitramanik.addLayout(self.horizontalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.About)
        self.textBrowser.setGeometry(QtCore.QRect(10, 160, 451, 151))
        font = QtGui.QFont()
        font.setFamily("Noto Sans [GOOG]")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.About, "")
        self.mainFrame.raise_()
        self.topframe.raise_()
        Citramanik.setCentralWidget(self.centralwidget)

        self.retranslateUi(Citramanik)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Citramanik)

    def retranslateUi(self, Citramanik):
        _translate = QtCore.QCoreApplication.translate
        Citramanik.setWindowTitle(_translate("Citramanik", "Citramanik - More Export, Less Effort"))
        self.banner_update.setText(_translate("Citramanik", "<html><head/><body><p><a href=\"http://localhost:8000\"><span style=\" text-decoration: none; color:#fff;\">New Version ${version} is available!</span></a></p></body></html>"))
        self.btn_opensvg.setText(_translate("Citramanik", "Open SVG"))
        self.btn_extratools.setText(_translate("Citramanik", "Extra Tool"))
        self.btn_export.setText(_translate("Citramanik", "Start Export !"))
        self.label_svgprocess.setText(_translate("Citramanik", "SVG to Process"))
        self.field_svginput.setPlaceholderText(_translate("Citramanik", "Choose Your SVG(s)"))
        self.combo_export_mode.setItemText(0, _translate("Citramanik", "Multi Export (By ID)"))
        self.combo_export_mode.setItemText(1, _translate("Citramanik", "Page Export (Without ID)"))
        self.label_idpattern.setText(_translate("Citramanik", "ID Pattern"))
        self.field_pattern.setPlaceholderText(_translate("Citramanik", "Object ID or Pattern"))
        self.label_exportformats.setText(_translate("Citramanik", "Export Formats"))
        self.checkBox_PNG.setText(_translate("Citramanik", "PNG"))
        self.checkBox_JPG.setText(_translate("Citramanik", "JPG"))
        self.checkBox_EPS.setText(_translate("Citramanik", "EPS"))
        self.checkBox_PDF.setText(_translate("Citramanik", "PDF"))
        self.checkBox_SVG.setText(_translate("Citramanik", "SVG"))
        self.checkBox_WEBP.setText(_translate("Citramanik", "WebP"))
        self.checkBox_BOOK.setText(_translate("Citramanik", "Booklet"))
        self.label_extraparams.setText(_translate("Citramanik", "Extra Parameters"))
        self.label_dpi.setText(_translate("Citramanik", "DPI"))
        self.label_quality.setText(_translate("Citramanik", "Quality"))
        self.label_colorspace.setText(_translate("Citramanik", "Colorspace"))
        self.combo_colorspace.setItemText(0, _translate("Citramanik", "CMYK"))
        self.combo_colorspace.setItemText(1, _translate("Citramanik", "RGB"))
        self.checkBox_ZIP.setText(_translate("Citramanik", "ZIP Result"))
        self.label_saveto.setText(_translate("Citramanik", "Save to : "))
        self.field_exportdir.setPlaceholderText(_translate("Citramanik", "Browse Directory"))
        self.btn_browse_outputdir.setText(_translate("Citramanik", "Browse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MainSetting), _translate("Citramanik", "Main Setting"))
        self.label_threads.setText(_translate("Citramanik", "Threads to use (4-8 is recommended)"))
        self.label_inkscape.setText(_translate("Citramanik", "Inkscape Path"))
        self.btn_browse_inkscape.setText(_translate("Citramanik", "Browse"))
        self.label_ghostscript.setText(_translate("Citramanik", "Ghostscript Path"))
        self.btn_browse_ghostscript.setText(_translate("Citramanik", "Browse"))
        self.darkTheme.setText(_translate("Citramanik", "Use Dark Theme (Coming Soon)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("Citramanik", "Settings"))
        self.label_title_3.setText(_translate("Citramanik", "Citramanik"))
        self.label_slug_3.setText(_translate("Citramanik", "More export, Less Effort!"))
        self.textBrowser.setHtml(_translate("Citramanik", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans [GOOG]\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans [MONO]\'; font-size:10pt;\">Citramanik is the next generation of Inkporter developed by Devlovers ID. This tool can export objects based on the ID pattern that you have previously set in Inkscape.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans [MONO]\'; font-size:10pt;\">Citramanik supports SVG, PNG, JPG, PDF, EPS, and WEBP export formats. You can also activate CMYK color format support for JPG and PDF export formats. Apart from that, you can also export multiple PDF pages at one time by selecting the booklet export format.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans [MONO]\'; font-size:10pt;\">We also added an export archive feature to help those of you who work on microstock or other design marketplaces.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans [MONO]\'; font-size:10pt;\">Citramanik Version: 1.1.0</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans [MONO]\'; font-size:10pt;\">Details:<br /></span><a href=\"https://citramanik.dev-is.my.id\"><span style=\" font-family:\'Inter\'; text-decoration: underline; color:#1d99f3;\">https://citramanik.dev-is.my.id</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans [MONO]\'; font-size:10pt;\">Donation:<br /></span><a href=\"https://support.dev-is.my.id\"><span style=\" font-family:\'Inter\'; text-decoration: underline; color:#1d99f3;\">https://support.dev-is.my.id</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans [MONO]\'; font-size:10pt;\">About Qt:<br /></span><a href=\"https://www.qt.io\"><span style=\" font-family:\'Inter\'; text-decoration: underline; color:#1d99f3;\">https://www.qt.io</span></a></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.About), _translate("Citramanik", "About"))
