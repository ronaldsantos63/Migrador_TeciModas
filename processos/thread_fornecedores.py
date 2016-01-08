#!/usr/bin/env python
# encoding: utf-8
__author__ = 'RONALD'

from PyQt4.QtCore import *
from PyQt4.QtSql import *

from utils.funcoes_utilitarias import *

class thread_fornecedores(QThread):
    update_info = pyqtSignal(str)
    update_pbar_max = pyqtSignal(int)
    update_pbar_value = pyqtSignal(int)
    update_alerta = pyqtSignal(str, str, str)
    update_regatual = pyqtSignal(str)
    update_regtotal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(thread_fornecedores, self).__init__(parent)

    def run(self):
        try:
            self.update_info.emit("Processando Produtos...")
        except Exception as e:
            pass