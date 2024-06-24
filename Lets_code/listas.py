# > LISTAS

lista = []
lista = list()
lista = [26, 'arthur', False]
lista_de_listas = [['joão','maria'],[12,25],[False,True]]

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]
print(lista[0:3])
print(lista[2:6:2])
print('_'*10)
# > Interação com FOR

# 1. Utilizando os próprios elemesntos da lista 

for elemento in lista:
    print(elemento)

# 2. Utilizando os indices 

print('Comprimento da lista: ', len(lista))

for i in range(len(lista)):
    print(lista[i])

# > MÉTODOS DE LISTAS

lista = [1, 3, 12, 8, 2]

# append

print('Antes do append:',lista)
lista.append(3)
print('Depois do append:',lista)

# insert

print('Antes do insert:', lista)
lista.insert(2,10)
print('Depois do insert:', lista)

# extend

lista2 = [1,2,3]

lista.extend(lista2)

print('Depois do extend: ',lista)

# pop

lista.pop()

print('Lista após o pop: ',lista)

# remove

lista.remove(3)

print('Depois do remove: ',lista)

#count

print('Quantidade de 2 na lista:', lista.count(2))

# index 

print('Indice do elemento 12:', lista.index(12))

# sort 

lista.sort(reverse=True)

print(lista)


# len

print(len(lista))

# sum

print(sum(lista))

# max

print('Maior elemento da lista: ',max(lista))

# min

print('Menor elemento da lista: ',min(lista))