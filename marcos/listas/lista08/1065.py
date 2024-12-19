
lista_numeros=[]
for i in range(5):
    numeros=int(input())
    lista_numeros.append(numeros)
cont=0
for i in lista_numeros:
    if i % 2==0:
        cont+=1
    
print("{} valores pares".format(cont))    