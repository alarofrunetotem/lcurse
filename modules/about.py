from PyQt5 import Qt
from modules import defines
from PyQt5.Qt import QSettings
from _ctypes import alignment
VERSION="2.1"

class AboutDlg(Qt.QDialog):
    def __init__(self, parent):
        super(AboutDlg, self).__init__(parent)
        settings = Qt.QSettings()
        print(settings.applicationName(),settings.organizationName())
        print("Groups",settings.childGroups())
        for key in settings.allKeys():
            print("KEY: {}:{}".format(key,settings.value(key)))

        prefix=settings.value(defines.WOW_VERSION_KEY)
        print("prefix",prefix)
        prefix=settings.value("version")
        print("prefix",prefix)
        settings.beginGroup(prefix)
        box = Qt.QVBoxLayout(self)
        box.addWidget(Qt.QLabel("Lcurse version: {}".format(VERSION), self))
        settings=Qt.QSettings()
        box.addWidget(Qt.QLabel("Wow version: {}".format(prefix), self))
        settings.beginGroup(prefix)
        box.addWidget(Qt.QLabel("Wow path: {}".format(settings.value(defines.WOW_FOLDER_KEY)), self))
        box.addWidget(Qt.QLabel("Wow toc: {}".format(settings.value(defines.WOW_TOC_KEY)), self))
        settings.endGroup()
        btnBox = Qt.QDialogButtonBox(Qt.QDialogButtonBox.Ok)
        btnBox.accepted.connect(self.close)
        box.addWidget(btnBox)
        self.show()
