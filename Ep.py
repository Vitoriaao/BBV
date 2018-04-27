# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 23:01:54 2018

@author: Beatriz
"""
#import json

#with open ('Arquivo.txt','r') as arquivo:
    #conteudo = arquivo.read()
    #estoque = json.loads(conteudo)
    

from firebase import firebase
firebase = firebase.FirebaseApplication('https://ep1-bbv.firebaseio.com/',None)


try :
    estoque = firebase.get('/estoque', None)
    estoque = estoque [0][0]
except:
    estoque= {'loja': {}}

#import tkinter as tk
#
#
#class Estoque:
#    def init(self):
#        self.window = tk.Tk()
#        
#        self.botao =tk.Button(self.window)
#        self.botao.configure(text = 'Clique aqui para acessar o Sistema de Gerenciamento de Estoques')
#        self.botao.configure(command = self.acessar_estoque)
#        self.botao.grid()
#
#
#    def iniciar(self):
#        self.window.mainloop()
#        
#    def acessar_estoque(self):

valendo = True
        
entra = True
        
while entra:
            
        #    loja = input('Qual a loja?:')
        #    estoque[loja] = {}
            print('')
            print('controle loja')
            print('0 - Sair')
            print('1 - Adicionar loja')
            print('2 - Remover loja')
            print('3 - Entrar no estoque de loja')
            escolha_loja= int(input('Faça sua escolha: '))
        #    print('Você acessou o estoque da loja {0}'.format(loja))
            if escolha_loja == 0:
                print('Até mais')
                entra = False
                break
            elif escolha_loja == 1:
                loja = input('Nome da loja: ')
                
                if loja in estoque:
                    print('Loja já cadastrada')
                    entra = False
                else:
                    estoque[loja] = {}
            elif escolha_loja == 2:
                deloja = input('Nome do loja: ')
                if deloja in estoque[loja]:
                    del estoque[loja][deloja]
                    valendo = False
                else:
                    print('Loja não encontrada.')
                    valendo = False
            elif  escolha_loja == 3:
                loja = input('Nome da loja: ')
                if loja in estoque:
                    valendo = True
                else:
                    print('Comando inválido.')
                    valendo = False
                   
        
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
                   entra = False
                   break
                
                elif escolha == 1:
                    produto = input('Nome do produto: ')
                    
                    if produto in estoque[loja]:
                        print('Produto já cadastrado.')
                    else:
                        estoque[loja][produto] = {}
                        preco = 0.0
                        while preco <= 0:
                             preco = float(input('Qual o valor do produto? '))
                             if preco <= 0:
                                 print('O preço deve ser positivo')
                        estoque[loja][produto]['preco'] = preco    
                             
                        quant = int(input('Quantidade inicial: '))
                        if quant < 0:
                            print('Quantidade inicial não pode ser negativa.')
                            quant = int(input('Quantidade inicial: '))
                            if quant > 0:
                                estoque[loja][produto]['quantidade']=quant
                            else:
                                print('Quantidade inicial inválida.')
                        elif quant > 0:
                            estoque[loja][produto]['quantidade']=quant
                        else:
                            print('Quantidade inicial não pode ser nula.')
                            quant = int(input('Quantidade inicial: '))
                            if quant > 0:
                                estoque[loja][produto]['quantidade']=quant
                            else:
                                print('Quantidade inicial inválida.')
               
                    
                elif escolha == 2:
                    delpro = input('Nome do produto: ')
                    if delpro in estoque[loja]:
                        del estoque[loja][delpro]
                    else:
                        print('Elemento não encontrado')
                        
            
                elif escolha == 3:
                    produto = input('Nome do produto: ')
                    if produto in estoque[loja]:
                        pergunta1 = input('Alterar quantidade?(s/n) ')
                        if pergunta1 == 's':
                            quant2 = int(input('Quantidade adicionada: '))
                            estoque[loja][produto]['quantidade'] += quant2
                            pergunta2 = input('Alterar o preco?(s/n) ')
                            
                            if pergunta2 == 's':
                                preco2 = float(input('Qual o novo preco? '))
                                while preco2 <= 0:
                                    print('Não pode ser negativo')
                                    preco2 = float(input('Qual o novo preco? '))
                                estoque[loja][produto]['preco'] = preco2    
                            print('Novo estoque de {0}: quantidade: {1}, preco: {2}'.format(produto, estoque[loja][produto]['quantidade'], estoque[loja][produto]['preco'] ))
                            
                        else:
                            pergunta2 = input('Alterar preco?(s/n) ')
                            if pergunta2 == 's':
                                preco2 = float(input('Qual o novo preco? '))
                                
                                while preco2 <= 0:
                                    print('O preço nao pode ser menor que zero')
                                    preco2 = float(input('Qual o novo preco? '))
                                estoque[loja][produto]['preco'] = preco2         
                            print('Novo estoque de {0}: quantidade: {1}, preco: {2}'.format(produto, estoque[loja][produto]['quantidade'], estoque[loja][produto]['preco'] ))
                    else:
                        print('Elemento não encontrado')
            
                elif escolha == 4:
                    for produto in estoque[loja]:
                        print('{0} - Quantidade:{1}, Preço: {2}'.format(produto, estoque[loja][produto]['quantidade'], estoque[loja][produto]['preco'] ))        
                    for produto in estoque[loja]:
                         estoque_negativo = []   
                         if estoque[loja][produto]['quantidade'] < 0:
                             estoque_negativo.append(estoque[loja])
                                
                         total = 0
                         if len(estoque) == 0:
                             print('Não existem produtos em estoque.')
                         else:
                             for produto in estoque[loja]:
                                    preco = estoque[loja][produto]['preco']
                                    quantidade = estoque[loja][produto]['quantidade']
                                    total += preco*quantidade 
                    print ('Produtos com estoque negativo: {0}'.format(estoque_negativo))
                    print ('Valor monetário total em estoque: {0}'.format(total))                
                else:
                    print('Comando inválido')


#with open ('Arquivo.txt','w') as arquivo:
#   conteudo = json.dumps(estoque)
#   arquivo.write(conteudo) 

#app = Estoque()
#app.iniciar()


fbestoque = [estoque]
firebase.put('/estoque', '0', fbestoque)