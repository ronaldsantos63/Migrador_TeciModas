#!/usr/bin/env python
#encoding: utf-8
from processos.thread_grupos import thread_grupos
from processos.thread_produtos import thread_produtos

__author__ = 'ronald'


from PyQt4.QtGui import *
from PyQt4.QtCore import *
from sys import argv, exit

from interfaces_ui.frm_principal import *
from formularios.form_config import *

from controle.conexao import *

class Migrador(QDialog, Ui_frm_principal):
    def __init__(self, parent=None):
        super(Migrador, self).__init__(parent)
        self.setupUi(self)

        self.btn_config.clicked.connect(self.show_conf)
        self.btn_processar.clicked.connect(self.processar)
        self.conn = conexao(self)

        result = self.conn.conectar()
        if not result[0]:
            QMessageBox.warning(self, 'Aviso', result[1])
            self.show_conf()

    def show_conf(self):
        form = form_conf(self, self.conn)
        form.show()

    def processar(self):
        result = self.conn.conectar()
        if not result[0]:
            erro = QMessageBox(self)
            erro.setWindowTitle("Error")
            erro.addButton("Ok", QMessageBox.AcceptRole)
            erro.setText(result[1])
            erro.setDetailedText(result[2])
            erro.setIcon(QMessageBox.Critical)
            erro.exec_()
        else:
            th_prod = thread_produtos(self)
            th_grp = thread_grupos(self)
            if self.check_produtos.isChecked():
                th_prod.update_pbar_max.connect(self.pbar.setMaximum)
                th_prod.update_pbar_value.connect(self.pbar.setValue)
                th_prod.update_info.connect(self.lbl_info.setText)
                th_prod.update_alerta.connect(self.alertas)
                th_prod.update_regatual.connect(self.lbl_reg_atual.setText)
                th_prod.update_regtotal.connect(self.lbl_reg_total.setText)
                if self.check_grupos.isChecked():
                    th_prod.finished.connect(th_grp.start)
                    th_prod.terminated.connect(th_grp.start)
                th_prod.start()
            if self.check_grupos.isChecked():
                th_grp.update_pbar_max.connect(self.pbar.setMaximum)
                th_grp.update_pbar_value.connect(self.pbar.setValue)
                th_grp.update_info.connect(self.lbl_info.setText)
                th_grp.update_alerta.connect(self.alertas)
                th_grp.update_regatual.connect(self.lbl_reg_atual.setText)
                th_grp.update_regtotal.connect(self.lbl_reg_total.setText)
                if not self.check_produtos.isChecked():
                    th_grp.start()


    def alertas(self, tipo='a', titulo="", msg=""):
        if tipo == 'a':
            QMessageBox.warning(self, titulo, msg)
        elif tipo == 'i':
            QMessageBox.information(self, titulo, msg)
        else:
            erro = QMessageBox(self)
            erro.setSizeGripEnabled(True)
            erro.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            erro.setFixedWidth(600)
            erro.setFixedHeight(400)
            erro.setWindowTitle(titulo)
            erro.setIcon(QMessageBox.Critical)
            erro.setText(u"Ocorreu um erro crítico!\nVerifique os detalhes do erro!")
            erro.addButton('Ok', QMessageBox.AcceptRole)
            erro.setDetailedText(msg)
            erro.exec_()


if __name__ == '__main__':
    app = QApplication(argv)
    form = Migrador()
    form.show()
    exit(app.exec_())