# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math as mt

angulo = float(input('Digite o valor do angulo que deseja saber o cosseno, seno e tangente: '))
cos = mt.cos(mt.radians(angulo))
seno = mt.sin(mt.radians(angulo))
tan =  mt.tan(mt.radians(angulo))


print('Analisando um angulo de {}° temos:\n\nValor do seno: {:.2f}\nValor do cosseno: {:.2f}\nValor da tangente: {:.2f}\n'.format(angulo,seno,cos,tan))