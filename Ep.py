# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 07:44:23 2018
programa para o EP
@author: vitoria
"""
<<<<<<< HEAD
=======

import json
from pprint import pprint
>>>>>>> 88b566224734c54dff65313626885caada03a597

estoque = {}

<<<<<<< HEAD


print('Controle de estoque')
print('0 - Sair')
print('1 - Adicionar item')
print('2 - Remover item')
print('3 - Alterar item')
print('4 - Imprimir estoque')
escolha = int(input('Faça sua escolha: '))

=======
>>>>>>> 88b566224734c54dff65313626885caada03a597

valendo = True

while valendo:
    
    print('Controle de estoque')
    print('0 - Sair')
    print('1 - Adicionar item')
    print('2 - Remover item')
    print('3 - Alterar item')
    print('4 - Imprimir estoque')
    escolha = int(input('Faça sua escolha: '))

    if escolha == 0:
       print('Até mais')
       valendo = False
    
    elif escolha == 1:
        produto = input('Nome do produto: ')
        
        if produto in estoque:
            print('Produto já cadastrado.')
        else:
            quant = float(input('Quantidade inicial: '))
<<<<<<< HEAD
            #precisa adicionar o produto no estoque
=======
>>>>>>> 6f88a908f1fc9559cac8cd79bd267032b709e7c6
            if quant < 0:
                print('Quantidade inicial não pode ser negativa.')
                quant = float(input('Quantidade inicial: '))
                if quant > 0:
                    estoque[produto]=quant
                else:
                    print('Quantidade inicial inválida.')
            elif quant > 0:
                estoque[produto]=quant
            else:
                print('Quantidade inicial não pode ser nula.')
                quant = float(input('Quantidade inicial: '))
                if quant > 0:
                    estoque[produto]=quant
                else:
                    print('Quantidade inicial inválida.')
        print('')        
        print('Controle de estoque')
        print('0 - Sair')
        print('1 - Adicionar item')
        print('2 - Remover item')
        print('3 - Alterar item')
        print('4 - Imprimir estoque')
        escolha = int(input('Faça sua escolha: '))
        
        
    elif escolha == 2:
        delpro = input('Nome do produto: ')
        if delpro in estoque:
            del estoque[delpro]
        else:
            print('Elemento não encontrado')
            
        print('')    
        print('Controle de estoque')
        print('0 - Sair')
        print('1 - Adicionar item')
        print('2 - Remover item')
        print('3 - Alterar item')
        print('4 - Imprimir estoque')
        escolha = int(input('Faça sua escolha: '))
        
    elif escolha == 3:
        produto = input('Nome do produto: ')
        if produto in estoque:
            quant2 = float(input('Quantidade: '))
            estoque[produto] += quant2
            print('Novo estoque de {0}: {1}'.format(produto, estoque[produto]))
        else:
            print('Elemento não encontrado')
        
        print('')
        print('Controle de estoque')
        print('0 - Sair')
        print('1 - Adicionar item')
        print('2 - Remover item')
        print('3 - Alterar item')
        print('4 - Imprimir estoque')
        escolha = int(input('Faça sua escolha: '))
        
<<<<<<< HEAD
   elif escolha == 4:
        print('Estoque:{0}'.format(estoque))
=======
    elif escolha == 4:
        pprint('Estoque:{0}'.format(estoque))
>>>>>>> 88b566224734c54dff65313626885caada03a597
        
        print('')
        print('Controle de estoque')
        print('0 - Sair')
        print('1 - Adicionar item')
        print('2 - Remover item')
        print('3 - Alterar item')
        print('4 - Imprimir estoque')
        escolha = int(input('Faça sua escolha: '))
        
    else: 
       print ('Comando Inválido') 
      
<<<<<<< HEAD
      print('')
      print('Controle de estoque')
      print('0 - Sair')
      print('1 - Adicionar item')
      print('2 - Remover item')
      print('3 - Alterar item')
      print('4 - Imprimir estoque')
      escolha = int(input('Faça sua escolha:'))
=======
       print('Controle de estoque')
       print('0 - Sair')
       print('1 - Adicionar item')
       print('2 - Remover item')
       print('3 - Alterar item')
       print('4 - Imprimir estoque')
<<<<<<< HEAD
       escolha = int(input('Faça sua escolha:'))
>>>>>>> 88b566224734c54dff65313626885caada03a597
=======
       escolha = int(input('Faça sua escolha: '))
>>>>>>> 6f88a908f1fc9559cac8cd79bd267032b709e7c6
     
with open ('Arquivo.txt','w') as arquivo:
   conteudo = json.dumps(estoque)
   arquivo.write(conteudo) 

   
