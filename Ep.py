# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 07:44:23 2018
programa para o EP
@author: vitoria
"""

import json

with open ('Arquivo.txt','r') as arquivo:
    conteudo = arquivo.read()
    estoque = json.loads(conteudo)


valendo = True

entra = True
loja = input('Qual a loja?:')

print('Você acessou o estoque da loja {0}'.format(loja))

while entra:

    while valendo:
        
        print('')
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
                estoque[produto] = {}
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
                pergunta1 = input('Alterar quantidade?(s/n) ')
                if pergunta1 == 's':
                    quant2 = float(input('Quantidade adicionada: '))
                    estoque[produto]['quantidade'] += quant2
                    pergunta2 = input('Alterar o preco?(s/n) ')
                    
                    if pergunta2 == 's':
                        preco2 = float(input('Qual o novo preco? '))
                        while preco2 <= 0:
                            print('Não pode ser negativo')
                            preco2 = float(input('Qual o novo preco? '))
                        estoque[produto]['preco'] = preco2    
                    print('Novo estoque de {0}: quantidade: {1}, preco: {2}'.format(produto, estoque[produto]['quantidade'], estoque[produto]['preco'] ))
                    
                else:
                    pergunta2 = input('Alterar preco?(s/n) ')
                    if pergunta2 == 's':
                        preco2 = float(input('Qual o novo preco? '))
<<<<<<< HEAD
                        while preco2 <= 0:
                            print('Não pode ser negativo')
                            preco2 = float(input('Qual o novo preco? '))
                        estoque[produto]['preco'] = preco2         
                    print('Novo estoque de {0}: quantidade: {1}, preco: {2}'.format(produto, estoque[produto]['quantidade'], estoque[produto]['preco'] ))
            else:
                print('Elemento não encontrado')
    
                
        elif escolha == 4:
            print('Estoque:{0}'.format(estoque))
=======
                    estoque[produto]['preco'] = preco2         
                print('Novo estoque de {0}: quantidade: {1}, preco: {2}'.format(produto, estoque[produto]['quantidade'], estoque[produto]['preco'] ))
        else:
            print('Elemento não encontrado')

            
    elif escolha == 4:
        for produto in estoque:
            print('{0} - Quantidade:{1}, Preço: {2}'.format(produto, estoque[produto]['quantidade'], estoque[produto]['preco'] ))

    else: 
       print ('Comando Inválido.') 


with open ('Arquivo.txt','w') as arquivo:
   conteudo = json.dumps(estoque)
   arquivo.write(conteudo) 
   

for produto in estoque:
    estoque_negativo = []
>>>>>>> 1d23a7f2a5a301eeded54a1ff55fa080aab3b0ba
    
        else: 
           print ('Comando Inválido.') 
    
    
    with open ('Arquivo.txt','w') as arquivo:
       conteudo = json.dumps(estoque)
       arquivo.write(conteudo) 
       
    
    for produto in estoque:
        estoque_negativo = []
        
        if estoque[produto]['quantidade'] < 0:
            estoque_negativo.append(produto)
            
        total = 0
        if len(estoque) == 0:
            print('Nâo existem produtos em estoque')
        else:
            for produto in estoque:
                preco = estoque[produto]['preco']
                quantidade = estoque[produto]['quantidade']
                total += preco*quantidade 
                
        
    print ('Produtos com estoque negativo: {0}'.format(estoque_negativo))#não ta printando todos os produtos
    print ('Valor monetário total em estoque: {0}'.format(total))
    
    entra = False
    
