# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
# senha = input('Senha: ')

print(not True)  # False
print(not False)  # True


# ==========================================================
# AULA 23 — OPERADOR LÓGICO NOT
# ==========================================================

# 1️⃣ O que é o operador NOT
# NOT significa "NÃO".
# Ele é usado para inverter o valor lógico de uma expressão.

# Exemplo:
# True  → vira False
# False → vira True

# 2️⃣ Funcionamento básico

# not True  → False
# not False → True

# Ou seja, o operador NOT simplesmente inverte o resultado lógico.

# 3️⃣ Uso dentro de condições

# O NOT é muito usado dentro de estruturas IF
# para verificar o contrário de uma condição.

# Exemplo conceitual:
# if not condição:

# Isso significa:
# "se a condição NÃO for verdadeira"

# 4️⃣ Uso com valores falsy

# Alguns valores são considerados falsos em Python:

# False
# 0
# 0.0
# ''
# None

# Quando usamos NOT nesses valores,
# o resultado passa a ser True.

# Exemplo conceitual:
# not 0   → True
# not ''  → True

# 5️⃣ Uso comum em inputs

# Um uso muito comum do NOT é verificar
# se o usuário NÃO digitou nada.

# Exemplo conceitual:

# senha = input()

# if not senha:
# significa:
# "se nenhuma senha foi digitada"

# 6️⃣ Vantagem do NOT

# Ele permite escrever código mais simples
# quando queremos verificar o oposto de algo.

# Em vez de escrever comparações longas,
# podemos apenas inverter a condição.

# 7️⃣ Conclusão

# O operador NOT:
# - Inverte expressões lógicas
# - É muito usado em verificações
# - Ajuda a simplificar condições no código