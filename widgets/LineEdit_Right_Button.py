from PyQt4.QtGui import *
from PyQt4.QtCore import *
from sys import argv, exit

class LineEdit(QLineEdit):
    def __init__(self,parent=None):
        QLineEdit.__init__(self,parent)

        self.bt_limpar = QToolButton(self)
        self.bt_limpar.setCursor(Qt.PointingHandCursor)

        self.bt_limpar.setFocusPolicy(Qt.NoFocus)
        #self.ButtonShowKeyboard.setIcon(QIcon("icons/myIcon.png"))
        icon = QIcon("imagens/icones/delete_16.png")
        self.bt_limpar.setIcon(icon)
        self.bt_limpar.setStyleSheet("background: transparent; border: none;")

        layout = QHBoxLayout(self)
        layout.addWidget(self.bt_limpar,0,Qt.AlignRight)

        layout.setSpacing(0)
        layout.setMargin(5)

        self.bt_limpar.setToolTip(QApplication.translate("None", "Limpar", None, QApplication.UnicodeUTF8))

        self.bt_limpar.clicked.connect(self.clear)