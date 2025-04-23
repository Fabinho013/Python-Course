nome = 'Fábio Henrique'
altura = 1.76
peso = 63
imc = peso / (altura ** 2) # IMC = peso / (altura x altura)

# Fábio Henrique tem 1.80 de altura,
#pesa 95 quilos e seu IMC é
# 20.33832644628099

print(f"{nome} tem {altura} e pesa {peso} seu IMC é {imc}")
print(nome, 'tem', altura, 'de altura',)
print('pesa', peso, 'quilos e seu imc é',)
print(imc)

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'
#linha_1 = f'{nome} tem {altura:,.2f} de altura' se acrescentar a vírgula antes do ponto, ele coloca a vírgula na conta

print(linha_1)
print(linha_2)
print(linha_3)