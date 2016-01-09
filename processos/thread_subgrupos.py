#!/usr/bin/env python
# encoding: utf-8
__author__ = 'ronald'

from PyQt4.QtCore import *
from PyQt4.QtSql import *

from utils.funcoes_utilitarias import *


class thread_subgrupos(QThread):
    update_info = pyqtSignal(str)
    update_pbar_max = pyqtSignal(int)
    update_pbar_value = pyqtSignal(int)
    update_alerta = pyqtSignal(str, str, str)
    update_regatual = pyqtSignal(str)
    update_regtotal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(thread_subgrupos, self).__init__(parent)

    def run(self):
        try:
            self.update_info.emit("Processando SubGrupos...")

            query = QSqlQuery()
            if not query.exec_(
                    "select distinct ite.dep, sgrp.cod, sgrp.des from ite right join mar as sgrp on sgrp.cod = ite.mar"):
                print("Nao executou o script")
                print(u"Erro: {0}".format(query.lastError().text()))
                self.update_alerta.emit('c', u'Atenção', u'Causa do erro: {0}\nquery que deu erro: {1}'
                                        .format(query.lastError().text(), query.lastQuery()))
                self.terminate()
            else:
                query.previous()
                pasta = QDir("arquivos")
                arq_grupo = QFile(pasta.path() + "/SYSPSBG.txt")
                if not pasta.exists(pasta.path()):
                    pasta.mkpath(pasta.path())
                if arq_grupo.exists():
                    arq_grupo.remove()

                arq_grupo.open(QFile.WriteOnly)

                self.update_pbar_max.emit(query.size())
                self.update_regtotal.emit("/ {0}".format(query.size()))

                cont = 0
                while query.next():
                    cont += 1
                    self.update_regatual.emit(str(cont))

                    codsecao = 99
                    grupo = query.value(0).toInt()[0]
                    codigo = query.value(1).toInt()[0]
                    descricao = remove_caracteres(str(QString.toUtf8(query.value(2).toString())))[1]

                    linha = "{0:02d}{1:03d}{2:03d}{3:30.30s}\n".format(
                        codsecao, grupo, codigo, descricao
                    )

                    arq_grupo.writeData(linha)
                    arq_grupo.flush()

                    self.update_pbar_value.emit(cont)

                arq_grupo.close()
                self.update_info.emit("Processo dos SubGrupos Finalizado!")
                self.update_alerta.emit("i", u"Informação", "Processo dos <strong>SubGrupos</strong> Finalizado!")
                self.sleep(3)
        except Exception as e:
            print("Erro: {0}".format(e))
            print("Ulimo codigo: {0}".format(codigo))
            self.update_alerta.emit("c", u"Critical Erro", u"ultimo codigo: {3}\nCausa do erro: {0}\n"
                                                           u"StackTrace: {1}\nQuery: {2}"
                                    .format(query.lastError().text(), e, query.lastQuery(), codigo))
            self.terminate()
