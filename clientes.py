from classes.cliente import Cliente
import os
class Clientes:
    def cadastrar_Cliente(self, cliente):
        '''cadastra um cliente'''
        with open('./pooAula/controle_estoque/pessoas/' + cliente.nome + '.txt', 'w') as p:
            p.write(cliente.nome + '\n')
            p.write(cliente.email + '\n')
            p.write(cliente.dataCadastro + '\n')
            print('Operacao realizada com sucesso')

    def listar_Clientes(self):
        '''lista todos os clientes'''
        print('lista de clientes')
        for pessoa in os.listdir('./pooAula/controle_estoque/pessoas/'):
            with open('./pooAula/controle_estoque/pessoas/' + pessoa, 'r') as p:
                print(p.read())
                print('--' * 15)


    def buscar_cliente(self, nome):
        clientes = os.listdir('./pooAula/controle_estoque/pessoas/')
        if nome in clientes:
            with open('./pooAula/controle_estoque/pessoas/' + nome + '.txt', 'r') as c:
                return c.readlines()
        else:
            return 'cliente nao cadastrado'

    def mudar_email(self, nome, novo_email):
        '''mudar email'''
        conteudo = self.buscar_cliente(nome)
        cliente = Cliente(conteudo[0].split('\n')[0], novo_email, conteudo[2].split('\n')[0])
        self.cadastrar_Cliente(cliente)