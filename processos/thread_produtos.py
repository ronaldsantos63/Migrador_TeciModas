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
            subquery = QSqlQuery()
            subquery2 = QSqlQuery()
            if not query.exec_("select * from ite"):
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
                arq_codbarra = QFile(pasta.path() + "/SYSPAUX.txt")

                if not pasta.exists(pasta.path()):
                    pasta.mkpath(pasta.path())
                if arq_produtos.exists():
                    arq_produtos.remove()
                if arq_secao.exists():
                    arq_secao.remove()
                if arq_codbarra.exists():
                    arq_codbarra.remove()

                arq_produtos.open(QFile.WriteOnly)
                arq_secao.open(QFile.WriteOnly)
                arq_codbarra.open(QFile.WriteOnly)
                # ###############( Fim da verificacao dos arquivos )####################

                subquery.exec_("select count(*) from ite")
                subquery.next()
                total_prod = subquery.value(0).toInt()[0]
                self.update_pbar_max.emit(total_prod)
                self.update_regtotal.emit("/ {0}".format(total_prod))

                cont = 0
                while query.next():
                    cont += 1
                    self.update_regatual.emit(str(cont))

                    codigo = query.value(0).toInt()[0]

                    tmp_desc = str(QString.toUtf8(query.value(19).toString()))
                    tmp_descrdz = tmp_desc

                    ##Executando subquery's para pegar as informacoes complementares
                    ####
                    ########( Pegando tributacao dos produtos )########
                    codTrb = query.value(13).toInt()[0]
                    if subquery.exec_("select siticm from trt where cod = {0}".format(codTrb)):
                        try:
                            print("Tem tributacao")
                            subquery.previous()
                            subquery.next()
                            tmp_sitTrb = subquery.value(0).toInt()[0]
                        except:
                            print("OPA acontaceu alguma coisa na tributacao")
                    else:
                        print("Ops Nao tem tributacao")
                        tmp_sitTrb = 0
                    ########( Pegando Precos de Venda, comissao, custo, estoque min e max etc... )########
                    if subquery2.exec_(
                            "select prccus as custo, prcven1 as preco1, prcven2 as preco2, prcven3 as preco3, "
                            "percom as comissao, perdesmax as desconto, dtaultreaven as dtultaltprc, "
                            "locfis as end_est, estmax, estmin from kdx"
                            " where lop = 1 and ite = {0}".format(codigo)):
                        try:
                            print("Tem preco!")
                            subquery2.previous()
                            subquery2.next()
                            tmp_custo = subquery2.value(0).toDouble()[0]
                            tmp_prc1 = subquery2.value(1).toDouble()[0]
                            tmp_prc2 = subquery2.value(2).toDouble()[0]
                            tmp_prc3 = subquery2.value(3).toDouble()[0]
                            tmp_comissao = subquery2.value(4).toDouble()[0]
                            tmp_descMax = subquery2.value(5).toDouble()[0]
                            tmp_ultaltprc1 = subquery2.value(6).toString()
                            tmp_end_est = subquery2.value(7).toString()
                            tmp_estmax = subquery2.value(8).toDouble()[0]
                            tmp_estmin = subquery2.value(9).toDouble()[0]
                        except:
                            print("OPA Aconteceu alguma coisa nos precos")
                    else:
                        print("Ops nao tem preco")
                        tmp_custo = 0.00
                        tmp_prc1 = 0.00
                        tmp_prc2 = 0.00
                        tmp_prc3 = 0.00
                        tmp_comissao = 0.00
                        tmp_descMax = 0.00
                        tmp_ultaltprc1 = datetime.now()
                        tmp_estmax = 0.00
                        tmp_estmin = 0.00
                    ##Fim da execucao das subquery's
                    print(tmp_desc)
                    print(remove_caracteres(tmp_desc)[1])
                    descricao = remove_caracteres(tmp_desc)[1]
                    descricao_reduzida = descricao
                    cod_sec = 99
                    if tmp_comissao > 0:
                        paga_comissao = 'S'
                    else:
                        paga_comissao = "N"

                    # Logica para pegar a tributacao correta dos produtos
                    if tmp_sitTrb == 1:
                        tributacao = "T17"
                    elif tmp_sitTrb == 2:
                        tributacao = "I00"
                    else:
                        tributacao = "T17"
                    # Fim da Logica para pegar a tributacao correta dos produtos

                    peso_variavel = "S"
                    cod_impressao = 00
                    comissao1 = tmp_comissao
                    comissao2 = 0.00
                    comissao3 = 0.00
                    desconto = tmp_descMax
                    preco1 = tmp_prc1
                    oferta1 = 0.00
                    dias_validade = 0
                    preco_variavel = "N"
                    frente_loja = "N"
                    min_estoque = tmp_estmin
                    max_estoque = tmp_estmax
                    cod_forn = 0
                    preco2 = tmp_prc2
                    oferta2 = 0.00
                    preco3 = tmp_prc3
                    oferta3 = 0.00
                    tabela_a = "0"
                    tipo_bonificacao = "P"
                    fator_bonificacao = 0.00
                    try:
                        if not isinstance(tmp_ultaltprc1, datetime):
                            tmp = strptime(str(tmp_ultaltprc1)[0:10], "%Y-%m-%d")
                            data_alteracao = datetime(*tmp[0:5]).strftime("%Y%m%d")
                        else:
                            data_alteracao = tmp_ultaltprc1.strftime("%Y%m%d")
                    except:
                        data_alteracao = datetime.now().strftime("%Y%m%d")
                    qtd_etiquetas = 1
                    und_venda = remove_caracteres(QString.toUtf8(query.value(9).toString()))[1]
                    produto_alterado = "A"
                    custo = tmp_custo
                    controla_serie = "N"
                    controla_estoque = "S"
                    permite_desconto = "S"
                    especializacao = "O"
                    composicao = "N"
                    balanca = "N"
                    controla_validade = "N"
                    margem1 = 0.00
                    margem2 = 0.00
                    margem3 = 0.00
                    mix = ""
                    'Ajustando data'
                    try:
                        if not isinstance(tmp_ultaltprc1, datetime):
                            # print("Entrou no if")
                            # print("E data a ser tratada e: {0}".format(tmp_ultaltprc1))
                            tmp = strptime(str(tmp_ultaltprc1)[0:10], "%Y-%m-%d")
                            # print("Agora a data esta assim: {}".format(tmp))
                            data_inclusao = datetime(*tmp[0:5]).strftime("%d%m%Y")
                            tmp_ultaltprc1 = data_inclusao
                        else:
                            # print("Entrou no else")
                            data_inclusao = tmp_ultaltprc1.strftime("%d%m%Y")
                            tmp_ultaltprc1 = data_inclusao
                    except Exception as ex:
                        # print("Caiu na excecao")
                        # print("O erro foi: ".format(str(ex)))
                        data_inclusao = datetime.now().strftime("%d%m%Y")
                        tmp_ultaltprc1 = data_inclusao
                    print("A data e: {0}".format(data_inclusao))
                    # raw_input("Parou boi")
                    data_forlin = ""
                    dta_ult_preco1 = data_inclusao
                    dta_ult_preco2 = ""
                    dta_ult_preco3 = ""
                    descricao_variavel = "N"
                    endereco = tmp_end_est
                    qtd_preco2 = 0.00
                    qtd_preco3 = 0.00
                    cod_grupo = query.value(1).toInt()[0]
                    cod_subgrupo = query.value(3).toInt()[0]
                    itens_embalagem = 1.0
                    qtd_max_oferta = 0.00
                    peso_bruto = 0.00
                    peso_liquido = 0.00
                    und_ref = "UN"
                    medida_ref = 1.00
                    cod_genero = ""
                    complemento_descricao = ""
                    reservado1 = ""
                    und_compra = und_venda
                    reservado2 = 0
                    natureza = 999
                    ncm = ""
                    ncm_excecao = ""

                    linha_produto = "{0:014d}{1:45.45s}{2:20.20s}{3:02d}{4}{5}{6}{7:02d}{8:5.2f}{9:5.2f}{10:5.2f}" \
                                    "{11:5.2f}{12:13.2f}{13:13.2f}{14:03d}{15}{16}{17:13.2f}{18:13.2f}{19:04d}" \
                                    "{20:13.2f}{21:13.2f}{22:13.2f}{23:13.2f}{24}{25}{26:13.2f}{27}{28}{29:3.3s}" \
                                    "{30}{31:13.2f}{32}{33}{34}{35}{36}{37}{38}{39:7.2f}{40:7.2f}{41:7.2f}" \
                                    "{42:1.1s}{43}{44:8.8s}{45:8.8s}{46:8.8s}{47:8.8s}{48}{49:20.20s}{50:9.2f}" \
                                    "{51:9.2f}{52:03d}{53:03d}{54:13.2f}{55:9.2f}{56:9.3f}{57:9.3f}{58:3.3s}" \
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
            print("Ulimo codigo: {0}".format(codigo))
            print("Erro: {0}".format(e))
            self.update_alerta.emit("c", u"Critical Erro", u"ultimo codigo: {3}\nCausa do erro: {0}\n"
                                                           u"StackTrace: {1}\nQuery: {2}"
                                    .format(query.lastError().text(), e, query.lastQuery(), codigo))
            self.terminate()
