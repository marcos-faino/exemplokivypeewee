class Produto:
    __slots__ = ('__cod',
                 '__descricao',
                 '__marca',
                 '__valor',
                 '__estoque')

    def __init__(self, cod, descricao, marca, valor, estoque=0):
        self.cod = cod
        self.descricao = descricao
        self.marca = marca
        self.valor = valor
        self.__estoque = estoque

    def __str__(self):
        return self.__descricao

    @property
    def cod(self):
        return self.__cod

    @cod.setter
    def cod(self, cod):
        self.__cod = cod

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        if valor>0:
            self.__valor = valor
        else:
            self.__valor = 0.0

    @property
    def estoque(self):
        return self.__estoque

    def aumenta_estoque(self, quant):
        self.__estoque += quant

    def reduz_estoque(self, quant):
        if self.__estoque - quant < self.__estoque:
            self.__estoque = 0
        else:
            self.__estoque -= quant


class Item:
    __slots__ = ('__numero',
                 '__quant',
                 '__produto',)

    def __init__(self, numero, quant, produto):
        self.numero = numero
        self.quant = quant
        self.produto = produto

    def __str__(self):
        return f'{self.__numero} - {self.produto.descricao}'

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def quant(self):
        return self.__quant

    @quant.setter
    def quant(self, quant):
        self.__quant = quant

    @property
    def produto(self):
        return self.__produto

    @produto.setter
    def produto(self, produto):
        if isinstance(produto, Produto):
            self.__produto = produto


class Pedido:
    __slots__ = ('__numero',
                 '__total',
                 '__itensproduto',
                 '__cliente',)

    def __init__(self, numero, itensprod=[], cliente=None):
        self.numero = numero
        self.itensproduto = itensprod
        self.cliente = cliente

    def __str__(self):
        return f'{self.__numero}'

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def total(self):
        return self.__total

    @property
    def itensproduto(self):
        return self.__itensproduto

    @itensproduto.setter
    def itensproduto(self, i):
        if isinstance(i, Item):
            self.add_item(i)
        elif isinstance(i, list):
            for item in i:
                self.add_item(item)

    def add_item(self, item):
        """
        metodo para adicionar um item ao pedido
        :param item: Espera uma instância da classe Item para adicionar ao Pedido
        :return: sem retorno
        """
        self.__itensproduto.append(item)
        self.__total += item.quant * item.produto.valor


class Cliente:
    __slots__ = ('__nome',
                 '__cpf',
                 '__telefone',)

    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
