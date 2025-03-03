
class Produto():
    def __init__(self, nome, descricao, precoCompra, precoVenda, estoque, status):
        self.__nome = nome
        self.__descricao = descricao
        self.__precoCompra = precoCompra
        self.__precoVenda = precoVenda
        self.__estoque = estoque
        self.__status = status
    
    # metodos get
    @property
    def nome(self):
        return self.__nome
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def precoCompra(self):
        return self.__precoCompra
    
    @property
    def precoVenda(self):
        return self.__precoVenda
    
    @property
    def estoque(self):
        return self.__estoque
    
    @property
    def status(self):
        return self.__status
    
    # metodos set
    @nome.setter
    def nome(self, nome):
        self.__nome =nome
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @precoCompra.setter
    def precoCompra(self, precoCompra):
        self.__precoCompra = precoCompra

    @precoVenda.setter
    def precoVenda(self, precoVenda):
        self.__precoVenda = precoVenda

    @estoque.setter
    def estoque(self, estoque):
        self.__estoque = estoque

    @status.setter
    def status(self, status):
        self.__status = status
        