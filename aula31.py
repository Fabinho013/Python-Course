# Flags, is, is not e None / Flags, is, is not, and None

# Flag (Bandeira) - Marcar um local no código
# None = Representa a ausência de um valor
# is e is not = Verifica se dois objetos possuem a mesma identidade na memória
# id = Retorna a identidade (endereço de memória) de um objeto

# Definição de uma condição
condicao = True
passou_no_if = None  # Inicialmente, não sabemos se a condição será atendida

# Estrutura condicional
if condicao:
    passou_no_if = True  # Marca que o código passou pelo if
    print('Faça algo')
else:
    print('Não faça algo.')

# Verifica se a variável ainda é None
if passou_no_if is None:
    print('Não passou no if')

# Verifica se a variável foi alterada (ou seja, passou pelo if)
if passou_no_if is not None:
    print('Passou no if')

# Testes comentados para verificar valores e identidades
# print(passou_no_if, passou_no_if is None)
# print(passou_no_if, passou_no_if is not None)

# Aula sobre Flags, is, is not e None / 
# Lesson on Flags, is, is not, and None
