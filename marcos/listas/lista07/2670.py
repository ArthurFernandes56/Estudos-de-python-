def imprimir_resposta(tempo):
    """
    Função responsável por imprimir o tempo.

    tempo (int): O tempo total.

    Returns: não tem.
        
    """
    print(tempo*2)



A1 = int(input())
A2 = int(input())
A3 = int(input())

tempo_1 = A2 * 1 + A3 * 2
tempo_2 = A1 * 1 + A3 * 1
tempo_3 = A1 * 2 + A2 * 1

tempoMin = min(tempo_1,tempo_2,tempo_3)



imprimir_resposta(tempoMin)


