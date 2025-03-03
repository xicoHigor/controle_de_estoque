from classes.produto import Produto
class Item:
    def __init__(self, produto, quantidade):
        self.__produto = produto
        self.__quantidade = quantidade
        self.__total = int(produto.precoVenda) * int(quantidade)

    # metodos get
    @property
    def produto(self):
        return self.__produto
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @property
    def total(self):
        return self.__total

    # metodos set
    @produto.setter
    def produto(self, produto):
        self.__produto = produto

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade