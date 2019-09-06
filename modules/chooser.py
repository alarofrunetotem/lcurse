from PyQt5 import Qt
from modules import defines
from modules import application

class ChooserDlg(Qt.QDialog):
    def __init__(self, parent):
        self.settings=Qt.QSettings()
        self.current=self.settings.value(defines.WOW_VERSION_KEY)
        super(ChooserDlg, self).__init__(parent)
        box = Qt.QVBoxLayout(self)
        box.addWidget(Qt.QLabel(self.tr("Select your WoW Version"), self))
        self.buttons=[]
        for v in self.settings.childGroups():
            button=Qt.QRadioButton(v)
            button.setChecked(1 if v == self.current else 0)
            box.addWidget(button)
            self.buttons.append(button)
        btnBox = Qt.QDialogButtonBox(Qt.QDialogButtonBox.Ok | Qt.QDialogButtonBox.Cancel)
        btnBox.accepted.connect(self.accept)
        btnBox.rejected.connect(self.reject)
        box.addWidget(btnBox)
        self.show()


    def accept(self):
        for button in self.buttons:
            if button.isChecked():
                print(button.text())
                self.settings.setValue(defines.WOW_VERSION_KEY,button.text())
        super(ChooserDlg, self).accept()


    def reject(self):
        super(ChooserDlg, self).reject()
