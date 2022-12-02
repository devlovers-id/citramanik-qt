from PyQt6.QtWidgets import QDialog, QMessageBox, QScrollArea, QGridLayout, QLabel
from PyQt6.QtCore import pyqtSignal
from random import choice

from citramanik.ui.Ui_ProgressDialog import Ui_CitramanikProgressBar


def show_message(msg_type=QMessageBox.information, msg="Info", scrollable=False):
    if scrollable:
        box = ScrollableMessageBox(msg_type, "Report", msg)
    else:
        box = QMessageBox(msg_type, "Citramanik Notification", msg)
    box.exec_()


class ScrollableMessageBox(QMessageBox):
    def __init__(self, *args, **kwargs):
        QMessageBox.__init__(self, *args, **kwargs)
        childn = self.children()
        scrollarea = QScrollArea(self)
        scrollarea.setWidgetResizable(True)
        grd = self.findChild(QGridLayout)
        lbl = QLabel(childn[1].text(), self)
        lbl.setWordWrap(True)
        scrollarea.setWidget(lbl)
        scrollarea.setMinimumSize(400,200)
        grd.addWidget(scrollarea,0,1)
        childn[1].setText('')


class ProgressDialog(QDialog, Ui_CitramanikProgressBar):

    process_canceled = pyqtSignal()

    def __init__(self, parent=None):
        super(ProgressDialog, self).__init__(parent=parent)
        self.setupUi(self)

    def initialize_dialog(self, max_range=1):
        """ Init the progressbar to show information about exports progression.
        @param max_range :int -> Set the max progress value based on number of export ids.
        """

        random_message = [
            "Please enjoy your coffee...",
            "It won't take long...",
            "Maybe you want to change the playlist?",
            "Get some water to drink...",
            "Just relax...",
            "Take a break",
            "We got you",
            "Processing your images...",
            "Please wait..."
            ]
        self.max_range = max_range
        self.label_exporting.setText(choice(random_message))
        self.progress_bar.setRange(1, max_range)

        # set all component below centralwidget disabled when exporting
        self.parent().centralwidget.setEnabled(False)
        self.btn_cancel.setEnabled(True)

        # register events
        self.btn_cancel.clicked.connect(self.__handle_cancel_button)
        self.progress_bar.valueChanged.connect(self.__handle_value_changed)

    def update_export_progression(self, finished_job):
        ''' Handler for each finished job '''
        new_value = self.progress_bar.value() + 1
        self.label_currentfile.setText(finished_job)
        self.progress_bar.setValue(new_value)

    def __handle_cancel_button(self):
        ''' Cancel export handler '''
        self.process_canceled.emit()
        self.label_exporting.setText("Aborting exports...")
        self.label_currentfile.setText("Aborting export processes, please wait ...")
        self.btn_cancel.setEnabled(False)

    def __handle_value_changed(self):
        ''' Handler when value is changed via setValue. '''
        # keep watch the progress_bar value,
        # if 100%, close this dialog and re-enable the main window
        if self.progress_bar.value() >= self.max_range:
            self.close()
            self.parent().centralwidget.setEnabled(True)
