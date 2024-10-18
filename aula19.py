# Exercício

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro Valor: ')

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)

print(f'A soma dos números é de: {int_primeiro_valor + int_segundo_valor}')
print(f'A subtração dos números é de: {int_primeiro_valor - int_segundo_valor}')

if int_primeiro_valor > int_segundo_valor:
    resultado = f"O primeiro valor: ({int_primeiro_valor}) é maior que o segundo valor: ({int_segundo_valor})."
else:
    resultado = f"O segundo valor: ({int_segundo_valor}) é maior que o primeiro valor: ({int_primeiro_valor})."

print(resultado)


# resultado = primeiro_valor != segundo_valor
# soma = primeiro_valor + segundo_valor

# print(primeiro_valor)
# print(segundo_valor)
# print(soma)
# print(resultado) a