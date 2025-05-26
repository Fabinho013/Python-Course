# Aula 41 - Aula sobre estrutura while/else e comportamento com break / Lesson on while/else structure and behavior with break
""" while/else"""

# ==========================================================================
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]
    
    if letra == ' ':
        break
#    break  # Interrompe o loop com break
    # Se o break for removido, o loop continuará até o final da string
    
    print(letra)
    i += 1
else:
    print('O else foi executado.')
print('Fora do While')
# ==========================================================================  
# O else do while é executado quando o while termina sem interrupção
# Se o while for interrompido com um break, o else não é executado
# ==========================================================================
# The else of the while is executed when the while ends without interruption
# If the while is interrupted with a break, the else is not executed