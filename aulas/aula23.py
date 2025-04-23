# Operadores in e not in
# String são interáveis
#  0 1 2 3 4 5 6
#  F á b i n h o
# -7-6-5-4-3-2-1

nome = 'Fábinho'
# print(nome[2])
# print(nome[-5])
print('á' in nome)
print(10 * '-')
print('á' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}') 
# .
