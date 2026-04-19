"""
CONSTANTES = "Variaveis" que não mudam
Letras Maiusculas
Muitas, condições no mesmo if(ruim)
<- Contagem de complexidade (ruim)
"""

velocidade = 61 # velocidade atual do carro
local_carro = 101 # localem que o carro está na estrada

RADAR_1 = 60 # velocidade maxima doradar 1
LOCAL_1 = 90 # local.onde.o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')

# ==========================================================
# AULA 30 — LÓGICA COM IF, VARIÁVEIS E CÓDIGO LEGÍVEL
# ==========================================================

# 1️⃣ Objetivo da aula

# Criar uma lógica para identificar:

# - Se o carro passou da velocidade do radar
# - Se o carro passou pelo local do radar
# - Se o carro foi multado

# A multa só acontece quando DUAS condições são verdadeiras:
# velocidade acima do limite
# carro dentro da área de alcance do radar

# ----------------------------------------------------------

# 2️⃣ Uso de constantes

# O professor usa constantes para valores fixos.

# CONSTANTES geralmente são escritas em
# LETRAS MAIÚSCULAS.

# Isso indica que o valor não deve mudar
# durante a execução do programa.

# Exemplo:

# RADAR_1
# LOCAL_1
# RADAR_RANGE

# ----------------------------------------------------------

# 3️⃣ Variáveis do problema

# velocidade
# velocidade atual do carro

# local_carro
# posição do carro na estrada

# RADAR_1
# velocidade máxima permitida

# LOCAL_1
# posição do radar na estrada

# RADAR_RANGE
# área onde o radar consegue detectar o carro

# ----------------------------------------------------------

# 4️⃣ Primeira verificação
# Se o carro passou da velocidade permitida

# velocidade > RADAR_1

# Isso retorna True ou False.

# ----------------------------------------------------------

# 5️⃣ Segunda verificação
# Se o carro passou pelo radar

# O carro precisa estar dentro do alcance do radar.

# Ou seja:

# LOCAL_1 - RADAR_RANGE
# até
# LOCAL_1 + RADAR_RANGE

# Isso cria um intervalo.

# Exemplo conceitual:

# radar = 100
# alcance = 1

# área do radar:
# 99 até 101

# ----------------------------------------------------------

# 6️⃣ Verificando se o carro está dentro do radar

# condição usada:

# local_carro >= (LOCAL_1 - RADAR_RANGE)
# and
# local_carro <= (LOCAL_1 + RADAR_RANGE)

# Isso verifica se o carro está dentro
# da área de atuação do radar.

# ----------------------------------------------------------

# 7️⃣ Verificando se o carro foi multado

# Para ser multado:

# carro precisa estar acima da velocidade
# E
# dentro do radar

# condição:

# carro_multado_radar_1 =
# carro_passou_radar_1 and vel_carro_pass_radar_1

# ----------------------------------------------------------

# 8️⃣ Melhorando a legibilidade do código

# Em vez de colocar tudo dentro do IF,
# o professor separa as condições
# em variáveis.

# Isso deixa o código:

# mais fácil de ler
# mais fácil de manter
# mais fácil de modificar

# ----------------------------------------------------------

# 9️⃣ Problema de colocar tudo no IF

# Exemplo ruim:

# if velocidade > RADAR_1 and local_carro >= ... and ...

# Isso deixa o código:

# difícil de entender
# difícil de manter
# difícil de debugar

# ----------------------------------------------------------

# 🔟 Uso de variáveis intermediárias

# Separar condições em variáveis
# deixa o código mais claro.

# Exemplo conceitual:

# vel_carro_pass_radar_1
# carro_passou_radar_1
# carro_multado_radar_1

# Agora cada variável representa
# um significado lógico.

# ----------------------------------------------------------

# 1️⃣1️⃣ Complexidade de código

# Muitos operadores dentro de um IF
# aumentam a complexidade do código.

# Código complexo é:

# difícil de entender
# difícil de manter
# difícil de testar

# ----------------------------------------------------------

# 1️⃣2️⃣ Boa prática

# Criar variáveis com nomes claros
# melhora a leitura do código.

# Exemplo:

# carro_passou_radar_1
# carro_multado_radar_1

# Assim qualquer pessoa consegue entender
# a lógica rapidamente.

# ----------------------------------------------------------

# 1️⃣3️⃣ Conclusão

# Nesta aula aprendemos:

# usar constantes
# separar lógica em variáveis
# melhorar a legibilidade do código
# reduzir complexidade nos IFs

# Código mais legível é essencial
# para trabalhar em projetos reais.