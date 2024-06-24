#Crie um algoritmo que leia um número e mostre o seu dobro triplo e raiz quadrada

num = int(input('Digite um numero inteiro: '))
num_dobro = num*2
num_triplo = num*3 
num_raiz = num **(1/2)
print('Com base no numero informado temos:\nSeu dobro: {}\nSeu triplo:{}\nSua raiz quadrada:{}'.format(num_dobro,num_triplo,num_raiz))