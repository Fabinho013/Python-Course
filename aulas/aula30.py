# id - A identidade do valor na memória / id - The identity of the value in memory

# Flag (Bandeira) - Marcar um local
# None = Representa a ausência de um valor
# is e is not = Verifica se dois objetos possuem a mesma identidade na memória
# id = Retorna a identidade (endereço de memória) de um objeto

# Exemplo de identidade na memória
v1 = 'a'
v2 = 'a'

# Como strings são imutáveis, Python reutiliza o mesmo endereço de memória para valores iguais
print(id(v1))  # Exibe o ID do valor armazenado em v1
print(id(v2))  # Exibe o ID do valor armazenado em v2 (deve ser o mesmo que v1)

# Exemplo de uso de uma flag (bandeira) para controle de fluxo
condicao = False

if condicao:
    print('Faça algo')
else:
    print('Não faça algo')

# Aula sobre identidade de valores na memória usando id / 
# Lesson on value identity in memory using id
# .

