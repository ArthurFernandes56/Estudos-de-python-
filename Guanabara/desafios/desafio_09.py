#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

num = int(input('Digite um número inteiro: '))
print('======Tabuada do {}======\n\n'.format(num))
for i in range(0,11):
    pro = num * i
    print('{} X {} = {}          {} : {} = {}\n'.format(num,i,pro,pro,num,i))