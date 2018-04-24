# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 07:44:23 2018
programa para o EP
@author: vitoria
"""
<<<<<<< HEAD
<<<<<<< HEAD
estoque = {}
=======
=======

>>>>>>> 11cf69066bd47ebd72c2fa001849b3b5f73c1806
import json
from pprint import pprint

with open ('Arquivo.txt','r') as arquivo:
    conteudo = arquivo.read()
    estoque = json.loads(conteudo)

with open ('Arquivo.txt','a') as arquivo:
    conteudo = arquivo.write('')
    estoque = json.dumps(conteudo) 


print('Controle de estoque')
print('0 - Sair')
print('1 - Adicionar item')
print('2 - Remover item')
print('3 - Alterar item')
print('4 - Imprimir estoque')
escolha = int(input('Faça sua escolha: '))


valendo = True


while valendo:

   if escolha == 0:
       print('Até mais')
       valendo = False
    
   elif escolha == 1:
        produto = input('Nome do produto: ')
        
        if produto in estoque:
            print('Produto já cadastrado.')
        else:
            quant = float(input('Quantidade inicial:'))
            #precisa adicionar o produto no estoque
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
            
        print('Controle de estoque')
        print('0 - Sair')
        print('1 - Adicionar item')
        print('2 - Remover item')
        print('3 - Alterar item')
        print('4 - Imprimir estoque')
        escolha = int(input('Faça sua escolha: '))
        
   elif escolha == 3: #não está somando a nova quantidade no estoque
        produto = input('Nome do produto: ')
        if produto in estoque:
            quant2 = float(input('Quantidade: '))
            estoque[produto] += quant2
            print('Novo estoque de {0}:{1}'.format(produto, estoque[produto]))
        else:
            print('Elemento não encontrado')
        
        print('Controle de estoque')
        print('0 - Sair')
        print('1 - Adicionar item')
        print('2 - Remover item')
        print('3 - Alterar item')
        print('4 - Imprimir estoque')
        escolha = int(input('Faça sua escolha:'))
        
   elif escolha == 4:
        pprint('Estoque:{0}'.format(estoque))
        
        print('Controle de estoque')
        print('0 - Sair')
        print('1 - Adicionar item')
        print('2 - Remover item')
        print('3 - Alterar item')
        print('4 - Imprimir estoque')
        escolha = int(input('Faça sua escolha:'))
        
   else: 
      print ('Comando Inválido') 
      
      print('Controle de estoque')
      print('0 - Sair')
      print('1 - Adicionar item')
      print('2 - Remover item')
      print('3 - Alterar item')
      print('4 - Imprimir estoque')
      escolha = int(input('Faça sua escolha:'))
     
 

   
