# Aula 45 - Aula sobre iteráveis, iteradores, iter() e next() em Python / Lesson on iterables, iterators, iter() and next() in Python
"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> entrega o próximo valor
iter -> transforma um iterável em um iterador / me entregue seu iterador
"""
#=========================================================
# texto = "Fábio".__iter__()
# print(texto)
# # numeros = range(0, 100, 8)

# # Método iter
# texto = iter("Fábio")
# # print(texto.__next__())  # Entrega o primeiro valor
# print(next(texto))

#=========================================================
# for numero in numeros:
#     print(numero)
#=========================================================

# for letra in texto
texto = 'Fábio'  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)