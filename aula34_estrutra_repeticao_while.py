"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')


# ==========================================================
# AULA 34 — ESTRUTURA DE REPETIÇÃO WHILE
# ==========================================================

# WHILE significa "ENQUANTO".

# Ele executa um bloco de código repetidamente
# enquanto uma condição for verdadeira.

# Estrutura lógica:

# enquanto condição for verdadeira:
#     execute o bloco de código


# ----------------------------------------------------------
# LOOP INFINITO
# ----------------------------------------------------------

# Se a condição nunca se tornar falsa,
# o programa ficará executando para sempre.

# Exemplo conceitual:

# while True:
#     executar algo


# Isso é chamado de:
# LOOP INFINITO


# ----------------------------------------------------------
# FLUXO DO WHILE
# ----------------------------------------------------------

# 1️⃣ Python verifica a condição

# 2️⃣ Se for True
# executa o bloco

# 3️⃣ Quando termina o bloco
# volta para o início

# 4️⃣ Verifica a condição novamente


# ----------------------------------------------------------
# COMO PARAR UM WHILE
# ----------------------------------------------------------

# Existem duas formas principais:

# 1️⃣ Fazer a condição virar False

# exemplo conceitual

# while numero != 10


# 2️⃣ Usar a palavra BREAK


# ----------------------------------------------------------
# BREAK
# ----------------------------------------------------------

# break interrompe imediatamente o laço.

# Ele sai do loop mais próximo.

# Exemplo conceitual

# while True:
#     if condição:
#         break


# ----------------------------------------------------------
# USO COM INPUT
# ----------------------------------------------------------

# loops são muito usados com input

# porque o programa pode continuar pedindo
# dados até uma condição acontecer


# ----------------------------------------------------------
# EXEMPLO DE USO
# ----------------------------------------------------------

# pedir nome até usuário digitar "sair"


# ----------------------------------------------------------
# IDEIA PRINCIPAL
# ----------------------------------------------------------

# while cria REPETIÇÃO

# ele permite que um programa execute
# a mesma lógica várias vezes

# sem precisar repetir código manualmente