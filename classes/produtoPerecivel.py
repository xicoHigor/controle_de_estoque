from classes.produto import Produto

class ProdutoPerecivel(Produto):
    def __init__(self, nome, descricao, precoCompra, precoVenda, estoque, status, validade):
        super().__init__(nome, descricao, precoCompra, precoVenda, estoque, status)
        self.__validade = validade

    @property
    def validade(self):
        return self.__validade

    @validade.setter
    def validade(self, validade):
        self.__validade = validade
    
    