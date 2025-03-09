from estoque import Estoque
from clientes import Clientes
from vendas import Vendas
import datetime

estoque = Estoque()
estoque.relatorio_estoque
'''estoque.cadastrar_produto('camisa', 'camisa de algodao', '10', '20', '100', 'disponivel', 'nao-perecivel')
estoque.cadastrar_produto('arroz', 'branco e gostoso', '10', '20', '100', 'disponivel', '10/10/2020')
estoque.cadastrar_produto('calca', 'calca de algodao', '10', '20', '100', 'esgotado', 'nao-perecivel')
estoque.cadastrar_produto('feijao', 'branco e gostoso', '10', '20', '100', 'esgotado',  '10/10/2020')
estoque.listar_produtos()
'''
'''cliente = Clientes()
cliente.cadastrar_Cliente('higor', 'higor@higor', '10/10/2020')
cliente.cadastrar_Cliente('joao', 'joao@joao', '10/10/2020')
cliente.cadastrar_Cliente('maria', 'maria@maria', '10/10/2020')
cliente.listar_Clientes()
print(cliente.buscar_cliente('higor'))
'''
print('meu deus')
venda = Vendas()
print(venda.ListaFinal())
#venda.relatorioPDF()
venda.relatorioPDF_data('2025-03-03')
#venda.cadastrar_venda('higor', [['camisa', 2], ['arroz', 80], ['calca', 2], ['feijao', 2]])
#venda.listar_vendas()
#venda.buscar_vendas_nome('higor')
