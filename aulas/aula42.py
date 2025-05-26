# Aula 42 - Aula sobre contagem de caracteres e identificação da letra mais frequente em uma string / Lesson on character counting and identifying the most frequent letter in a string
frase = "O python é uma linguagem de programação "\
    "multiparadigma. "\
    "Python foi criado por Guido van Rossum e lançado em 1991."

# print(frase.count('a'))  # Conta quantas vezes a letra 'a' aparece na frase
i = 0
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue
    
    quantas_vezes_atual = frase.count(letra_atual)
    
    if quantas_vezes_atual > qtd_apareceu_mais_vezes:
        qtd_apareceu_mais_vezes = quantas_vezes_atual
        letra_que_apareceu_mais_vezes = letra_atual
        
    i += 1
    
print(f'A letra que apareceu mais vezes foi "{letra_que_apareceu_mais_vezes}" e apareceu {qtd_apareceu_mais_vezes} vezes.')
# print(frase.count('a', 0, 10))  # Conta quantas vezes a letra 'a  ' aparece na frase, do índice 0 ao 10
