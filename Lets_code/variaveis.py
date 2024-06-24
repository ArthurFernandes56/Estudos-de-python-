# >   VARIÁVEIS 
"""
cls - limpa o terminal
"""

# 1. VARIÁVEIS

nome= 'Arthur Fernandes' # CRIANDO VARIÁVEIS 

print(nome) 

idade = 18 

print(idade)

altura = 1.81

print(altura)

estudando = True

print(estudando)

print(type(nome))
print(type(altura))
print(type(idade))
print(type(estudando))

linguagem = input('Qual linguagem de programação você esta estudando?')

print('Oi {}! A linguagem que você esta estudando é {}'.format(nome,linguagem))