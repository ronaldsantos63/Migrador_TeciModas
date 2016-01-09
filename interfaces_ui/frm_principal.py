# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\frm_principal.ui'
#
# Created: Fri Jan 08 22:50:41 2016
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_frm_principal(object):
    def setupUi(self, frm_principal):
        frm_principal.setObjectName(_fromUtf8("frm_principal"))
        frm_principal.resize(484, 212)
        self.verticalLayout = QtGui.QVBoxLayout(frm_principal)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(frm_principal)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 451, 71))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.check_produtos = QtGui.QCheckBox(self.layoutWidget)
        self.check_produtos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_produtos.setObjectName(_fromUtf8("check_produtos"))
        self.gridLayout.addWidget(self.check_produtos, 0, 0, 1, 1)
        self.check_grupos = QtGui.QCheckBox(self.layoutWidget)
        self.check_grupos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_grupos.setObjectName(_fromUtf8("check_grupos"))
        self.gridLayout.addWidget(self.check_grupos, 0, 1, 1, 1)
        self.check_marcar_todos = QtGui.QCheckBox(self.layoutWidget)
        self.check_marcar_todos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_marcar_todos.setObjectName(_fromUtf8("check_marcar_todos"))
        self.gridLayout.addWidget(self.check_marcar_todos, 1, 3, 1, 1)
        self.check_subgrupos = QtGui.QCheckBox(self.layoutWidget)
        self.check_subgrupos.setObjectName(_fromUtf8("check_subgrupos"))
        self.gridLayout.addWidget(self.check_subgrupos, 0, 2, 1, 1)
        self.check_fornecedor = QtGui.QCheckBox(self.layoutWidget)
        self.check_fornecedor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_fornecedor.setObjectName(_fromUtf8("check_fornecedor"))
        self.gridLayout.addWidget(self.check_fornecedor, 0, 3, 1, 1)
        self.check_cliente = QtGui.QCheckBox(self.layoutWidget)
        self.check_cliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_cliente.setObjectName(_fromUtf8("check_cliente"))
        self.gridLayout.addWidget(self.check_cliente, 1, 0, 1, 1)
        self.check_conta_receber = QtGui.QCheckBox(self.layoutWidget)
        self.check_conta_receber.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_conta_receber.setObjectName(_fromUtf8("check_conta_receber"))
        self.gridLayout.addWidget(self.check_conta_receber, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.lbl_info = QtGui.QLabel(frm_principal)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_info.sizePolicy().hasHeightForWidth())
        self.lbl_info.setSizePolicy(sizePolicy)
        self.lbl_info.setText(_fromUtf8(""))
        self.lbl_info.setObjectName(_fromUtf8("lbl_info"))
        self.verticalLayout.addWidget(self.lbl_info)
        self.quadro_botoes = QtGui.QFrame(frm_principal)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quadro_botoes.sizePolicy().hasHeightForWidth())
        self.quadro_botoes.setSizePolicy(sizePolicy)
        self.quadro_botoes.setMaximumSize(QtCore.QSize(16777215, 50))
        self.quadro_botoes.setFrameShape(QtGui.QFrame.Panel)
        self.quadro_botoes.setFrameShadow(QtGui.QFrame.Plain)
        self.quadro_botoes.setObjectName(_fromUtf8("quadro_botoes"))
        self.pbar = QtGui.QProgressBar(self.quadro_botoes)
        self.pbar.setGeometry(QtCore.QRect(10, 30, 191, 16))
        self.pbar.setProperty("value", 24)
        self.pbar.setTextVisible(True)
        self.pbar.setInvertedAppearance(False)
        self.pbar.setObjectName(_fromUtf8("pbar"))
        self.lbl_reg_atual = QtGui.QLabel(self.quadro_botoes)
        self.lbl_reg_atual.setGeometry(QtCore.QRect(0, 10, 91, 16))
        self.lbl_reg_atual.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_reg_atual.setObjectName(_fromUtf8("lbl_reg_atual"))
        self.lbl_reg_total = QtGui.QLabel(self.quadro_botoes)
        self.lbl_reg_total.setGeometry(QtCore.QRect(100, 10, 81, 16))
        self.lbl_reg_total.setObjectName(_fromUtf8("lbl_reg_total"))
        self.layoutWidget1 = QtGui.QWidget(self.quadro_botoes)
        self.layoutWidget1.setGeometry(QtCore.QRect(210, 20, 239, 25))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_processar = QtGui.QPushButton(self.layoutWidget1)
        self.btn_processar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_processar.setObjectName(_fromUtf8("btn_processar"))
        self.horizontalLayout.addWidget(self.btn_processar)
        self.btn_config = QtGui.QPushButton(self.layoutWidget1)
        self.btn_config.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_config.setObjectName(_fromUtf8("btn_config"))
        self.horizontalLayout.addWidget(self.btn_config)
        self.btn_sair = QtGui.QPushButton(self.layoutWidget1)
        self.btn_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_sair.setObjectName(_fromUtf8("btn_sair"))
        self.horizontalLayout.addWidget(self.btn_sair)
        self.verticalLayout.addWidget(self.quadro_botoes)

        self.retranslateUi(frm_principal)
        QtCore.QObject.connect(self.check_marcar_todos, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.check_produtos.setChecked)
        QtCore.QObject.connect(self.check_marcar_todos, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.check_grupos.setChecked)
        QtCore.QObject.connect(self.check_marcar_todos, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.check_fornecedor.setChecked)
        QtCore.QObject.connect(self.check_marcar_todos, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.check_cliente.setChecked)
        QtCore.QObject.connect(self.check_marcar_todos, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.check_conta_receber.setChecked)
        QtCore.QObject.connect(self.btn_sair, QtCore.SIGNAL(_fromUtf8("clicked()")), frm_principal.close)
        QtCore.QMetaObject.connectSlotsByName(frm_principal)

    def retranslateUi(self, frm_principal):
        frm_principal.setWindowTitle(_translate("frm_principal", "Orionline Automação Comercial Ltda", None))
        self.groupBox.setTitle(_translate("frm_principal", "Marque as opções que deseja Migrar", None))
        self.check_produtos.setText(_translate("frm_principal", "Produtos", None))
        self.check_grupos.setText(_translate("frm_principal", "Grupos", None))
        self.check_marcar_todos.setText(_translate("frm_principal", "Marcar Todos", None))
        self.check_subgrupos.setText(_translate("frm_principal", "Subgrupos", None))
        self.check_fornecedor.setText(_translate("frm_principal", "Fornecedor", None))
        self.check_cliente.setText(_translate("frm_principal", "Cliente", None))
        self.check_conta_receber.setText(_translate("frm_principal", "Contas Receber", None))
        self.lbl_reg_atual.setText(_translate("frm_principal", "0", None))
        self.lbl_reg_total.setText(_translate("frm_principal", "/ 0", None))
        self.btn_processar.setText(_translate("frm_principal", "Processar", None))
        self.btn_config.setText(_translate("frm_principal", "Config", None))
        self.btn_sair.setText(_translate("frm_principal", "Sair", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frm_principal = QtGui.QDialog()
    ui = Ui_frm_principal()
    ui.setupUi(frm_principal)
    frm_principal.show()
    sys.exit(app.exec_())

