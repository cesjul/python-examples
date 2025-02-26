from abc import ABC, abstractmethod
import datetime
import json

class Banco:
    def __init__(self, banco):
        self._banco = banco
        self._banco_lista_agencia = []
        self._banco_lista_conta = []
        self._banco_lista_clientes = []
        self._banco_dict_cliente_dados = {}
        self.__banco_lista_clientes_inner = []
        self._banco_lista_dados_gerais = []
        

    @property
    def nome_banco(self):
        return self._banco
    
    @nome_banco.setter
    def nome_banco(self, valor):
        self._banco = valor
    
    def vincula_agencia(self, agencia):
        self._banco_lista_agencia.append(agencia)
        
    def vincula_conta(self, conta):
        self._banco_lista_conta.append(conta.nome_conta)
       
    def vincula_cliente(self, cliente_nome, cliente):
        self._banco_lista_clientes.append(cliente_nome)
        self.__banco_lista_clientes_inner.append(cliente)
        
    def exibir_dados_conta(self):
        return self._banco_dict_cliente_dados

    def auth(self, cliente, agencia, conta):
        autenticacao = agencia == cliente.agencia \
                       and conta == cliente.client_conta \
                       and cliente in self.__banco_lista_clientes_inner
        if autenticacao:
            return True
        return False


class Agencia:
    def __init__(self, agencia):
        self._agencia = agencia
        self._banco_agencia = None
        self._agencia_contas = []

    @property
    def num_agencia(self):
        return self._agencia

    @num_agencia.setter
    def num_agencia(self, valor):
        self._agencia = valor
    
    @property
    def banco_da_agencia(self):
        return self._banco_agencia

    @banco_da_agencia.setter
    def banco_da_agencia(self, banco: Banco):
        self._banco_agencia = banco
        self._banco_agencia.vincula_agencia(self._agencia)

    def contas_agencia(self, conta):
        self._agencia_contas.append(conta.nome_conta)
        

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    @property
    def nome_(self):
        return self._nome
    
    @nome_.setter
    def nome_(self, nome_atual):
        self._nome = nome_atual
    
    @property
    def idade_(self):
        return self._idade
    
    @idade_.setter
    def idade_(self, valor_idade):
        self._idade = valor_idade

class Client(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._banco = None
        self.client_conta = None
        self.agencia = None

    def vincula_o_cliente_ao_banco(self, banco: Banco):
        self._banco = banco
        self._banco.vincula_cliente(self._nome, self)
    
    def vincula_o_cliente_a_conta(self, conta):
        self.client_conta = conta
        self.client_conta.receber_cliente(self)

    def recebe_a_agencia_do_cliente(self, agencia):
        self.agencia = agencia

class Conta(ABC):
    def __init__(self, conta):
        self._conta = conta
        self._saldo = 0
        self._banco = None
        self.client = None
        self._agencia_conta = None
        self.extrato_ = []

    @property
    def nome_conta(self):
        return self._conta
        
    @nome_conta.setter
    def nome_conta(self, valor):
        self._conta = valor
    
    def depositar(self, valor: int | float):
        self._saldo += valor
        self.extrato_.append(f'Deposito: Saldo anterior: {self._saldo - valor:,.2f},' 
                              f' Valor: {valor:,.2f}, Saldo Atual: {self._saldo:,.2f}'
                              f' data e hora : {datetime.date.today()}'
                            f' {datetime.datetime.now().strftime("%H:%M:%S")}')
    @property
    def vincula_a_conta_a_agencia(self):
        return self._agencia_conta
    
    @vincula_a_conta_a_agencia.setter
    def vincula_a_conta_a_agencia(self, agencia: Agencia):
        self._agencia_conta = agencia

    @abstractmethod
    def sacar(self, valor, agencia, nome):...
    
    def criar_conta_banco(self, banco: Banco):
        self._banco = banco
        self._banco.vincula_conta(self)
    
    def receber_cliente(self, cliente: Client):
        self.client = cliente
        self.client.recebe_a_agencia_do_cliente(self.vincula_a_conta_a_agencia)
    
    def exibir_saldo(self):
        return f'O saldo da conta: {self._conta} é {self._saldo} R$'

    def extrato(self):
        return self.extrato_
    

class ContaCorrente(Conta):
    def __init__(self, conta, limite=200):
        super().__init__(conta)
        self.limite = limite

    def sacar(self, valor, cliente, agencia, conta):
        
        validacao = banco.auth(cliente, agencia, conta)

        if validacao:
            if self._saldo >= -200 and valor <= self._saldo + self.limite:
                self._saldo -= valor
            

                self.extrato_.append(f'Saque: Saldo anterior: {self._saldo + valor:,.2f},'
                                    f' Valor: {valor:,.2f}, Saldo Atual: {self._saldo:,.2f},'
                                    f' data e hora :'
                                    f' {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
                
                print(f'Saque de {valor} autorizado')
                return f'Saque de {valor} autorizado'
            else:
                print('Saldo Insuficiente')
        else:    
            print('Credenciais nao validadas')
            return 'Operação não autorizada!'

class ContaPoupanca(Conta):
    def sacar(self, valor, cliente, agencia, conta):

        validacao = banco.auth(cliente, agencia, conta)

        if validacao:
        
            if valor <= self._saldo and self._saldo > 0:
                self._saldo -= valor
            else:
                return f'Saldo insuficiente, ({__class__.__name__})'
            
            self.extrato_.append(f'Saque: Saldo anterior: {self._saldo + valor:,.2f},'
                                f' Valor: {valor:,.2f}, Saldo Atual: {self._saldo:,.2f},'
                                f' data e hora : {datetime.date.today()}'
                            f' {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
            return f'Saque de {valor} autorizado'

###############################################################################
banco = Banco('Itau')
banco1 = Banco('Nu')
agencia = Agencia('5408')
agencia1 = Agencia('1101')
cliente = Client('Nome', 21)
cliente1 = Client('Nome1', 19)
cliente2 = Client('IOwfw', 30)
conta = ContaCorrente('Conta do Nome')
conta1 = ContaCorrente('Conta do Nome1')
conta2 = ContaCorrente('Conta do IOwfw')
agencia1.banco_da_agencia = banco1
agencia.banco_da_agencia = banco
cliente.vincula_o_cliente_ao_banco(banco)
cliente1.vincula_o_cliente_ao_banco(banco)
conta.vincula_a_conta_a_agencia = agencia
conta1.vincula_a_conta_a_agencia = agencia
cliente.vincula_o_cliente_a_conta(conta)
cliente1.vincula_o_cliente_a_conta(conta1)
conta.criar_conta_banco(banco)
conta1.criar_conta_banco(banco)
conta.limite = 500
conta.depositar(10000.25)
conta.sacar(10000.25, cliente, agencia, conta)
conta.sacar(499.99, cliente2, agencia1, conta2)
print(*list(conta.extrato()), sep='\n')
