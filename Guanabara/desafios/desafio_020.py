# o mesmo professor do desafio anterio quer sortear a ordem de apresentção de trabalhos dos alunos faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random as rd

nomes = []

for i in range(1,5):
    nomes.append(input('Digite o nome do aluno {}: '.format(i)))

rd.shuffle(nomes)

print('\n\nOrdem de quem deve apagar o quadro:\n')
for i in range(0, len(nomes)):
    print('{}-{}'.format(i+1,nomes[i]))
print('\n\n')