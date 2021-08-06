#2)Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
#de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

print("RESOLUÇÃO DA 12")

largura = float(input("Meça e diga qual é a largura da parede(em Metros)"))

altura = float(input("Meça e diga qual é a Altura da parede (em Metros)"))

area = (largura * altura)

tinta = area/2

areaObtida = print('A área da parede foi de {} metros quadrados'.format(area))

qtdTinta = print('e a quantidade necessária de tinta foi de {} litros'.format(tinta))

print('------------------------------------------------------------------------------------')
