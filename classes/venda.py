from item import Item

class venda:
    def __init__(self, nomeCliente, dataCompra, itens):
        self.__nomeCliente = nomeCliente
        self.__dataCompra = dataCompra
        self.__itens[] = itens

        #metodos get
        @property
        def nomeCliente(self):
            return self.__nomeCliente

        @property
        def dataCompra(self):
            return self.__dataCompra
        
        @property
        def itens(self):
            return self.itens

        #metodos set
        @nomeCliente.setter
        def nomeCliente(self, nomeCliente):
            self.__nomeCliente = nomeCliente

        @dataCompra.setter
        def dataCompra(self, dataCompra):
            self.dataCompra = dataCompra
