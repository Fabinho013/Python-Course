# Introdução ao try e except para capturar erros (exceptions) / Introduction to try and except for catching errors (exceptions)
# try -> tentar executar um código
# except -> ocorreu algum erro ao tentar executar

# Exemplo de erro:
# print(1234)
# print(456)
# int('a')  # Isso gera um erro porque 'a' não pode ser convertido em inteiro

# Solicita ao usuário um número
numero_str = input("Vou dobrar o número que você digitar: ")
# print(numero_str.isdigit())  # Verifica se é número (somente dígitos)

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)  # Tenta converter para número float
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')  # Mensagem de erro caso a conversão falhe

# Alternativa com isdigit() (somente para inteiros positivos):
# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')
# .
