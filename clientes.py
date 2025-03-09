import os
class Clientes:
    def cadastrar_Cliente(self, nome, email, dataCadastro):
        '''cadastra um cliente'''
        with open('./pooAula/projeto_estoque/pessoas/' + nome + '.txt', 'w') as p:
            p.write(nome + ',' + email + ',' + dataCadastro)
            print('Operacao realizada com sucesso')

    def listar_Clientes(self):
        '''lista todos os clientes'''
        print('lista de clientes')
        for pessoa in os.listdir('./pooAula/projeto_estoque/pessoas/'):
            with open('./pooAula/projeto_estoque/pessoas/' + pessoa, 'r') as p:
                print(p.read())
                print('--' * 15)


    def buscar_cliente(self, nome):
        clientes = os.listdir('./pooAula/projeto_estoque/pessoas/')
        if nome + '.txt'  in clientes:
            with open('./pooAula/projeto_estoque/pessoas/' + nome + '.txt', 'r') as c:
                return c.read().split(',')
        else:
            return 'cliente nao cadastrado'

    def mudar_email(self, nome, novo_email):
        '''mudar email'''
        conteudo = self.buscar_cliente(nome).split(',')
        self.cadastrar_Cliente(conteudo[0], novo_email, conteudo[2])