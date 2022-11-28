import os
import subprocess
import sys
import zipfile
import concurrent.futures
import traceback

from PIL import Image
from shutil import copy2

from PyQt6.QtCore import QThread, pyqtSignal
from citramanik.handler.error import CitraManikCancelException
from citramanik.utils.sorter import natural_sort
from citramanik.utils.timer import CitramanikTimer


class CitraManikThread(QThread):
    '''
    Citramanik Main Process Threads.
    each completed export format will emit export_format_complete, so we can transfer this signal to progress bar to update progression.
    if all exports finished, it will emit export_finished signal with specific successful/failed export lists.
    '''

    export_format_complete = pyqtSignal(str)
    export_finished = pyqtSignal(list, str)

    cancel = False
    time_counter = CitramanikTimer()

    def __init__(self, parent, tempdir):
        super(CitraManikThread, self).__init__(parent=parent)
        self.inkscape = [parent.options.inkscape_path]
        self.colorspace = parent.options.colorspace.upper()
        self.outputdir = parent.options.outputdir
        self.dpi = parent.options.dpi
        self.quality = parent.options.quality
        self.inputfile = parent.options.inputfile
        self.pattern = parent.options.pattern
        self.with_png = parent.options.with_png
        self.with_jpg = parent.options.with_jpg
        self.with_webp = parent.options.with_webp
        self.with_svg = parent.options.with_svg
        self.with_eps = parent.options.with_eps
        self.with_pdf = parent.options.with_pdf
        self.with_booklet = parent.options.with_booklet
        self.with_zip = parent.options.with_zip
        self.only_jpg = parent.options.only_jpg
        self.only_webp = parent.options.only_webp
        self.only_booklet = parent.options.only_booklet
        self.num_threads = parent.options.threads
        self.ids_to_process = parent.ids_to_process
        self.use_bitmapPNG = parent.use_bitmapPNG
        self.use_vectorPDF = parent.use_vectorPDF
        self.eps_useCMYK = parent.eps_useCMYK
        self.gs_binary = parent.options.ghostscript_path
        self.is_progressive = parent.options.is_progressive
        self.optimize_png = parent.options.optimize_png
        self.pngquant = parent.options.pngquant_path
        self.onlyPage = parent.options.pageOnly

        if parent.use_flatpak:
            self.inkscape = ["flatpak", "run", "--filesystem=/tmp", "org.inkscape.Inkscape"]

        self.tempdir = tempdir
        self.booklet_pages = []

    def toBeProcessed(self, idItem):
        if not self.onlyPage:
            argument = f"--export-id={idItem}"
        else:
            argument = "--export-area-page"
            
        return argument

    def process_call(self, command):
        # CREATE_NO_WINDOW = 0x08000000
        if os.name == "nt":
            stinfo = subprocess.STARTUPINFO()
            stinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            subprocess.Popen(command, startupinfo=stinfo, stdout=sys.stdout, stderr=sys.stdout).wait()
        else:
            subprocess.Popen(command, stdout=sys.stdout, stderr=sys.stdout).wait()

    def execute_task_jpg(self, item, is_progressive):
        target_jpg= f"{self.outputdir}{os.sep}JPG{os.sep}{os.path.basename(item)[:-4]}.jpg"
        if is_progressive:
            target_jpg= f"{self.outputdir}{os.sep}JPG_PROGRESSIVE{os.sep}{os.path.basename(item)[:-4]}.jpg"
        if self.colorspace == "CMYK":
            newname = os.path.basename(target_jpg)[:-4] + "-CMYK.jpg"
            dirname = os.path.dirname(target_jpg) + "-CMYK"
            target_jpg = dirname + os.sep + newname
        Image.open(item).convert(self.colorspace).save(target_jpg, quality=self.quality, progression=is_progressive)
        return target_jpg

    def execute_task_optimize_png(self, item):
        ''' Optimize PNG (pngquant) Executor '''
        target_optimized_png = f"{self.outputdir}{os.sep}PNG_OPTIMIZED{os.sep}{os.path.basename(item)[:-4]}.png" 
        command = [ self.pngquant, item, "-f", "-o", target_optimized_png ]
        self.process_call(command)
        return target_optimized_png


    def execute_task_png(self, item):
        ''' PNG exports executor '''

        if self.cancel:
            if self.with_png:
                idformat = "png"
            if self.with_jpg:
                idformat += "+jpg"
            if self.with_webp:
                idformat += "+webp"
            raise CitraManikCancelException(idformat, item)

        temp_png = f"{self.tempdir}{os.sep}{item}.png"
        command = self.inkscape + [ self.toBeProcessed(item), "--export-id-only", f"--export-dpi={self.dpi}", "--export-type=png", f"--export-filename={temp_png}", self.inputfile ]
        # subprocess.Popen(command).wait()
        self.process_call(command)
        ccc = f"{temp_png} processed!"
        if self.with_jpg or self.with_webp:
            if self.with_jpg:
                target_jpg = self.execute_task_jpg(temp_png, self.is_progressive)
                self.export_format_complete.emit(f"{item}.jpg")
                ccc += f" dan {target_jpg} processed!"
            if self.with_webp:
                target_webp = f"{self.outputdir}{os.sep}WEBP{os.sep}{item}.webp"
                Image.open(temp_png).convert("RGBA").save(target_webp, quality=self.quality)
                self.export_format_complete.emit(f"{item}.webp")
                ccc += f" dan {target_webp} processed!"
        if self.with_png:
            if self.optimize_png:
                target_optimized = self.execute_task_optimize_png(temp_png)
                ccc += f" dan {target_optimized} processed!"
            else:
                target_png = f"{self.outputdir}{os.sep}PNG"
                copy2(temp_png, target_png)
            self.export_format_complete.emit(f"{item}.png")
        return ccc

    def execute_task_pdf(self, item):
        ''' PDF exports executor '''

        if self.cancel:
            idformat = "pdf"
            raise CitraManikCancelException(idformat, item)
        pdf_temp = f"{self.tempdir}{os.sep}{item}.pdf"
        command = self.inkscape + [ self.toBeProcessed(item), "--export-id-only", f"--export-dpi={self.dpi}", "--export-type=pdf", f"--export-filename={pdf_temp}", self.inputfile ]
        # subprocess.Popen(command).wait()
        self.process_call(command)
        ccc = f"{pdf_temp} processed!"
        self.export_format_complete.emit(f"{item}.pdf")

        if self.colorspace == "CMYK":
            pdf_cmyk_temp = f"{self.tempdir}{os.sep}{item}-cmyk.pdf"
            command = [ self.gs_binary, "-dSAFER", "-dBATCH", "-dNOPAUSE", "-dNOCACHE", "-sDEVICE=pdfwrite",
                    "-sColorConversionStrategy=CMYK", "-dProcessColorModel=/DeviceCMYK",
                    f"-sOutputFile={pdf_cmyk_temp}", pdf_temp ]
            # subprocess.Popen(command).wait()
            self.process_call(command)
            # os.system(f'"{self.gs_binary}" -dSAFER -dBATCH -dNOPAUSE -dNOCACHE -sDEVICE=pdfwrite -sColorConversionStrategy=CMYK -dProcessColorModel=/DeviceCMYK -sOutputFile="{pdf_cmyk_temp}" "{pdf_temp}"')
            self.booklet_pages.append(pdf_cmyk_temp)
        else:
            self.booklet_pages.append(pdf_temp)

        if self.with_pdf:
            if self.colorspace == "CMYK":
                OUTDIR = f"{self.outputdir}{os.sep}PDF-CMYK"
                target_pdfcmyk = f"{self.outputdir}{os.sep}PDF-CMYK{os.sep}{item}-CMYK.pdf"
                self.export_format_complete.emit(f"{item}-CMYK.pdf")
                copy2(pdf_cmyk_temp, target_pdfcmyk)
                ccc +=f"PDF CMYK Done {target_pdfcmyk}"
            else:
                OUTDIR = f"{self.outputdir}{os.sep}PDF"
                target_pdf = f"{OUTDIR}{os.sep}{item}.pdf"
                copy2(pdf_temp, target_pdf)
                ccc += f"PDF Done {target_pdf}"

        if self.eps_useCMYK:
            target_epscmyk = f"{self.outputdir}{os.sep}EPS-CMYK{os.sep}{item}-CMYK.eps"
            command = [ self.gs_binary, "-dSAFER", "-dBATCH", "-dNOPAUSE", "-dNOCACHE", "-sDEVICE=pdfwrite",
                    "-sColorConversionStrategy=CMYK", "-dProcessColorModel=/DeviceCMYK",
                    f"-sOutputFile={target_epscmyk}", pdf_temp ]
            # subprocess.Popen(command).wait()
            self.process_call(command)
            # os.system(f'"{self.gs_binary}" -q -dSAFER -dBATCH -dNOPAUSE -dNOCACHE -sDEVICE=pdfwrite -sColorConversionStrategy=CMYK -dProcessColorModel=/DeviceCMYK -sOutputFile="{target_epscmyk}" "{pdf_temp}"')
            self.export_format_complete.emit(f"{item}-CMYK.eps")
            ccc += f"{target_epscmyk} processed!"
        return ccc

    def execute_task_eps(self, item):
        ''' EPS exports executor '''

        if self.cancel:
            idformat = "eps"
            raise CitraManikCancelException(idformat, item)
        OUTDIR = f"{self.outputdir}{os.sep}EPS"
        target_eps = f"{OUTDIR}{os.sep}{item}.eps"
        command = self.inkscape + [ self.toBeProcessed(item), "--export-id-only", f"--export-dpi={self.dpi}", "--export-type=eps", f"--export-filename={target_eps}", self.inputfile ]
        # subprocess.Popen(command).wait()
        self.process_call(command)
        self.export_format_complete.emit(f"{item}.eps")
        ccc = f"{target_eps} processed!"
        return ccc

    def execute_task_svg(self, item):
        ''' SVG exports executor '''

        if self.cancel:
            idformat = "svg"
            raise CitraManikCancelException(idformat, item)
        OUTDIR = f"{self.outputdir}{os.sep}SVG"
        target_svg = f"{OUTDIR}/{item}.svg"
        command = self.inkscape + [ self.toBeProcessed(item), "--export-id-only", f"--export-dpi={self.dpi}", "--export-type=svg", "--export-plain-svg", f"--export-filename={target_svg}", self.inputfile ]
         # subprocess.Popen(command).wait()
        self.process_call(command)
        ccc = f"{target_svg} processed!"
        self.export_format_complete.emit(f"{item}.svg")
        return ccc

    def execute_task_booklet(self):
        ''' Booklet exports executor '''

        if self.cancel:
            idformat = "booklet"
            raise CitraManikCancelException(idformat, "Converting all objects to booklet")
        OUTDIR = f"{self.outputdir}{os.sep}BOOKLET"
        # LOOKDIR = self.outputdir + "/PDF"
        target_booklet = f"{OUTDIR}{os.sep}{self.pattern}-booklet.pdf"
        emit_msg = f"{self.pattern}-booklet.pdf"
        if self.colorspace == "CMYK":
            OUTDIR = f"{self.outputdir}{os.sep}BOOKLET-CMYK"
            target_booklet = f"{OUTDIR}{os.sep}{self.pattern}-booklet-cmyk.pdf"
            emit_msg = f"{self.pattern}-booklet-cmyk.pdf"
        booklet_pages = natural_sort(self.booklet_pages)
        # cmd = f'"{self.gs_binary}" -q -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -sOutputFile="{target_booklet}" ' + " ".join(f'"{item}"' for item in booklet_pages)
        # os.system(cmd)
        command = [ self.gs_binary, "-q", "-sDEVICE=pdfwrite", "-dNOPAUSE",
                "-dBATCH","-dSAFER", f"-sOutputFile={target_booklet}" ] + booklet_pages
        # subprocess.Popen(command).wait()
        self.process_call(command)
        ccc = f"{target_booklet} processed!"
        self.export_format_complete.emit(emit_msg)
        return ccc

    def execute_task_zip(self):
        ''' ZIP executor '''

        if self.cancel:
            idformat = "zip"
            raise CitraManikCancelException(idformat, "Zipping all files")
        # do find exported formats with pattern
        OUTDIR = f"{self.outputdir}{os.sep}ZIP"
        for item in self.ids_to_process:
            zf = zipfile.ZipFile(f"{OUTDIR}{os.sep}{item}.zip", "w", zipfile.ZIP_DEFLATED)
            for root,dirs,files in os.walk(self.outputdir):
                for f in files:
                    if item == f.split(".")[0] and not ".zip" in f:
                        zf.write(os.path.join(root, f), f)
            zf.close()
        self.export_format_complete.emit(OUTDIR)

    def stop(self):
        ''' Stop this export processes '''

        self.cancel = True
        self.quit()

    def run(self):
        ''' Run the thread '''

        self.cancel = False
        self.id_not_processed = []

        self.time_counter.start()

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            # handle bitmap executor (png, jpg, webp)
            if self.use_bitmapPNG:
                png_processes = {executor.submit(self.execute_task_png, item): item for item in self.ids_to_process}
                for ea in concurrent.futures.as_completed(png_processes):
                    hasil = png_processes[ea]
                    try:
                        data = ea.result()
                    except Exception as exc:
                        if self.with_png:
                            self.id_not_processed.append((png_processes[ea], "png"))
                        if self.with_jpg:
                            self.id_not_processed.append((png_processes[ea], "jpg"))
                        if self.with_webp:
                            self.id_not_processed.append((png_processes[ea], "webp"))
                        print('%r generated an exception: %s' % (hasil, exc))
                    else:
                        print('%r process is %s' % (hasil, data))

            if self.with_pdf or self.with_booklet or self.eps_useCMYK:
                pdf_processes = {executor.submit(self.execute_task_pdf, item): item for item in self.ids_to_process}
                for ea in concurrent.futures.as_completed(pdf_processes):
                    hasil = pdf_processes[ea]
                    try:
                        data = ea.result()
                    except Exception as exc:
                        if self.with_pdf:
                            self.id_not_processed.append((pdf_processes[ea], "pdf"))
                        print('%r generated an exception: %s' % (hasil, exc))
                    else:
                        print('%r process is %s' % (hasil, data))

            if self.with_eps and not self.eps_useCMYK:
                eps_processes = {executor.submit(self.execute_task_eps, item): item for item in self.ids_to_process}
                for ea in concurrent.futures.as_completed(eps_processes):
                    hasil = eps_processes[ea]
                    try:
                        data = ea.result()
                    except Exception as exc:
                        self.id_not_processed.append((eps_processes[ea], "eps"))
                        print('%r generated an exception: %s' % (hasil, exc))
                    else:
                        print('%r process is %s' % (hasil, data))

            if self.with_svg:
                svg_processes = {executor.submit(self.execute_task_svg, item): item for item in self.ids_to_process}
                for ea in concurrent.futures.as_completed(svg_processes):
                    hasil = svg_processes[ea]
                    try:
                        data = ea.result()
                    except Exception as exc:
                        self.id_not_processed.append((svg_processes[ea], "svg"))
                        print('%r generated an exception: %s' % (hasil, exc))
                    else:
                        print('%r process is %s' % (hasil, data))

        # see what id and format not performed well, then we could re-add this to queue later
        print("Failed task to finish: ",self.id_not_processed)
        # Do Booklet
        try:
            if self.with_booklet:
                self.execute_task_booklet()
        except:
            print(traceback.format_exc())
            self.id_not_processed.append(("Booklets","pdf booklet"))
        # Do zip
        try:
            if self.with_zip:
                print("Zipping files ...")
                self.execute_task_zip()
        except:
            self.id_not_processed.append(("Zipfiles", "zip"))
        self.export_finished.emit(self.id_not_processed, self.time_counter.get_elapsed_time())
        print(f"----------\nFailed: {len(self.id_not_processed)} ")
