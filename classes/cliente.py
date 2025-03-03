class Cliente:
    def __init__(self, nome, email, dataCadastro):
        self.__nome = nome
        self.__email = email
        self.__dataCadastro = dataCadastro

    # metodos get
    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def dataCadastro(self):
        return self.__dataCadastro

    #metodos set
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @email.setter
    def email(self, email):
        self.__email = email

    @dataCadastro.setter
    def dataCadastro(self, dataCadastro):
        self.__dataCadastro = dataCadastro