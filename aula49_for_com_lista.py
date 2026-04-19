# ==========================================================
# AULA 49 — FOR COM LISTAS
# ==========================================================

# 📌 IDEIA PRINCIPAL
# O for funciona com QUALQUER iterável:
# - string
# - range
# - lista

# ==========================================================

# 1️⃣ LISTA (iterável)

lista = ["Alvez", "Joseph", "Gkuia"]

# ==========================================================

# 2️⃣ USANDO FOR NA LISTA

for item in lista:
    print(item)

# Saída:
# Alvez
# Joseph
# Gkuia

# ==========================================================

# 🧠 COMO FUNCIONA

"""
O for percorre a lista e:
- pega UM item por vez
- joga na variável (item)
- executa o código
"""

# ==========================================================

# 🔁 VISUALIZAÇÃO

"""
lista = ["Alvez", "Joseph", "Gkuia"]

1ª volta → item = "Alvez"
2ª volta → item = "Joseph"
3ª volta → item = "Gkuia"
"""

# ==========================================================

# 📌 IMPORTANTE

"""
Você NÃO está pegando índice
Você está pegando o VALOR direto
"""

# ==========================================================

# 3️⃣ EXEMPLO COM NOMES

nomes = ["Maria", "Helena", "Luiz"]

for nome in nomes:
    print("Nome:", nome)

# ==========================================================

# 4️⃣ LISTA COM TIPOS DIFERENTES

lista_mista = ["Luiz", 123, True, 1.5]

for item in lista_mista:
    print(item, type(item))

# 📌 Lista aceita qualquer tipo

# ==========================================================

# 🧠 RESUMO FINAL

"""
for item in lista:
    → percorre item por item

lista → iterável
item  → valor atual

Simples assim 🚀
"""

# ==========================================================

# 💡 CONCLUSÃO

# Essa aula é simples, mas MUITO importante
# porque você vai usar isso o tempo todo

# for + lista = base de praticamente tudo em Python