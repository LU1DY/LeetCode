s = "["


def validParentheses(s):
    lista = []
    abertura = ["(", "[", "{"]
    busca = ["()", "[]", "{}"]

    if s[0] in abertura:
        for i in s:
            if i in abertura:
                lista.append(i)
            else:
                if len(lista) > 0:
                    if lista[-1] + i in busca:
                        lista.pop(len(lista) - 1)
                    else:
                        return False
                else:
                    return False
        return len(lista) == 0
    else:
        return False


print(validParenteses(s))
