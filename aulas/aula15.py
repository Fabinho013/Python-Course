# Aula de como coletar dados utilizando input.
# nome = input('Qual o seu nome? ')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ') #Evitar fazer a conversão do tipo de dado direto na variavel.

int_numero_1 = int(numero_1) #Fazer a conversão do tipo de dado em outra variavel é o ideal para conseguirmos verificar o dado antes de prosseguir.
int_numero_2 = int(numero_2) #Exemplo é colocar uma checagem antes de somar, para validar se não é uma string.

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
# .
