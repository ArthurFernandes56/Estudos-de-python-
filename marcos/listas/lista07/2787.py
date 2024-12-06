def casa(x,y):
    """

    Verifica se ooooooo a casa é branca ou preta
    :param x: número de linhas
    :param y: número de colunas
    :return: Retorna o valor que determina se a casa é branca ou preta 
    """
    if ((x % 2==0 and y % 2==0)or (x % 2!=0 and y % 2!=0)):
        return(print(1))
    else:
        return(print(0))


x=int(input())
y=int(input())

casa(x,y)