#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta_la, sabendo que cada litro de tinta pinta uma area de 2m^2

altura= float(input('Digite o valor da altura da parede em metros: '))
largura= float(input('Digite o valor da largura da parede em metros: '))
area=altura*largura
litragem_nescessaria = area/2

print('Será nescessario que se tenha {} litros de tinta para pintar a parede toda'.format(litragem_nescessaria))