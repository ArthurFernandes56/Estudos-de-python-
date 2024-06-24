#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

vMetros = float(input('Infome o valor em metros: \n'))

vCent = vMetros*100

vMili = vMetros*1000

print('{} metros é igual a:\n-Centimetros: {} \n-Milimetros: {}'.format(vMetros,vCent,vMili))