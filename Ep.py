# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 07:44:23 2018
programa para o EP
@author: vitoria
"""
<<<<<<< HEAD
estoque = {'banana'}
=======
import json

with open ('Arquivo.txt','r') as arquivo:
    conteudo = arquivo.read()
    estoque = json.loads(conteudo)


>>>>>>> 442f343586072afa5ffe39bf40f6cefba573e49d
print('Controle de estoque')
print('0 - sair')
print('1 - adicionar item')
print('2 - remover item')
print('3 - alterar item')
print('4 - Imprimir estoque')
escolha = int(input('Faça sua escolha: '))

<<<<<<< HEAD

valendo = True


while valendo :

   if escolha == 0:
       print('Até mais')
       valendo = False
    
   elif escolha == 1:
        produto = input('Nome do produto: ')
        
        if produto in estoque:
            print('Produto ja está cadastrado.')
        else:
            quant = float(input('Qual a quantidade?:'))
            
            if quant < 0:
                print('Quantidade inicial nao pode ser negativa.')
                float(input('Quantidade inicial: '))
                estoque[produto]=[quant]
        escolha = int(input('Faça sua escolha: '))
        
        
   elif escolha == 2:  #NAO ESTA REMOVENDO
        delpro = input('Nome do produto: ')
        if delpro in estoque:
            del estoque[delpro]
        else:
            print('Elemento não encontrado')
        escolha = int(input('Faça sua escolha: '))
        
   elif escolha == 3:
        produto = input('Nome do produto: ')
        quant2 = float(input('Quantidade: '))
        estoque[produto] = quant2+quant
        print('Novo estoque de {0}:{1}'.format(produto, quant))
     
   elif escolha == 4:
        print(estoque)
        
   else:
      print ('Comando Inválido')
=======
if x == 0:
    print('Até mais')
elif x == 1:
    produto = input('Nome do produto: ')
    if produto in estoque:
        print('Produto ja está cadastrado.')
    quant = float(input('Quantidade inicial: '))
    if quant < 0:
        print('Quantidade inicial nao pode ser negativa.')
        float(input('Quantidade inicial: '))
    estoque[produto]=[quant]
x = int(input('Faça sua escolha: '))
elif x == 2:
     delpro = input('Nome do produto: ')
     if delpro in estoque:
        del estoque[delpro]
     else:
        print('Elemento não encontrado')
x = int(input('Faça sua escolha: '))
elif x == 3:
     produto = input('Nome do produto: ')
     quant2 = float(input('Quantidade: '))
     estoque[produto] = quant2+quant
     print('Novo estoque de {0}:{1}'.format(produto, quant))
     
     
     
with open ('Arquivo.txt','a') as arquivo:
    conteudo = arquivo.write()
    original = json.dumps(conteudo)
    print(original)
>>>>>>> 442f343586072afa5ffe39bf40f6cefba573e49d
