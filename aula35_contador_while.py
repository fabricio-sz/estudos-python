"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 10:
    contador = contador + 1
    print(contador)

print('Acabou')

# ==========================================================
# AULA 35 — CONTADOR COM WHILE
# ==========================================================

# O while executa um bloco de código repetidamente
# enquanto uma condição for verdadeira.


# ----------------------------------------------------------
# CONTADOR
# ----------------------------------------------------------

# Um contador é uma variável usada para controlar
# quantas vezes um loop executa.

# Exemplo conceitual

# contador começa em 0

# enquanto contador for menor ou igual a 10
# execute o bloco


# ----------------------------------------------------------
# FUNCIONAMENTO DO CONTADOR
# ----------------------------------------------------------

# 1️⃣ cria variável contador

# contador = 0


# 2️⃣ while verifica condição

# enquanto contador <= limite


# 3️⃣ executa bloco do while


# 4️⃣ incrementa contador

# contador = contador + 1


# 5️⃣ volta para o início do while


# ----------------------------------------------------------
# IMPORTANTE
# ----------------------------------------------------------

# Se o contador não for atualizado,
# o loop vira infinito.

# exemplo errado

# contador = 0
# while contador <= 10:
#     print(contador)

# contador nunca muda
# loop infinito


# ----------------------------------------------------------
# INCREMENTO
# ----------------------------------------------------------

# incremento significa aumentar o valor
# do contador.

# exemplo

# contador = contador + 1


# isso faz o contador crescer


# ----------------------------------------------------------
# CONTROLE DE PARADA
# ----------------------------------------------------------

# quando a condição do while se torna falsa
# o loop termina.

# exemplo

# contador = 10
# while contador <= 10
# executa uma última vez

# depois contador vira 11
# condição fica falsa
# loop termina


# ----------------------------------------------------------
# IDEIA PRINCIPAL
# ----------------------------------------------------------

# while + contador
# é usado para repetir ações várias vezes

# muito usado para:

# contagem
# jogos
# menus
# validação de dados