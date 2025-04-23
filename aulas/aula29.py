# Variáveis, Constantes e Complexidade de Código / Variables, Constants, and Code Complexity

# Definição de variáveis e constantes
velocidade = 61  # Velocidade atual do carro
local_carro = 100  # Localização atual do carro na estrada

# Definição de constantes (valores fixos que não devem mudar)
RADAR_1 = 60  # Velocidade máxima permitida no radar 1
LOCAL_1 = 100  # Localização do radar 1 na estrada
RADAR_RANGE = 1  # Alcance do radar 1 (margem de erro, ou área de monitoramento)

# Verifica se o carro ultrapassou a velocidade permitida no radar 1
velocidade_carro_passou_radar_1 = velocidade > RADAR_1  # True se a velocidade for maior que a permitida

# Verifica se o carro está dentro da área de alcance do radar 1
carro_no_alcance_do_radar = LOCAL_1 - RADAR_RANGE <= local_carro <= LOCAL_1 + RADAR_RANGE

# Exibe mensagem se o carro ultrapassou a velocidade máxima do radar
if velocidade_carro_passou_radar_1:
    print('Velocidade do carro passou do radar 1')

# Se o carro ultrapassou a velocidade e está dentro do alcance do radar, ele será multado
if velocidade_carro_passou_radar_1 and carro_no_alcance_do_radar:
    print('Carro multado em radar 1')

# Aula sobre variáveis, constantes e complexidade de código / 
# Lesson on variables, constants, and code complexity
# .

