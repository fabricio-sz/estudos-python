"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')


# ==========================================================
# AULA 53 — ENUMERATE (ÍNDICE + VALOR)
# ==========================================================

"""
enumerate → enumera iteráveis (índice + valor)
"""

# ==========================================================

# 1️⃣ LISTA

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# ==========================================================

# 2️⃣ USO MAIS COMUM (DESEMPACOTANDO)

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# ==========================================================

# 🧠 COMO FUNCIONA

"""
enumerate(lista) gera:

(0, 'Maria')
(1, 'Helena')
(2, 'Luiz')
(3, 'João')
"""

# Cada item é uma TUPLA:
# (indice, valor)

# ==========================================================

# 3️⃣ FORMA MANUAL (SEM DESEMPACOTAR)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

# ==========================================================

# 4️⃣ ENTENDENDO A TUPLA

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')

# ==========================================================

# 🧠 RESUMO VISUAL

"""
enumerate(lista):

→ (0, 'Maria')
→ (1, 'Helena')
→ (2, 'Luiz')
→ (3, 'João')
"""

# ==========================================================

# 5️⃣ START PERSONALIZADO

for indice, nome in enumerate(lista, start=1):
    print(indice, nome)

# Começa do 1 ao invés de 0

# ==========================================================

# ⚠️ CUIDADO COM ITERATOR

# Isso NÃO é comum de usar assim:
lista_enum = enumerate(lista)

for item in lista_enum:
    print(item)

# Segundo loop NÃO funciona (já foi consumido)

for item in lista_enum:
    print(item)  # nada acontece ❌

# ==========================================================

# ✅ FORMA CORRETA

# Use direto no for:

for indice, nome in enumerate(lista):
    print(indice, nome)

# ==========================================================

# 📌 QUANDO USAR ENUMERATE?

"""
✔ Quando precisa de índice + valor
✔ Melhor que usar range(len(lista))
✔ Código mais limpo
"""

# ==========================================================

# 🔥 COMPARAÇÃO

# ❌ Forma antiga
for i in range(len(lista)):
    print(i, lista[i])

# ✅ Forma moderna
for i, nome in enumerate(lista):
    print(i, nome)

# ==========================================================

# 🚀 CONCLUSÃO

"""
enumerate = padrão profissional

✔ mais legível
✔ mais simples
✔ mais pythonico

Use sempre que precisar de índice + valor 🔥
"""