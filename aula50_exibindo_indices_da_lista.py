"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))

# ==========================================================
# AULA 50 — EXIBINDO ÍNDICES DA LISTA
# ==========================================================

"""
Exercício:
Exiba os índices da lista

0 Maria
1 Helena
2 Luiz
"""

# ==========================================================

# 1️⃣ LISTA

lista = ['Maria', 'Helena', 'Luiz']

# Adicionando dinamicamente
lista.append('João')

# ==========================================================

# 2️⃣ GERANDO ÍNDICES

# len(lista) → tamanho da lista
# range(...) → gera números de 0 até tamanho - 1

indices = range(len(lista))

# ==========================================================

# 3️⃣ LOOP

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))

# ==========================================================

# 🧠 COMO FUNCIONA

"""
len(lista) → 4

range(4) → 0, 1, 2, 3

lista[indice] → acessa valor pelo índice
"""

# ==========================================================

# 🔁 VISUALIZAÇÃO

"""
indice = 0 → lista[0] → Maria
indice = 1 → lista[1] → Helena
indice = 2 → lista[2] → Luiz
indice = 3 → lista[3] → João
"""

# ==========================================================

# 📌 IMPORTANTE

"""
- range + len → gera índices automaticamente
- funciona para qualquer tamanho de lista
- totalmente dinâmico
"""

# ==========================================================

# 💡 DICA

"""
Esse padrão é MUITO usado:

for i in range(len(lista)):
    print(i, lista[i])
"""

# ==========================================================

# 🚀 CONCLUSÃO

"""
Você aprendeu a:
- gerar índices dinamicamente
- acessar valores por índice
- combinar range + len

Isso é base para muita coisa em Python 🔥
"""