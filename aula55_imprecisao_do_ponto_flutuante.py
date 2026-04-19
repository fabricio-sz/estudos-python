"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))

# # ==========================================================
# # AULA 55 — IMPRECISÃO DE PONTO FLUTUANTE
# # ==========================================================

# """
# Imprecisão de ponto flutuante (float)

# Problema comum em várias linguagens de programação
# (Python também)

# Baseado no padrão:
# IEEE 754 (Double Precision Floating Point)
# """

# # ==========================================================

# # 1️⃣ O PROBLEMA

# numero_1 = 0.1
# numero_2 = 0.7
# numero_3 = numero_1 + numero_2

# print(numero_3)  # ❌ 0.7999999999999999 (impreciso)

# # ==========================================================

# # 🧠 POR QUE ISSO ACONTECE?

# """
# O problema NÃO é do Python

# ✔ O computador NÃO consegue representar
# certos números decimais exatamente na memória

# Exemplo:
# 0.1 não existe exatamente em binário

# 👉 Resultado: pequenas imprecisões
# """

# # Explicação baseada na aula :contentReference[oaicite:0]{index=0}

# # ==========================================================

# # 2️⃣ SOLUÇÃO 1 — FORMATAR (F-STRING)

# numero_3 = numero_1 + numero_2

# print(f'{numero_3:.2f}')  # ✔ 0.80

# # 📌 IMPORTANTE:
# # Isso vira STRING (texto)

# # ==========================================================

# # 3️⃣ SOLUÇÃO 2 — ROUND

# print(round(numero_3, 2))  # ✔ 0.8

# # 📌 IMPORTANTE:
# # Continua sendo FLOAT (número)

# # ==========================================================

# # 4️⃣ SOLUÇÃO 3 — DECIMAL (PRECISÃO REAL)

# import decimal

# numero_1 = decimal.Decimal('0.1')
# numero_2 = decimal.Decimal('0.7')

# numero_3 = numero_1 + numero_2

# print(numero_3)  # ✔ 0.8

# # ==========================================================

# # 🧠 DETALHE IMPORTANTE

# """
# Decimal deve receber STRING ❗

# ❌ errado:
# Decimal(0.1)

# ✔ correto:
# Decimal('0.1')
# """

# # ==========================================================

# # 📊 COMPARAÇÃO

# """
# float:
# ✔ rápido
# ❌ impreciso em alguns casos

# round:
# ✔ corrige visualmente
# ✔ continua float

# f-string:
# ✔ formata bonito
# ❌ vira texto

# decimal:
# ✔ preciso
# ❌ mais lento
# """

# # ==========================================================

# # 📌 QUANDO USAR?

# """
# 99% dos casos:
# → use float normalmente

# Exibição:
# → use f-string

# Cálculo simples:
# → use round()

# Alta precisão (financeiro, científico):
# → use decimal
# """

# # ==========================================================

# # 🚀 CONCLUSÃO

# """
# Imprecisão de float é NORMAL

# ✔ Não é erro do Python
# ✔ É limitação do computador

# Você deve saber:
# - quando ignorar
# - quando corrigir
# - quando usar decimal

# Isso é nível mais avançado 🔥
# """
