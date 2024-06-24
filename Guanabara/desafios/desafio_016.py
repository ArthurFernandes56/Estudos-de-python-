#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
import math as mt
num = float(input('Escreva um numero real qualquer: '))


print('A parte inteira do numero {} é {}'.format(num, mt.trunc(num)))