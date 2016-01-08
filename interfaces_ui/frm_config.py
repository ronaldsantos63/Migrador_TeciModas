#!/usr/bin/env python
#encoding: utf-8
__author__ = 'ronald'

from PyQt4 import QtCore, QtGui

from widgets.LineEdit_BtLocate import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_frm_config(object):
    def setupUi(self, frm_config=QtGui.QDialog):
        frm_config.setObjectName(_fromUtf8("frm_config"))
        frm_config.resize(484, 212)
        self.verticalLayout = QtGui.QVBoxLayout(frm_config)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(frm_config)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.widget = QtGui.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 30, 451, 71))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.lbl_banco = QtGui.QLabel(self.widget)
        self.lbl_banco.setObjectName(_fromUtf8("lbl_banco"))
        self.gridLayout.addWidget(self.lbl_banco, 0, 0, 1, 1)

        self.txt_banco = LineEdit_BtLocate(self.widget, filtro="Banco Access(*.mdb;*.accdb)")
        self.txt_banco.setObjectName(_fromUtf8("txt_banco"))
        self.gridLayout.addWidget(self.txt_banco, 0, 1, 1, 1)

        self.verticalLayout.addWidget(self.groupBox)

        self.quadro_botoes = QtGui.QFrame(frm_config)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quadro_botoes.sizePolicy().hasHeightForWidth())
        self.quadro_botoes.setSizePolicy(sizePolicy)
        self.quadro_botoes.setMaximumSize(QtCore.QSize(16777215, 50))
        self.quadro_botoes.setFrameShape(QtGui.QFrame.Panel)
        self.quadro_botoes.setFrameShadow(QtGui.QFrame.Plain)
        self.quadro_botoes.setObjectName(_fromUtf8("quadro_botoes"))

        self.widget1 = QtGui.QWidget(self.quadro_botoes)
        self.widget1.setGeometry(QtCore.QRect(210, 20, 239, 25))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.bt_testar = QtGui.QPushButton(self.widget1)
        self.bt_testar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_testar.setObjectName(_fromUtf8("bt_testar"))
        self.horizontalLayout.addWidget(self.bt_testar)

        self.bt_salvar = QtGui.QPushButton(self.widget1)
        self.bt_salvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_salvar.setObjectName(_fromUtf8("bt_salvar"))
        self.horizontalLayout.addWidget(self.bt_salvar)

        self.bt_sair = QtGui.QPushButton(self.widget1)
        self.bt_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_sair.setObjectName(_fromUtf8("bt_sair"))
        self.horizontalLayout.addWidget(self.bt_sair)

        self.verticalLayout.addWidget(self.quadro_botoes)

        self.retranslateUi(frm_config)
        QtCore.QObject.connect(self.bt_sair, QtCore.SIGNAL(_fromUtf8("clicked()")), frm_config.close)
        QtCore.QMetaObject.connectSlotsByName(frm_config)

    def retranslateUi(self, frm_config):
        frm_config.setWindowTitle(_translate("frm_config", "Configurar banco de dados", None))
        self.groupBox.setTitle(_translate("frm_config", "Selecione a pasta onde se encotram os DBF's", None))
        self.lbl_banco.setText(_translate("frm_config", "Banco: ", None))
        self.bt_sair.setText(_translate("frm_config", "Sair", None))
        self.bt_testar.setText(_translate("frm_config", "Testar", None))
        self.bt_salvar.setText(_translate("frm_config", "Salvar", None))
