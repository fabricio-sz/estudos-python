adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)

# ==========================================================
# AULA 9 — Operadores Aritméticos
# ==========================================================

# 1️⃣ O que essa aula ensina?
# - Operações matemáticas em Python.
# - Diferença entre divisão normal e divisão inteira.
# - Uso do módulo (%).
# - Como verificar múltiplos e números pares/ímpares.

# 2️⃣ Operadores básicos:

# +  -> Adição
# -  -> Subtração
# *  -> Multiplicação
# /  -> Divisão (sempre retorna float)
# // -> Divisão inteira (remove casas decimais)
# ** -> Exponenciação (potência)
# %  -> Módulo (resto da divisão)

# 3️⃣ Divisão (/)
# - Sempre retorna float.
# - Mesmo que os números sejam inteiros.

# Exemplo:
# 10 / 2 -> 5.0

# 4️⃣ Divisão inteira (//)
# - Remove tudo que vem depois do ponto.
# - Não arredonda, apenas corta.

# Exemplo:
# 10 // 3 -> 3

# 5️⃣ Exponenciação (**)
# - Eleva um número a outro.
# Exemplo:
# 2 ** 3 -> 8

# 6️⃣ Módulo (%)
# - Retorna o resto da divisão.
# Exemplo:
# 10 % 3 -> 1

# 7️⃣ Aplicações práticas do módulo:

# ✔ Verificar se é múltiplo:
# numero % divisor == 0

# ✔ Verificar se é par:
# numero % 2 == 0

# ✔ Verificar se é ímpar:
# numero % 2 != 0

# 8️⃣ Conclusão:
# - Python respeita regras matemáticas.
# - Cada operador tem comportamento específico.
# - Módulo é extremamente útil para lógica.