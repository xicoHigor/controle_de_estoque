
import os
import datetime

class Estoque:


    def cadastrar_produto(self, nome, descricao, precoCompra, precoVenda, estoque, status, validade):
        '''cadastra um produto no estoque'''
        with open('./pooAula/projeto_estoque/produtos/' + nome + '.txt', 'w') as p:
            p.write(nome +','+ descricao + ',' + str(precoCompra) + ',' + str(precoVenda) + ',' + str(estoque) + ',' + status + ',' + validade)
            print('operacao realizada com sucesso')

    def listar_produtos(self):
        '''traz todos os produtos cadastrados'''
        produtos = os.listdir('./pooAula/projeto_estoque/produtos')
        for produto in produtos:
            with open('./pooAula/projeto_estoque/produtos/' + produto, 'r') as p:
                print(p.read().split(',')[0])
                print('--' * 20)    
 
 
    def listar_disponiveis(self):
        '''traz todos os produtos disponíveis'''
        produtos = os.listdir('./pooAula/projeto_estoque/produtos')
        lista = []
        for produto in produtos:
            with open('./pooAula/projeto_estoque/produtos/' + produto, 'r') as p:
                conteudo = p.read().split(',')
                if conteudo[5] == 'disponivel':
                    lista.append(conteudo)
       
        if len(lista)> 0:
            return lista
        else:
            return 'sem itens no estoque'


    def listar_esgotados(self):
        '''traz todos os produtos disponíveis'''
        produtos = os.listdir('./pooAula/projeto_estoque/produtos')
        for produto in produtos:
            with open('./pooAula/projeto_estoque/produtos/' + produto, 'r') as p:
                conteudo = p.read().split(',')
                lista = []
                if conteudo[5] == 'esgotado':
                    lista.append(conteudo)
                    return lista
                return 'sem itens no esgotados'

    def buscar_produto(self, produto): 
        '''busca um produto pelo nome'''
        if os.path.exists('./pooAula/projeto_estoque/produtos/' + produto + '.txt'):
            with open('./pooAula/projeto_estoque/produtos/' + produto + '.txt', 'r') as p:
                return p.read().split(',')
        return'produto nao cadastrado'

    def atualizar_estoque(self, produto, quantidade):
        '''aumenta o estque do produto'''
        produto = self.buscar_produto(produto)
        produto[4] = str(int(produto[4]) + int(quantidade))
        produto[5] = 'disponivel'
        with open('./pooAula/projeto_estoque/produtos/' + produto[0] + '.txt','w') as p:
            self.cadastrar_produto(produto[0], produto[1], produto[2], produto[3], produto[4], produto[5], produto[6])
       
    def remover_estoque(self, produto, quantidade):  
        '''diminui o estque do produto'''
        produto = self.buscar_produto(produto) 
        if int(produto[4]) >= quantidade:
              produto[4] = int(produto[4]) - quantidade
              if produto[4] == 0:
                produto[5] = 'esgotado'
              with open('./pooAula/projeto_estoque/produtos/' + produto[0] + '.txt','w') as p:
                self.cadastrar_produto(produto[0], produto[1], produto[2], produto[3], produto[4], produto[5], produto[6])
        else:
            print('quantidade insuficiente no estoque')

    def remover_produto(self, produto):
        if os.path.exists('./pooAula/projeto_estoque/produtos/' + produto + '.txt'):
            os.remove('./pooAula/projeto_estoque/produtos/' + produto + '.txt')
            return 'removido com sucesso'
        return 'produto nao cadastrado'
    
    def relatorio_estoque(self):
        data = datetime.datetime.now()
        with open('./pooAula/projeto_estoque/relatorio/relatorio' + str(data.date()) + '.txt', 'w') as r:
            r.write('Produtos em Estoque\n')
            r.write(('--' * 15) + '\n')
        produtos = os.listdir('./pooAula/projeto_estoque/produtos')
        estoque = None
        for produto in produtos:
            estoque = self.buscar_produto(produto.split('.txt')[0])           
            with open('./pooAula/projeto_estoque/relatorio/relatorio' + str(data.date()) + '.txt', 'a') as r:
                r.write('Produto: ' + estoque[0] + ' Quantidade: '+ estoque[4] + '\n' )
        print('Relatorio feito com sucesso')
