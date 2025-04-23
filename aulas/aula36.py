contador = 10
print("Valor inicial:", contador)

contador += 5  # contador = contador + 5 → 10 + 5 = 15
print("Depois de += 5:", contador)

contador -= 3  # contador = contador - 3 → 15 - 3 = 12
print("Depois de -= 3:", contador)

contador *= 2  # contador = contador * 2 → 12 * 2 = 24
print("Depois de *= 2:", contador)

contador /= 4  # contador = contador / 4 → 24 / 4 = 6.0
print("Depois de /= 4:", contador)

contador %= 4  # contador = contador % 4 → 6.0 % 4 = 2.0
print("Depois de %= 4:", contador)

# A variável contador vai sendo atualizada em cada linha.

# Depois do operador /=, o tipo do valor vira float (número com casa decimal), mesmo que o número seja "redondo".

# Esses operadores tornam o código mais limpo e fácil de ler, especialmente quando a operação é sobre a mesma variável.

# O mesmo vale para os operadores de comparação, como ==, !=, <, >, <= e >=. Eles também podem ser usados com +=, -=, *=, /= e %=.