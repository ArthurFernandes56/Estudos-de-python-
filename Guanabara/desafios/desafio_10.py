#Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar 

# Considere US$1.00 = 3,27

carteira =float(input('Informe quanto você tem na casteira (em reais): '))

dolar = carteira//3.27
print('Você pode comprar {} dolares com essa quantia de dinheiro'.format(dolar))