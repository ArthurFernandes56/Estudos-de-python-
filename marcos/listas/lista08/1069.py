"""casos=int(input())
for i in range(casos):
    teste=input()
    cont1=0
    cont2=0
    
    for j in range(len(teste)):
        if teste[j] == "<":
            
            cont1+=1
        elif teste[j] == ">":
            
            cont2+=1
        
    
    if cont1>cont2:
        for k in range(cont1):
              
            if cont1==cont2:
                continue
            cont1-=1
    if cont1<cont2:
        for k in range(cont2):
               
            
            if cont1==cont2:
                continue
            cont1-=1    
    print(cont1)    
    """

casos = int(input())

for i in range(casos):
    teste = input()
    cont1 = 0
    diamantes = 0
    
    for char in teste:
        if char == "<":
            cont1 += 1
        elif char == ">":
            if cont1 > 0:
                cont1 -= 1
                diamantes += 1
    
    print(diamantes)
