from classes.produto import Produto
from classes.produtoPerecivel import ProdutoPerecivel
import os

class Estoque:

    @staticmethod
    def mecher_no_estoque(produto, valor):
        '''aumenta ou diminui o estoque de um produto'''
        with open('./pooAula/controle_estoque/produtos/'+ produto + '.txt', 'r') as p:
            conteudo = p.readlines()
            estoque = int(conteudo[4].strip('\n')[0]) + valor
            return estoque
    

    def cadastrar_produto(self, produto):
        '''cadastra um produto no estoque'''
        with open('./pooAula/controle_estoque/produtos/' + produto.nome + '.txt', 'w') as p:
            p.write(produto.nome + '\n')
            p.write(produto.descricao + '\n')
            p.write(produto.precoCompra + '\n')
            p.write(produto.precoVenda + '\n')
            p.write(produto.estoque + '\n')
            p.write(produto.status + '\n')
            if type(produto) is ProdutoPerecivel:
                p.write(produto.validade)
            print('produto cadastrado com sucesso')

    def listar_produtos(self):
        '''traz todos os produtos cadastrados'''
        produtos = os.listdir('./pooAula/controle_estoque/produtos')
        for produto in produtos:
            with open('./pooAula/controle_estoque/produtos/' + produto, 'r') as p:
                print(p.read())
                print('--' * 20)    
 
 
    def listar_disponiveis(self):
        '''traz todos os produtos disponíveis'''
        produtos = os.listdir('./pooAula/controle_estoque/produtos')
        print('Produtos disponíveis:')
        print('--' * 20)
        for produto in produtos:
            with open('./pooAula/controle_estoque/produtos/' + produto, 'r') as p:
                conteudo = p.read()
                if 'disponivel' in conteudo:
                    print(conteudo)
                    print('--' * 20)    


    def listar_esgotados(self):
        '''traz todos os produtos esgotados'''
        produtos = os.listdir('./pooAula/controle_estoque/produtos')
        print('Produtos indisponíveis:')
        print('--' * 20)
        for produto in produtos:
            with open('./pooAula/controle_estoque/produtos/' + produto, 'r') as p:
                conteudo = p.read()
                if 'esgotado' in conteudo:
                    print(conteudo)
                    print('--' * 20)

    def buscar_produto(self, produto): 
        '''busca um produto pelo nome'''
        
        if os.path.exists('./pooAula/controle_estoque/produtos/' + produto + '.txt'):
            with open('./pooAula/controle_estoque/produtos/' + produto + '.txt', 'r') as p:
                return p.readlines()
        else:
            print('produto nao cadastrado')

    def atualizar_estoque(self, produto, valor):
        '''aumenta o estque do produto'''

        if os.path.exists('./pooAula/controle_estoque/produtos/' + produto + '.txt'):
            estoque = self.mecher_no_estoque(produto, valor)
            p = self.buscar_produto(produto)
           
            for x in range(len(p)):
                p[x] = p[x].strip('\n')
            
            p[4] =  estoque + int(p[4])

            if len(self.buscar_produto(produto)) > 6:
                atualiza = ProdutoPerecivel(p[0], p[1], str(p[2]), str(p[3]), str(p[4]), p[5], p[6])
            
            else:
                 atualiza = Produto(p[0],p[1],str(p[2]),str(p[3]),str(p[4]),p[5])
            self.cadastrar_produto(atualiza)

            print('estoque Atualizado')
        else:
            print('produto nao cadastrado')

    def remover_produto(self, produto):
        if os.path.exists('./pooAula/controle_estoque/produtos/' + produto + '.txt'):
            os.remove('./pooAula/controle_estoque/produtos/' + produto + '.txt')
            print('produto removido')
        else:
            print('produto nao cadastrado')