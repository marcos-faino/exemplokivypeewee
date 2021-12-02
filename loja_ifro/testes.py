from model import *

p1 = Produto(1, 'Arroz', 'Branco', 27.98)
p2 = Produto(2, 'Feijão', 'Preto', 7.52)
p3 = Produto(3, 'Macarrão', 'Amarelo', 3.54)

cliente1 = Cliente('João da Silva', '123.456.789-00', '(69)9 9999-0000')

pedido1 = Pedido(numero=1, cliente=cliente1)

item1 = Item(1, 5, p3)
#pedido1.itens = item1
item2 = Item(2, 1, p2)
#pedido1.itens = item2
item3 = Item(3, 2, p1)
#pedido1.itens = item3
item4 = Item(4, 12, p1)
#pedido1.itens = item4
item5 = Item(5, 6, p2)
#pedido1.itens = item5
item6 = Item(6, 8, p3)
#pedido1.itens = item6
item7 = Item(7, 2, p3)
#pedido1.itens = item7
item8 = Item(8, 2, p2)
#pedido1.itens = item8

# pedido1.itens = [item1, item2, item3, item4, item5, item6, item7, item8]

print(pedido1.itensproduto)