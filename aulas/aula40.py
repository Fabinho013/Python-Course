# """Calculadora com while/Calculator with while"""
# Aula 40 - Aula sobre construção de calculadora com while, validação de números, operadores e laço de repetição com opção de saída 
# / Lesson on building a calculator with while loop, number and operator validation, and exit condition with user input


#=======================================================================
# while True:
#     sair = input("Deseja sair? [s]im:")
#     sair = sair.lower()
#     sair =sair.startswitch("s")
#     print(sair)

#=======================================================================
# # Otimizando o código/Optimizing the code
# while True:
#     sair = input("Deseja sair? [s]im:").lower().startswith("s")
#     print(sair)

#=======================================================================
# while True:
#     print('nummmmmm')
#     ##############
#     sair = input("Deseja sair? [s]im:").lower().startswith("s")

#     if sair is True:
#         break

#=======================================================================
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador  (+, -, *, /): ')
    
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou mais números são inválidos!')
        continue
    operadores_permitidos = ['+', '-', '*', '/']
    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue
    
    if len(operador) > 1:
        print('Operador inválido!')
        continue
    print('Realizando sua conta. Confira o resultado abaixo:')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = {num_1_float + num_2_float}')
    elif operador == '-':
        print(f'{num_1_float} + {num_2_float} = {num_1_float + num_2_float}')
    elif operador == '*':
        print(f'{num_1_float} + {num_2_float} = {num_1_float + num_2_float}')
    elif operador == '/':
        print(f'{num_1_float} + {num_2_float} = {num_1_float + num_2_float}')
    else:
        print('Nunca deveria chegar aqui!')
    
    
    sair = input("Deseja sair? [s]im:").lower().startswith("s")

    if sair is True:
        break
