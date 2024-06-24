# > While

numero_sorteado = 15

numero_escolhido = int(input('Informe um número entre 1 e 20: '))

while numero_escolhido != numero_sorteado:
    print('Você errou o numero tente novamente...')

    numero_escolhido = int(input('Informe um numero entre 1 e 20: '))

print('Parabens você acertou!')

contador=0
while contador <= 5:
    print(contador)
    contador +=1
