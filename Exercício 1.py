#1) Faça um programa que insira um valor em reais, e faça ele converter o valor para dólar,mostrando quantos
# dólares podem ser comprados com aquela quantia. (Valor para ser usado do dólar no exercício: 5.30)

print('RESOLUÇÃO DA 1')

ValorEscolhido = float(input("Digite o valor que você quer converter para dolar"))

DolarAtual = 5.30

valorConvertido = (ValorEscolhido * DolarAtual)

print("R${} equivale a {} Dolares".format(ValorEscolhido, valorConvertido))
print('----------------------------------------------------------------------')
