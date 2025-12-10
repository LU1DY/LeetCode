s = "aab"

def find_longest_subs(s):
    sequencia = []
    sequencias = []
    for i, item in enumerate(s):
        if item in sequencia:
                sequencias.append(sequencia)
                indice = sequencia.index(item)
                indice += 1
                sequencia = sequencia[indice:]
                sequencia.append(item)
        else:
            sequencia.append(item)
    sequencias.append(sequencia)

    maior = 0
    for i in sequencias:
        if len(i) > maior:
            maior = len(i)

    return maior


print(find_longest_subs(s))