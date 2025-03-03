from classes.produto import Produto
from classes.produtoPerecivel import ProdutoPerecivel
from estoque import Estoque
from clientes import Clientes
from classes.cliente import Cliente
from vendas import Vendas
from classes.item import Item
'''estoque = Estoque()
produto = Produto('camisa', 'camisa de algodao', '10', '20', '100', 'disponivel')
produtoPer = ProdutoPerecivel('arroz', 'branco e gostoso', '10', '20', '100', 'disponivel', '10/10/2020')
produto2 = Produto('calca', 'calca de algodao', '10', '20', '100', 'esgotado')
produtoPer2 = ProdutoPerecivel('feijao', 'branco e gostoso', '10', '20', '100', 'esgotado', '10/10/2020')

estoque.cadastrar_produto(produto)
estoque.cadastrar_produto(produto)
estoque.cadastrar_produto(produtoPer)
estoque.cadastrar_produto(produto2)
estoque.cadastrar_produto(produtoPer2)
estoque.listar_produtos()
estoque.listar_disponiveis()
estoque.listar_esgotados()
estoque.atualizar_estoque('arroz', 50)
estoque.remover_produto('cuzcuz')'''
'''cliente1 = Cliente('joao', 'joao@joao', '10/10/2020')
cliente2 = Cliente('maria', 'maria@maria', '10/10/2020')
clientes = Clientes()
clientes.cadastrar_Cliente(cliente1)
clientes.cadastrar_Cliente(cliente2)
clientes.listar_Clientes()
print(clientes.buscar_cliente(cliente1.nome))
clientes.mudar_email('joao', 'joao@gmail.com')'''
produto = Produto('camisa', 'camisa de algodao', '10', '20', '100', 'disponivel')
produtoPer = ProdutoPerecivel('arroz', 'branco e gostoso', '10', '20', '100', 'disponivel', '10/10/2020')
produto2 = Produto('calca', 'calca de algodao', '10', '20', '100', 'esgotado')
produtoPer2 = ProdutoPerecivel('feijao', 'branco e gostoso', '10', '20', '100', 'esgotado',  '10/10/2020')
item1 = Item(produto, 10)
item2 = Item(produtoPer, 10)
item3 = Item(produtoPer2, 10)
lista = [item1, item2, item3]
vendas = Vendas()
vendas.cadastrar_venda('joao', lista)