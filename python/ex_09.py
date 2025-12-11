x = 12


def isPalindrome(x):
        n_int = x
        int_invertido = []
        while n_int > 0:
            n = n_int % 10
            int_invertido.append(n)
            n_int //= 10

        tamanho = len(int_invertido)
        x_invertido = 0
        for i, item in enumerate(int_invertido):
            x_invertido += item * (10 ** (tamanho - 1))
            tamanho -= 1

        return x == x_invertido


print(isPalindrome(x))
