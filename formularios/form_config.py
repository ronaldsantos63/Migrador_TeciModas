#!/usr/bin/env python
# encoding: utf-8

from PyQt4.QtGui import *

from controle.conexao import *
from interfaces_ui.frm_config import *


class form_conf(QDialog, Ui_frm_config):
    def __init__(self, parent, conn):
        super(form_conf, self).__init__(parent)
        self.setupUi(self)
        self.conn = conn

        self.bt_testar.clicked.connect(self.testar)
        self.bt_salvar.clicked.connect(self.salvar)

        self.on_form_load()
        self.pai = parent

    def on_form_load(self):
        conf = QSettings('Migrador_TeciModas', 'connection')
        self.txt_banco.setText(conf.value('db', '', type=str))

    def salvar(self):
        conf = QSettings('Migrador_TeciModas', 'connection')
        pasta = QDir()
        if pasta.exists(self.txt_banco.text()):
            conf.setValue('db', self.txt_banco.text())
            QMessageBox.information(self, 'Info', "Salvo com sucesso!")
            QMessageBox.warning(self, "Alerta", u"A aplicação será fechada para validar as configurações!")
            self.pai.close()
        else:
            QMessageBox.warning(self, 'Aviso', u"Por favor selecione uma pasta válida")

    def testar(self):
        # print("Camiho: {0}".format(self.txt_banco.text()))
        result = self.conn.conectar(db=self.txt_banco.text())
        if result[0]:
            QMessageBox.information(self, u"Informação", 'Conectado com sucesso!')
        else:
            QMessageBox.warning(self, u"Alerta", result[1])
            self.conn.desconectar()
