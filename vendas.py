from estoque import Estoque
from clientes import Clientes
from classes.item import Item
from classes.produto import Produto
from classes.produtoPerecivel import ProdutoPerecivel
import os

class Vendas:
    estoque = Estoque()
    cliente = Clientes()
    @classmethod
    def produto(cls, produto):
        pro =  cls.estoque.buscar_produtos(produto)
        if len(pro) > 6:
            produto = ProdutoPerecivel(pro[0].split('\n'), pro[1].split('\n'),pro[2].split('\n'),pro[3].split('\n'),pro[4].split('\n'),pro[5].split('\n'),pro[6].split('\n'),)
            return produto
        else:
            produto = Produto(pro[0].split('\n'), pro[1].split('\n'),pro[2].split('\n'),pro[3].split('\n'),pro[4].split('\n'),pro[5].split('\n'))
            return produto
        
    @classmethod
    def criar_pasta(cls, cliente):
        if os.path.exists('./pooAula/controle_estoque/historico/' + cliente):#cria 
            pass
        else:
            os.makedirs('./pooAula/controle_estoque/historico/' + cliente)


    def cadastrar_venda(self, cliente, itens):
        '''cadastra uma venda'''
        self.criar_pasta(cliente)
        venda = len(os.listdir('./pooAula/controle_estoque/historico/'+ cliente +'/')) + 1
        if (cliente + '.txt') in os.listdir('./pooAula/controle_estoque/pessoas/'):
            with open('./pooAula/controle_estoque/historico/' + cliente + '/venda'+ str(venda) + '.txt', 'w') as v:
                total = 0
                for item in itens:
                    v.write(item.produto.nome + '\n')
                    v.write(str(item.quantidade) + '\n')
                    v.write(str(item.total) + '\n')
                    total += item.total
                    self.estoque.atualizar_estoque(item.produto.nome, -int(item.quantidade))
                v.write(str(total))
                print('--' * 15)
            print('Operacao realizada com sucesso')
        else:
            print('cliente nao cadastrado')