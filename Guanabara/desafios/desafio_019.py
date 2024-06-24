#Um professor quer sortear um de seus quatro alunos para apagar o quadro faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido 

import random as rd

nomes=[]

for i in range(1,4):
    nomes.append(input('Digite o nome do aluno{} e pressione ENTER: '.format(i)))
print('Escolhido: {}'.format(rd.choice(nomes)))
