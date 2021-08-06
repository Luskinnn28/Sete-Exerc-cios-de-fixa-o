#3. Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.


print('RESOLUÇÃO DA 3')

Preco = float (input("Digite aqui o preço do produto"))

desconto = Preco -(Preco * 5 / 100)

print('O preço inicial do pruduto era de R$ {}. Com o desconto, o produto fica R$ {}'.format(Preco, desconto))
