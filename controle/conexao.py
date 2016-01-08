#!/usr/bin/env python
#encoding: utf-8
__author__ = 'ronald'

from PyQt4.QtSql import *
from PyQt4.QtCore import *


class conexao(QObject):
    def __init__(self, parent=None):
        self.database = None


    def conectar(self, db=None):
        if self.database is None:
            print("Entrou no if principal")
            conf = QSettings("Migrador_TeciModas", "connection")
            tmp_db = conf.value("db", '', type=str)
            print "Banco: ".format(str(tmp_db))
            if db is None and tmp_db == '':
                print("Caiu no primeiro if")
                return [False, "Por favor configurar banco de dados primeiro"]
            elif db is not None:
                print("Entrou no elif DB")
                str_conn = "Driver={driver};Dbq={banco};".format(driver="{Microsoft Access Driver (*.mdb, *.accdb)}",
                                                                 banco=db)
                print(u"String de conexao: {0}".format(str_conn))
                self.database = QSqlDatabase.addDatabase("QODBC")
                self.database.setDatabaseName(str_conn)
            else:
                print("Caiu no else do ")
                str_conn = "Driver={driver};Dbq={banco};".format(driver="{Microsoft Access Driver (*.mdb, *.accdb)}",
                                                                 banco=tmp_db)
                print(u"String de conexao: {0}".format(str_conn))
                self.database = QSqlDatabase.addDatabase("QODBC")
                self.database.setDatabaseName(str_conn)
        else:
            print("Caiu no else principal")
        if not self.database.open():
            return [False, u"Erro ao conectar ao banco de dados!\nErro: {0}".format(self.database.lastError().text())]
        else:
            print("Conectado com sucesso!")
            return [True, "Conectado com sucesso!"]


    def desconectar(self):
        self.database.removeDatabase("QODBC")
        self.database = None