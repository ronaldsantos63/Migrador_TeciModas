#!/usr/bin/env python
# encoding: utf-8

import os

if __name__ == '__main__':
    from PyInstaller.__main__ import run

    opts = ['Migrador_TeciModas.py', '-w', '--icon=logo.ico', '-y', '--clean', '-F', '--uac-admin', '--uac-uiaccess']
    run(opts)

# from distutils.core import setup
#
# setup(
#     name='Migrador_Wintor',
#     version='1.0.0.0',
#     packages=['utils', 'gerador', 'imagens', 'Modelos', 'controle', 'interfaces', 'formularios'],
#     url='http:/www.orionline.com.br',
#     license='',
#     author='ronald',
#     author_email='ronaldsantos63@gmail.com',
#     description='Converte dados do banco Oracle do Sistema Winthor para o banco Firebird do Sistema SysPDV'
# )
