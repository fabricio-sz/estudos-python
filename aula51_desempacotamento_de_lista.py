"""
Introdução ao empacotamento e desempacotamento
"""
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)

# ==========================================================
# AULA 51 — DESEMPACOTAMENTO DE LISTAS
# ==========================================================

"""
Introdução ao desempacotamento

Permite extrair valores de uma lista diretamente
em variáveis
"""

# ==========================================================

# 1️⃣ DESEMPACOTAMENTO BÁSICO

nomes = ["Jose", "Fael", "Ricardo"]

nome1, nome2, nome3 = nomes

print(nome1)  # Jose
print(nome2)  # Fael
print(nome3)  # Ricardo

# ==========================================================

# 🧠 REGRA IMPORTANTE

"""
Quantidade de variáveis == quantidade de valores

✔ 3 variáveis → 3 valores → OK
❌ menos variáveis → erro
❌ mais variáveis → erro
"""

# ==========================================================

# 2️⃣ ERRO COMUM

# nome1, nome2 = nomes
# ❌ ValueError: muitos valores para desempacotar

# ==========================================================

# 3️⃣ USANDO * (RESTO)

nome1, *resto = ["Jose", "Fael", "Ricardo"]

print(nome1)   # Jose
print(resto)   # ['Fael', 'Ricardo']

# ==========================================================

# 🧠 COMO FUNCIONA

"""
*resto → pega TODOS os valores restantes
e coloca dentro de uma lista
"""

# ==========================================================

# 4️⃣ IGNORANDO VALORES (_)

nome1, *_ = ["Jose", "Fael", "Ricardo"]

print(nome1)  # Jose
print(_)      # ['Fael', 'Ricardo']

# ==========================================================

# 🧠 CONVENÇÃO

"""
_ (underline) → variável que você NÃO vai usar

Muito usado para ignorar valores
"""

# ==========================================================

# 5️⃣ PEGANDO VALOR DO MEIO

_, nome2, *_ = ["Jose", "Fael", "Ricardo"]

print(nome2)  # Fael

# ==========================================================

# 6️⃣ PEGANDO ÚLTIMO VALOR

*_, ultimo = ["Jose", "Fael", "Ricardo"]

print(ultimo)  # Ricardo

# ==========================================================

# 7️⃣ CASO SEM RESTO

nome1, nome2, *resto = ["Jose", "Fael"]

print(nome1)   # Jose
print(nome2)   # Fael
print(resto)   # []

# ==========================================================

# 📌 RESUMO FINAL

"""
Desempacotamento:
→ pega valores da lista e joga em variáveis

*variavel:
→ pega o restante

_:
→ ignorar valores

Regra:
→ número de variáveis deve bater com valores
→ ou usar * para capturar o resto
"""

# ==========================================================

# 🚀 CONCLUSÃO

"""
Esse conceito é MUITO importante porque:
- simplifica código
- evita indexação manual
- é usado em códigos profissionais

Você vai usar MUITO isso ainda 🔥
"""