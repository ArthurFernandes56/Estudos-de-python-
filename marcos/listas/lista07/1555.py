def rafael(x,y):

    """
    
    Calcula a função de Rafael
    :param x: primeiro numero
    :param y: segundo numero
    :return: Retorna o resultado da função escolhida por rafael
    """
    resultR = pow(3*x,2) + pow(y,2)
    return resultR

def beto(x,y):

    """ 

    Calcula a função de Beto
    :param x: primeiro numero
    :param y: segundo numero
    :return: Retorna o resultado da função escolhida por Beto
    """
    resultB = 2*(pow(x,2)) + pow(5*y,2)
    return resultB
def carlos(x,y):

    """

    Calcula a função de Beto
    :param x: primeiro numero
    :param y: segundo numero
    :return: Retorna o resultado da função escolhida por Beto
    """
    resultC = -100*x + pow(y,3)
    return resultC

num=int(input())

for i in range(num):
   z= input()
   x,y= map(int,z.split())
   if (rafael(x, y)>beto(x,y) and rafael(x,y)>carlos(x,y)):
       print("Rafael ganhou")

   if (beto(x, y)>rafael(x,y) and beto(x,y)>carlos(x,y)):
       print("Beto ganhou")

   if (carlos(x, y)>beto(x,y) and carlos(x,y)>rafael(x,y)):
       print("Carlos ganhou")   


help(rafael)
help(carlos)
help(beto)