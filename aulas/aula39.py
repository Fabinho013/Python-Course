nome = 'Fábio Henrique'
indice = 0
novo_nome = ''

while indice < len(nome):
  letra = nome[indice]
  novo_nome += f'*{letra}'
  indice += 1

novo_nome += '*'  # Aqui é onde você adiciona o * final
print(novo_nome)
