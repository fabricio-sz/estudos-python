"""
Operados de atribuição
= += -= *= /= //= **= %=
"""

contador = 20

contador += 3

print(contador)

# ==========================================================
# AULA 36 — OPERADORES DE ATRIBUIÇÃO
# ==========================================================

# 1️⃣ O que são operadores de atribuição

# Operadores de atribuição servem para
# atualizar o valor de uma variável.

# Eles utilizam o valor antigo da variável
# para calcular um novo valor.

# ----------------------------------------------------------

# 2️⃣ Atribuição normal

# O operador básico de atribuição é:

# =

# Exemplo:

contador = 10

# Aqui a variável contador recebe o valor 10.

# ----------------------------------------------------------

# 3️⃣ Usando o valor antigo da variável

# Muitas vezes queremos atualizar
# uma variável usando o valor que ela
# já possui.

# Exemplo clássico:

contador = contador + 1

# O Python pega o valor antigo
# soma 1
# e guarda novamente na variável.

# ----------------------------------------------------------

# 4️⃣ Forma simplificada

# Como essa operação é muito comum,
# existe uma forma mais curta.

contador += 1

# Isso significa exatamente:

# contador = contador + 1

# ----------------------------------------------------------

# 5️⃣ Operadores de atribuição disponíveis

# =   atribuição normal
# +=  soma e atribui
# -=  subtrai e atribui
# *=  multiplica e atribui
# /=  divide e atribui
# //= divisão inteira e atribui
# **= potência e atribui
# %=  resto da divisão (módulo) e atribui

# Todos utilizam o valor antigo da variável.

# ----------------------------------------------------------

# 6️⃣ Exemplos com números

contador = 10

contador += 2   # 10 + 2 = 12
contador -= 1   # 12 - 1 = 11
contador *= 3   # 11 * 3 = 33
contador /= 3   # 33 / 3 = 11.0

# ----------------------------------------------------------

# 7️⃣ Divisão inteira

# O operador // descarta a parte decimal.

contador = 10
contador //= 3

# Resultado: 3

# ----------------------------------------------------------

# 8️⃣ Potência

# O operador ** faz exponenciação.

contador = 2
contador **= 10

# Resultado: 1024

# ----------------------------------------------------------

# 9️⃣ Operador módulo

# O operador % retorna o resto da divisão.

contador = 10
contador %= 3

# Resultado: 1

# Muito usado para verificar
# números pares ou ímpares.

# Exemplo conceitual:

# numero % 2 == 0

# Se for verdadeiro → número é par.

# ----------------------------------------------------------

# 🔟 Operadores também funcionam com strings

texto = "1"
texto += "2"

# Resultado: "12"
# Aqui ocorre concatenação de strings.

# ----------------------------------------------------------

# 1️⃣1️⃣ Multiplicação de string

texto = "A"
texto *= 5

# Resultado: "AAAAA"
# O Python repete a string.

# ----------------------------------------------------------

# 1️⃣2️⃣ Conclusão

# Operadores de atribuição servem para:

# atualizar variáveis
# escrever menos código
# deixar o código mais limpo

# Estrutura mental importante:

# x += y → x = x + y
# x -= y → x = x - y
# x *= y → x = x * y
# x /= y → x = x / y

# Ou seja:
# sempre usa o valor antigo da variável
# para calcular o novo valor.