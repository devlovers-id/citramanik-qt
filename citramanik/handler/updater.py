import sys
import json

from PyQt6 import QtCore, QtWidgets, QtNetwork
from citramanik import __download_url__

class CitramanikUpdater(QtCore.QObject):

    latest_version = None
    latest_version_date = None

    __url = f"{__download_url__}/releases/info"
    __download_url = f"{__download_url__}/releases"

    def __init__(self, parent=None, *args, **kwargs):
        QtCore.QObject.__init__(self, parent=parent, *args, **kwargs)
        self.parent = parent

    def processRes(self, reply):
        if reply.error():
            banner_text = f"Unable to fetch update - {reply.error()}"
            self.parent.banner_update.setText(banner_text)
            self.parent.banner_update.show()
            return
        if reply.bytesAvailable():
            result = json.loads(bytes(reply.readAll()).decode('utf-8'))
            self.latest_version = result.get('latest_version')
            self.latest_version_date = result.get('date').split(' ')[0]
            local_version = self.parent.local_version.split('.')
            local_version = ".".join(str(x) for x in local_version[:3])
            if (self.should_show_notif(local_version)):
                banner_text = f"<html><head/><body><p><a href=\"{self.__download_url}/{self.latest_version}\"><span style=\" text-decoration: none; color:#fff;\">New Version {self.latest_version} is available!</span></a></p></body></html>"
                self.parent.banner_update.setText(banner_text)
                self.parent.banner_update.show()

    def retrieve_latest_version(self):
        ''' return latest version from server '''
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(self.__url))
        self.__qnam = QtNetwork.QNetworkAccessManager()
        self.__qnam.finished.connect(self.processRes)
        self.__qnam.get(req)

    def should_show_notif(self, local_version):
        if self.latest_version > local_version:
            return True
        return False
