# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 07:44:23 2018
programa para o EP
@author: vitoria
"""
estoque = {}
print('Controle de estoque')
print('0 - sair')
print('1 - adicionar item')
print('2 - remover item')
print('3 - alterar item')
print('4 - Imprimir estoque')
x = int(input('Faça sua escolha: '))

if x == 0:
    print('Até mais')
if x == 1:
    produto = input('Nome do produto: ')
    if produto in estoque:
        print('Produto ja está cadastrado.')
    quant = float(input('Quantidade inicial: '))
    if quant < 0:
        print('Quantidade inicial nao pode ser negativa.')
        float(input('Quantidade inicial: '))
    estoque[produto]=[quant]
x = int(input('Faça sua escolha: '))
if x == 2:
     delpro = input('Nome do produto: ')
     if delpro in estoque:
        del estoque[delpro]
     else:
        print('Elemento não encontrado')
x = int(input('Faça sua escolha: '))
if x == 3:
     produto = input('Nome do produto: ')
     quant2 = float(input('Quantidade: '))
     estoque[produto] = quant2+quant
     print('Novo estoque de {0}:{1}'.format(produto, quant))