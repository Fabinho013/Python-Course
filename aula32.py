# Solução 2 dos Exercícios - Enunciados / Solution 2 of the Exercises - Statements

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# Solicita um número ao usuário
entrada = input('Digite um número inteiro: ')

# Verifica se a entrada contém apenas dígitos numéricos
if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0  # Verifica se o número é par

    if par_impar:
        print(f'O número {entrada_int} é par')
    else:
        print(f'O número {entrada_int} é ímpar')
else:
    print('Você não digitou um número inteiro.')

# Outra forma de tratar a entrada com try/except
try:
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0

    if par_impar:
        print(f'O número {entrada_int} é par')
    else:
        print(f'O número {entrada_int} é ímpar')
except ValueError:
    print('Você não digitou um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# Solicita a hora ao usuário
entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if 0 <= hora <= 11:
        print('Bom dia')
    elif 12 <= hora <= 17:
        print('Boa tarde')
    elif 18 <= hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except ValueError:
    print('Por favor, digite apenas números inteiros.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Solicita o nome do usuário
nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)

# Verifica o tamanho do nome
if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif 5 <= tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')

# Aula sobre soluções de exercícios básicos em Python /
# Lesson on basic Python exercise solutions
