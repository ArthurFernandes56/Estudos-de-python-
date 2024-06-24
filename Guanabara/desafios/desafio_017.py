#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
import math as mt

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = mt.hypot(cateto_adjacente,cateto_oposto)

print('O triângulo em questão tem {} de hipotenusa'.format(hipotenusa))