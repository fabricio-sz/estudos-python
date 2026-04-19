concatenacao = 'Luiz' + ' ' + 'Otávio'
print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_luiz = 3 * 'Luiz'
print(a_dez_vezes)
print(tres_vezes_luiz)

# ==========================================================
# AULA 10 — Concatenação e Repetição com Operadores
# ==========================================================

# 1️⃣ O que essa aula ensina?
# - O operador + pode somar números.
# - O operador + também pode concatenar strings.
# - O operador * pode repetir strings.

# 2️⃣ Concatenação (+)
# - Só funciona corretamente quando os dois lados são strings.
# - Ele junta os valores.
#
# Exemplo:
# "Luiz" + " " + "Otávio"
# Resultado: "Luiz Otávio"

# ⚠️ Cuidado com tipos diferentes:
# "Luiz" + 1  -> ERRO
# Para corrigir:
# "Luiz" + str(1)

# 3️⃣ Repetição (*)
# - Funciona com: string * inteiro
#
# Exemplo:
# "A" * 5
# Resultado: "AAAAA"

# 4️⃣ Regras importantes:
# - string + string → concatenação
# - string * inteiro → repetição
# - tipos diferentes sem conversão → erro

# 5️⃣ Conclusão:
# - Python é fortemente tipado.
# - Sempre observe o tipo da variável antes da operação.
