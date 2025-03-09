from estoque import Estoque
from clientes import Clientes
import os
import datetime
import pydf
from random import randint
class Vendas:
    estoque = Estoque()
    cliente = Clientes()

    @classmethod
    def criar_pasta(cls, cliente):
        if cls.verificar_cliente(cliente):
            if not os.path.exists('./pooAula/projeto_estoque/historico/' + cliente):
                os.makedirs('./pooAula/projeto_estoque/historico/' + cliente)
        
    @classmethod
    def verificar_cliente(cls, cliente):

        if os.path.exists('./pooAula/projeto_estoque/pessoas/' + cliente + '.txt'):
            return True
        return False
        
    @classmethod
    def verificar_estoque(cls, produto, quantidade):
      
      produto =  cls.estoque.buscar_produto(produto)

      
      if produto == 'produto nao cadastrado':
        return False
      else:
        if quantidade <= int(produto[4]):
          return produto
    @classmethod
    def buscar_vendas_cod(cls, codigo):
        lista = os.listdir('./pooAula/projeto_estoque/historico')
        for venda in lista:
            vendas = os.listdir('./pooAula/projeto_estoque/historico/' + venda)
            for arquivo in vendas:
                with open('./pooAula/projeto_estoque/historico/'+ venda + '/' + arquivo) as a:
                    conteudo = a.readlines()                
                    if str(codigo) == conteudo[-1].split(',')[-1]:
                        lista = [venda, conteudo]
                        return lista
        
        return 'venda nao cadastrada'

    @classmethod
    def gerarCodigo(cls):
        
        cod = randint(1, 1000)
        lista = os.listdir('./pooAula/projeto_estoque/historico')
        if len(lista) == 0:
            return cod 
        comparar = cls.buscar_vendas_cod(cod)
        if comparar == 'venda nao cadastrada':
            return str(cod)
        else:
            cls.gerarCod()

    @classmethod
    def    verificarData(cls, data):
        lista = os.listdir('./pooAula/projeto_estoque/historico')
        for cliente in lista:
            vendas = os.listdir('./pooAula/projeto_estoque/historico/' + cliente)
            for venda in vendas:
                with open('./pooAula/projeto_estoque/historico/' + cliente + '/' + venda) as v:
                    conteudo = v.readlines()
                    conteudo = conteudo[-1].split(',')
                    if conteudo[1] == data:
                        print(data)
                        return True
        return False 


    @staticmethod
    def stilo():
        return '''<style>
        table {
  border: 1px solid black;
  border-collapse: collapse;
  background-color: #f5f5f5;
  width: 100%;
  margin-bottom: 20px;
}

th, td {
  padding: 8px;
  text-align: left;
}

th {
  background-color: #333;
  color: #fff;
}

tr:nth-child(even) {
  background-color: #ddd;
}

tr:hover {
  background-color: #ccc;
}

        </style>
        <center><h1>Relatorio de Vendas</h1></center>'''
        

    def cadastrar_venda(self, cliente, listaVenda, precoVenda =0 , valorTotal=0, data=None, conta=0):
        cod = self.gerarCodigo()
        self.criar_pasta(cliente)
        venda = os.listhir('./pooAula/projeto_estoque/historico/' + cliente)
    
        venda = len(venda) + 1

        if self.verificar_cliente(cliente) != False:
            
            with open('./pooAula/projeto_estoque/historico/' + cliente + '/' + 'venda' + str(venda) + '.txt', 'a' ) as v:
              
                for x in listaVenda:
                    if self.verificar_estoque(x[0], x[1]):
                        precoVenda = self.estoque.buscar_produto(x[0])
                        valorTotal = x[1] * int(precoVenda[3])
                        v.write(x[0] + ',' + str(precoVenda[3]) + ',' + str(x[1]) + ',' + str(valorTotal)+'\n')
                        self.estoque.remover_estoque(x[0], int(x[1]))
                        print('--' * 15)
                        conta += valorTotal
                    else:
                        print(x[0] + ' nao disponivel no estoque')
                data = datetime.datetime.now().date()
                v.write(str(conta)+ ',' + str(data) + ',' + cod)
        else:
            print('cliente nao cadastrado')
        
    def listar_vendas(self):
        vendas = os.listdir('./pooAula/projeto_estoque/historico')
        for x in vendas:
            vendas2 = os.listdir('./pooAula/projeto_estoque/historico/'+ x)
            print('--' * 15)        
            for venda in vendas2:
                with open('./pooAula/projeto_estoque/historico/'+ x + '/' + venda) as f:
                        conteudo = f.readlines()
                        for y in conteudo:
                            produto = y.split(',')
                            if len(produto) == 4:
                                print('Produto: ', produto[0])
                                print('Preco: ',  produto[1])
                                print('Quantidade: ', produto[2])
                                print('Valor de venda: ',  produto[3].split('\n')[0])
                                print(' ' * 5 + ('--' * 5) + ' ' * 5)
                        ultimaLinha = conteudo[-1].split(',')
                        print('Total a pagar:', ultimaLinha[0])
                        print('Data da Venda:', ultimaLinha[1])
                        print('Codigo da Venda:', ultimaLinha[2])
                        print('--' * 15)                


    def buscar_vendas_nome(self, nome):
            if self.verificar_cliente(nome):
                vendas = os.listdir('./pooAula/projeto_estoque/historico/'+ nome)
                print('--' * 15)
                print('--' * 2 + (' Historico de '+ nome +' ') + '--' * 2) 
                print('--' * 15)       
                for venda in vendas:
                    with open('./pooAula/projeto_estoque/historico/'+ nome + '/' + venda) as f:
                            conteudo = f.readlines()
                            for y in conteudo:
                                produto = y.split(',')
                                if len(produto) == 4:
                                    print('Produto: ', produto[0])
                                    print('Preco: ',  produto[1])
                                    print('Quantidade: ', produto[2])
                                    print('Valor de venda: ',  produto[3].split('\n')[0])
                                    print(' ' * 5 + ('--' * 5) + ' ' * 5)
                            ultimaLinha = conteudo[-1].split(',')
                            print('Total a pagar:', ultimaLinha[0])
                            print('Data da Venda:', ultimaLinha[1])
                            print('Codigo da Venda:', ultimaLinha[2])
                            print('--' * 15)                
            
            else: print('cliente nao cadastrado')

    def detalhamento_vendas(self, cod):
        vendas = self.buscar_vendas_cod(cod)
        if vendas != 'venda nao cadastrada':
            lucro = 0
            dt = None
            celula = self.cliente.buscar_cliente(vendas[0])
            print(vendas[0])
            print('Cliente: ' + celula[0])
            print('Email: ' + celula[1])
            print('Data de Cadastro: ' + celula[2])
            vendas = vendas[1]
            for proVenda in vendas:
                print('--' * 15)
                proVenda = proVenda.split(',')
                if proVenda[0].isdigit():
                    lucro += int(proVenda[0])
                    dt = proVenda[1]
                    print('Data da Venda: ' + dt)
                    print('Codigo da Venda: ' + proVenda[2])
                    print('lucro Total: ', lucro)
                else:
                    produto = self.estoque.buscar_produto(proVenda[0])
                    print('Produto: ' + produto[0])
                    print('Descricao Produto: ' + produto[1])
                    print('preco do Produto: ' + proVenda[1])
                    print('quantidade vendida: ' + proVenda[2])
                    precoVenda = int(produto[2]) * int(proVenda[2])
                    lucro -= precoVenda
        else:
            print('venda nao cadastrada')
        
    def ListaFinal(self):

        lista = os.listdir('./pooAula/projeto_estoque/historico')
        listaFinal = []
        for clie in lista:
            listaDinamica1 = []
            pessoa = self.cliente.buscar_cliente(clie)
            listaDinamica1.append(pessoa[0])
            listaDinamica1.append(pessoa[1])
            listaDinamica1.append(pessoa[2])
            clientes = os.listdir('./pooAula/projeto_estoque/historico/' + clie + '/')
            for ven in clientes:
                listaDinamica2 = []
                with open('./pooAula/projeto_estoque/historico/'+ clie + '/' + ven) as r:
                    venda = r.readlines()
                    lucro = 0
                    for linha in venda:
                        
                        linha = linha.split(',')
                        if linha[0].isdigit():
                            listaDinamica2.append(str(linha[0]) + ' ')
                            listaDinamica2.append(int(linha[0]) - lucro)
                            listaDinamica2.append(linha[1])
                            listaDinamica2.append(int(linha[2]))
                            
                        else:
                            produto = self.estoque.buscar_produto(linha[0])
                            listaDinamica2.append(produto[0])
                            listaDinamica2.append(produto[1])
                            listaDinamica2.append(produto[2])
                            listaDinamica2.append(linha[1])
                            listaDinamica2.append(linha[2])
                            listaDinamica2.append(linha[3].split('\n')[0])
                            lucro = lucro + (int(produto[2]) * int(linha[2]))
                    listaFinal.append(listaDinamica1 + listaDinamica2)
        return listaFinal


    def relatorioPDf(self):
        estilo = self.stilo()
        vendas = self.ListaFinal()
        print(len(vendas))
        textofinal = ''
        for venda in vendas:
         

            index = 0
            index1 = 1
            index2 = 2
            textofinal += f'''
            
<table border="1">>
    <tr>
        <th>Cliente</th>
        <th>{venda[index]}</th>
    </tr>
    <tr>
        <th>Email</th>
        <th>{venda[index1]}</th>
    </tr>
    <tr>
        <th>Data de Cadastro</th>
        <th>{venda[index2]}</th>
    </tr>
<tr>'''
            index = 3 
            index1 = 4
            index2 = 5
            index3 = 6
            index4 = 7
            index5 = 8
            cont = 0
            while True:
                index += cont 
                index1 += cont
                index2 += cont
                index3 += cont
                index4 += cont
                index5 += cont

                texto = f''' <tr>
                                    <th >       </th>
                                    <th >        </th>
                                </tr>
                                
                                <tr>
                                    <th>Produto</th>
                                    <th>{venda[index]}</th>
                                </tr>
                                <tr>
                                    <th>Descricao</th>
                                    <th>{venda[index1]}</th>
                                </tr>
                                <tr>
                                    <th>Preco de Compra</th>
                                    <th>{venda[index2]}</th>
                                </tr>
                                <tr>
                                    <th>Preco de Venda</th>
                                    <th>{venda[index3]}</th>
                                </tr>
                                <tr>
                                    <th>Quantidade</th>
                                    <th>{venda[index4]}</th>
                                </tr>
                                <tr>
                                    <th>valor da venda</th>
                                    <th>{venda[index5]}</th>
                                </tr>'''
                textofinal += texto
                if ' ' in venda[index5 + 1]:
                    print('entrou aqui', venda[index5 + 1])
                    index = index5 + 1
                    index1 = index5 + 2
                    index2 = index5 + 3
                    index3 = index5 + 4
                    texto = f'''
                                    <th>Preco final da venda</th>
                                    <th>{venda[index]}</th>
                                </tr>
                                <tr>
                                    <th>Lucro</th>
                                    <th>{venda[index1]}</th>
                                </tr>
                                <tr>
                                    <th>Data da Compra</th>
                                    <th>{venda[index2]}</th>
                                </tr>
                                <tr>
                                    <th>codigo da Compra</th>
                                    <th>{venda[index3]}</th>
                                </tr>
                                  
                                </table>''' 
                    textofinal += texto
                    break
                else:
                    cont += 6
                textofinal += texto        
        textoPDF = estilo + textofinal
        print(textoPDF)
        pdf = pydf.generate_pdf(textoPDF)
        with open('./pooAula/projeto_estoque/relatorioPDF/relatorio_total.pdf', 'wb') as arquivo:
            arquivo.write(pdf)

    def relatorioPDF_data(self, data):
      
        estilo = self.stilo()
        vendas = self.ListaFinal()
        print(len(vendas))
        textofinal = ''
        for venda in vendas:
            if venda[-2] == data:

                index = 0
                index1 = 1
                index2 = 2
                textofinal += f'''
                
    <table border="1">>
        <tr>
            <th>Cliente</th>
            <th>{venda[index]}</th>
        </tr>
        <tr>
            <th>Email</th>
            <th>{venda[index1]}</th>
        </tr>
        <tr>
            <th>Data de Cadastro</th>
            <th>{venda[index2]}</th>
        </tr>
    <tr>'''
                index = 3 
                index1 = 4
                index2 = 5
                index3 = 6
                index4 = 7
                index5 = 8
                cont = 0
                while True:
                    index += cont 
                    index1 += cont
                    index2 += cont
                    index3 += cont
                    index4 += cont
                    index5 += cont

                    texto = f''' <tr>
                                        <th >       </th>
                                        <th >        </th>
                                    </tr>
                                    
                                    <tr>
                                        <th>Produto</th>
                                        <th>{venda[index]}</th>
                                    </tr>
                                    <tr>
                                        <th>Descricao</th>
                                        <th>{venda[index1]}</th>
                                    </tr>
                                    <tr>
                                        <th>Preco de Compra</th>
                                        <th>{venda[index2]}</th>
                                    </tr>
                                    <tr>
                                        <th>Preco de Venda</th>
                                        <th>{venda[index3]}</th>
                                    </tr>
                                    <tr>
                                        <th>Quantidade</th>
                                        <th>{venda[index4]}</th>
                                    </tr>
                                    <tr>
                                        <th>valor da venda</th>
                                        <th>{venda[index5]}</th>
                                    </tr>'''
                    textofinal += texto
                    if ' ' in venda[index5 + 1]:
                        print('entrou aqui', venda[index5 + 1])
                        index = index5 + 1
                        index1 = index5 + 2
                        index2 = index5 + 3
                        index3 = index5 + 4
                        texto = f'''
                                        <th>Preco final da venda</th>
                                        <th>{venda[index]}</th>
                                    </tr>
                                    <tr>
                                        <th>Lucro</th>
                                        <th>{venda[index1]}</th>
                                    </tr>
                                    <tr>
                                        <th>Data da Compra</th>
                                        <th>{venda[index2]}</th>
                                    </tr>
                                    <tr>
                                        <th>codigo da Compra</th>
                                        <th>{venda[index3]}</th>
                                    </tr>
                                    
                                    </table>''' 
                        textofinal += texto
                        break
                    else:
                        cont += 6
                    textofinal += texto        
        textoPDF = estilo + textofinal
        print(textoPDF)
        pdf = pydf.generate_pdf(textoPDF)
        with open('./pooAula/projeto_estoque/relatorioPDF/relatorio_' + data + '.pdf', 'wb') as arquivo:
            arquivo.write(pdf)