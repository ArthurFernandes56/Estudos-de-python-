def media(idades):
    soma=0
    media=0
    for n in idades:
        soma +=n
        media=soma/len(idades)
    print(soma)
    print(len(idades),idades)    
    return media

idades=[]
num =0
while True:
    
    if num >= 0:
        num=int(input())
        idades.append(num)
    else:
        break
print(media(idades))