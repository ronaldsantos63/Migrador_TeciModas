#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime
from time import strptime
from PyQt4.QtCore import *
from PyQt4.QtSql import *


from utils.funcoes_utilitarias import *

class thread_produtos(QThread):
    update_info = pyqtSignal(str)
    update_pbar_max = pyqtSignal(int)
    update_pbar_value = pyqtSignal(int)
    update_alerta = pyqtSignal(str, str, str)
    update_regatual = pyqtSignal(str)
    update_regtotal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(thread_produtos, self).__init__(parent)

    def run(self):
        try:
            self.update_info.emit("Processando Produtos...")

            query = QSqlQuery()
            script_file = QFile("scripts/produtos.sql")
            script_file.open(QFile.ReadOnly)
            if not query.exec_(str(script_file.readAll())):
                print("Nao executou o script")
                print(u"Erro: {0}".format(query.lastError().text()))
                self.update_alerta.emit('c', u'Atenção', u'Causa do erro: {0}\nquery que deu erro: {1}'
                                        .format(query.lastError().text(), query.lastQuery()))
                self.terminate()
            else:
                query.previous()
                # ###############( Checando arquivos )###############################
                pasta = QDir("arquivos")
                arq_produtos = QFile(pasta.path() + "/SYSPPRO.txt")
                arq_secao = QFile(pasta.path() + "/SYSPSEC.txt")

                if not pasta.exists(pasta.path()):
                    pasta.mkpath(pasta.path())
                if arq_produtos.exists():
                    arq_produtos.remove()
                if arq_secao.exists():
                    arq_secao.remove()

                arq_produtos.open(QFile.WriteOnly)
                arq_secao.open(QFile.WriteOnly)
                # ###############( Fim da verificacao dos arquivos )####################

                self.update_pbar_max.emit(query.size())
                self.update_regtotal.emit("/ {0}".format(query.size()))

                cont = 0
                while query.next():
                    cont += 1
                    self.update_regatual.emit(str(cont))
                    tmp_desc = str(QString.toUtf8(query.value(1).toString()))
                    tmp_descrdz = str(QString.toUtf8(query.value(2).toString()))
                    print(tmp_desc)
                    print(tmp_descrdz)
                    codigo = query.value(0).toInt()[0]
                    descricao = remove_caracteres(tmp_desc)[1]
                    descricao_reduzida = remove_caracteres(tmp_descrdz)[1]
                    cod_sec = query.value(3).toInt()[0]
                    paga_comissao = query.value(4).toString()
                    tributacao = query.value(5).toString()
                    peso_variavel = query.value(6).toString()
                    cod_impressao = query.value(7).toInt()[0]
                    print("Codigo Impressao: {}".format(cod_impressao))
                    comissao1 = query.value(8).toDouble()[0]
                    comissao2 = query.value(9).toDouble()[0]
                    comissao3 = query.value(10).toDouble()[0]
                    desconto = query.value(11).toDouble()[0]
                    preco1 = query.value(12).toDouble()[0]
                    oferta1 = query.value(13).toDouble()[0]
                    dias_validade = query.value(14).toInt()[0]
                    preco_variavel = query.value(15).toString()
                    frente_loja = query.value(16).toString()
                    min_estoque = query.value(17).toDouble()[0]
                    max_estoque = query.value(18).toDouble()[0]
                    cod_forn = query.value(19).toInt()[0]
                    preco2 = query.value(20).toDouble()[0]
                    oferta2 = query.value(21).toDouble()[0]
                    preco3 = query.value(22).toDouble()[0]
                    oferta3 = query.value(23).toDouble()[0]
                    tabela_a = query.value(24).toString()
                    tipo_bonificacao = query.value(25).toString()
                    fator_bonificacao = query.value(26).toDouble()[0]
                    data_alteracao = query.value(27).toString()
                    qtd_etiquetas = query.value(28).toInt()[0]
                    und_venda = query.value(29).toString()
                    produto_alterado = query.value(30).toString()
                    custo = query.value(31).toDouble()[0]
                    controla_serie = query.value(32).toString()
                    controla_estoque = query.value(33).toString()
                    permite_desconto = query.value(34).toString()
                    especializacao = query.value(35).toString()
                    composicao = query.value(36).toString()
                    balanca = query.value(37).toString()
                    controla_validade = query.value(38).toString()
                    margem1 = query.value(39).toDouble()[0]
                    margem2 = query.value(40).toDouble()[0]
                    margem3 = query.value(41).toDouble()[0]
                    mix = query.value(42).toString()
                    'Ajustando data'
                    tmp = strptime(str(query.value(43).toString()), "%Y-%m-%d")
                    data_inclusao = datetime(*tmp[0:5]).strftime("%d%m%Y")
                    print(data_inclusao)
                    data_forlin = query.value(44).toString()
                    dta_ult_preco1 = query.value(45).toString()
                    dta_ult_preco2 = query.value(46).toString()
                    dta_ult_preco3 = query.value(47).toString()
                    descricao_variavel = query.value(48).toString()
                    endereco = query.value(49).toString()
                    qtd_preco2 = query.value(50).toDouble()[0]
                    qtd_preco3 = query.value(51).toDouble()[0]
                    cod_grupo = query.value(52).toString()
                    cod_subgrupo = query.value(53).toInt()[0]
                    itens_embalagem = query.value(54).toDouble()[0]
                    qtd_max_oferta = query.value(55).toDouble()[0]
                    peso_bruto = query.value(56).toDouble()[0]
                    peso_liquido = query.value(57).toDouble()[0]
                    und_ref = query.value(58).toString()
                    medida_ref = query.value(59).toDouble()[0]
                    cod_genero = query.value(60).toString()
                    complemento_descricao = query.value(61).toString()
                    reservado1 = query.value(62).toString()
                    und_compra = query.value(63).toString()
                    reservado2 = query.value(64).toInt()[0]
                    natureza = query.value(65).toInt()[0]
                    ncm = query.value(66).toString()
                    ncm_excecao = query.value(67).toString()

                    linha_produto = "{0:014d}{1:45.45s}{2:20.20s}{3:02d}{4}{5}{6}{7:02d}{8:5.2f}{9:5.2f}{10:5.2f}" \
                                    "{11:5.2f}{12:13.2f}{13:13.2f}{14:03d}{15}{16}{17:13.2f}{18:13.2f}{19:04d}" \
                                    "{20:13.2f}{21:13.2f}{22:13.2f}{23:13.2f}{24}{25}{26:13.2f}{27}{28}{29:3.3s}" \
                                    "{30}{31:13.2f}{32}{33}{34}{35}{36}{37}{38}{39:7.2f}{40:7.2f}{41:7.2f}" \
                                    "{42:1.1s}{43}{44:8.8s}{45:8.8s}{46:8.8s}{47:8.8s}{48}{49:20.20s}{50:9.2f}" \
                                    "{51:9.2f}{52:3.3s}{53:03d}{54:13.2f}{55:9.2f}{56:9.3f}{57:9.3f}{58:3.3s}" \
                                    "{59:13.2f}{60:3.3s}{61:35.35s}{62:20.20s}{63:3.3s}{64:03d}{65}{66:8.8s}" \
                                    "{67:2.2s}\n" \
                        .format(codigo, descricao, descricao_reduzida, cod_sec, paga_comissao, tributacao,
                                peso_variavel, cod_impressao, comissao1, comissao2, comissao3, desconto, preco1,
                                oferta1, dias_validade, preco_variavel, frente_loja, min_estoque, max_estoque,
                                cod_forn, preco2, oferta2, preco3, oferta3, tabela_a, tipo_bonificacao,
                                fator_bonificacao, data_alteracao, qtd_etiquetas, und_venda, produto_alterado,
                                custo, controla_serie, controla_estoque, permite_desconto, especializacao, composicao,
                                balanca, controla_validade, margem1, margem2, margem3, mix, data_inclusao,
                                data_forlin, dta_ult_preco1, dta_ult_preco2, dta_ult_preco3, descricao_variavel,
                                endereco, qtd_preco2, qtd_preco3, cod_grupo, cod_subgrupo, itens_embalagem,
                                qtd_max_oferta, peso_bruto, peso_liquido, und_ref, medida_ref, cod_genero,
                                complemento_descricao, reservado1, und_compra, reservado2, natureza, ncm, ncm_excecao)

                    arq_produtos.writeData(linha_produto)
                    arq_produtos.flush()

                    self.update_pbar_value.emit(cont)

                linha_secao = "{0:02d}{1:30.30s}\n".format(
                    99, "GERAL"
                )
                arq_secao.writeData(linha_secao)
                arq_secao.flush()
                arq_secao.close()

                arq_produtos.close()
                self.update_info.emit("Processo dos Produtos Finalizado!")
                self.update_alerta.emit("i", u"Informação", "Processo dos <strong>Produtos</strong> Finalizado!")
                self.sleep(3)
        except Exception as e:
            print("Erro: {0}".format(e))
            print("Ulimo codigo: {0}".format(codigo))
            self.update_alerta.emit("c", u"Critical Erro",  u"ultimo codigo: {3}\nCausa do erro: {0}\n"
                                                            u"StackTrace: {1}\nQuery: {2}"
                                    .format(query.lastError().text(), e, query.lastQuery(), codigo))
            self.terminate()