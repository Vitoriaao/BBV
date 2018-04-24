# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 07:44:23 2018
programa para o EP
@author: vitoria
"""

import json
from pprint import pprint

with open ('Arquivo.txt','r') as arquivo:
    conteudo = arquivo.read()
    estoque = json.loads(conteudo)


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
        estoque[produto] = produto
        
        if produto in estoque:
            print('Produto já cadastrado.')
        else:
            preco = 0.0
            
            while preco <= 0:
                 preco = float(input('Qual o valor do produto? '))
                 if preco <= 0:
                     print('O preço deve ser positivo')
                 estoque[produto]['preco'] = preco    
                 
            quant = float(input('Quantidade inicial: '))
            if quant < 0:
                print('Quantidade inicial não pode ser negativa.')
                quant = float(input('Quantidade inicial: '))
                if quant > 0:
                    estoque[produto]['quantidade']=quant
                else:
                    print('Quantidade inicial inválida.')
            elif quant > 0:
                estoque[produto]['quantidade']=quant
            else:
                print('Quantidade inicial não pode ser nula.')
                quant = float(input('Quantidade inicial: '))
                if quant > 0:
                    estoque[produto]['quantidade']=quant
                else:
                    print('Quantidade inicial inválida.')
   
        
        
    elif escolha == 2:
        delpro = input('Nome do produto: ')
        if delpro in estoque:
            del estoque[delpro]
        else:
            print('Elemento não encontrado')
            

        
    elif escolha == 3:
        produto = input('Nome do produto: ')
        if produto in estoque:
            quant2 = float(input('Quantidade adicionada: '))
            estoque[produto]['quant'] += quant2
            pergunta = input('Vai alterar o preco? (sim / nao)')
            if pergunta == 'sim':
                preco2 = float(input('Qual o novo preco? '))
                while preco2 <= 0:
                    print('Não pode ser negativo')
                    preco2 = float(input('Qual o novo preco? '))
                    estoque[produto]['preco'] = preco2        
            
            print('Novo estoque de {0}: {1}, {2}'.format(produto, estoque[produto]['quant'], estoque[produto]['preco'] ))
        else:
            print('Elemento não encontrado')
        
 
        
        
    elif escolha == 4:
        print('Estoque:{0}'.format(estoque))

 
        
    else: 
       print ('Comando Inválido') 



with open ('Arquivo.txt','w') as arquivo:
   conteudo = json.dumps(estoque)
   arquivo.write(conteudo) 

   