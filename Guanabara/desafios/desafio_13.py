#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento 

salario_atual = float(input('Você recebeu um aumento!!\nParabéns!!!\nInforme seu salario atual para que possamos acrescer e lhe informar seu novo salario: '))

salario_atual*=1.15

print('Seu novo salario é de R$ {:.2f}.'.format(salario_atual))