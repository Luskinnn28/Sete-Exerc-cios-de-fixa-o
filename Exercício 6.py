6)#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
#de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15
#por Km rodado

print('RESOLUÇÃO DA 16')

quilometragem = float(input('Digite a quantidade de km percorrido pelo carro'))


dias = int(input('Por quantos dias o carro percorreu'))

Valor_Diario_Automovel = 60 * dias

Valor_por_cada_km = quilometragem * 0.15

ValorTotal = Valor_Diario_Automovel + Valor_por_cada_km

print('O valor total a ser pago é de R$ {}'.format(ValorTotal))
