"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)

# ==========================================================
# AULA 57 — LISTA DE LISTAS (MATRIZ / ESTRUTURA ANINHADA)
# ==========================================================

"""
Lista de listas e seus índices

Podemos ter:
- lista dentro de lista
- tupla dentro de lista
- etc

Isso é MUITO comum em programação
"""

# ==========================================================

# 1️⃣ ESTRUTURA

salas = [
    # 0        1
    ['Maria', 'Helena'],        # índice 0
    # 0
    ['Elaine'],                 # índice 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda'] # índice 2
]

# ==========================================================

# 2️⃣ ACESSANDO VALORES

# Acessar lista externa
print(salas[0])        # ['Maria', 'Helena']

# Acessar lista interna
print(salas[0][1])     # Helena
print(salas[1][0])     # Elaine
print(salas[2][2])     # Eduarda

# ==========================================================

# 🧠 COMO PENSAR

"""
salas[linha][coluna]

Primeiro:
→ escolhe a lista (sala)

Depois:
→ escolhe o item dentro dela
"""

# Explicação baseada na aula :contentReference[oaicite:0]{index=0}

# ==========================================================

# 3️⃣ ERRO COMUM

# print(salas[2][3]) ❌ IndexError
# índice não existe

# ==========================================================

# 4️⃣ FOR COM LISTA DE LISTAS

for sala in salas:
    print(f'A sala é {sala}')

    for aluno in sala:
        print(aluno)

# ==========================================================

# 🧠 COMO FUNCIONA O FOR

"""
for sala in salas:
→ percorre cada lista interna

for aluno in sala:
→ percorre cada item da lista interna
"""

# ==========================================================

# 🔁 VISUALIZAÇÃO

"""
salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda']
]

FOR externo:
→ pega cada lista

FOR interno:
→ pega cada aluno
"""

# ==========================================================

# 5️⃣ EXEMPLO MAIS AVANÇADO

salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda', (10, 20, 30)]
]

# Acessando valor dentro de tupla dentro da lista

print(salas[2][3][1])  # 20

# ==========================================================

# 🧠 IMPORTANTE

"""
Você pode ter:
- lista dentro de lista
- lista dentro de tupla
- tupla dentro de lista

Tudo que for iterável pode estar dentro
"""

# ==========================================================

# ⚠️ BOA PRÁTICA

"""
Evite misturar muitos tipos diferentes:

✔ melhor:
lista só com strings

❌ ruim:
string + int + lista + tupla misturado

Isso dificulta o código
"""

# ==========================================================

# 🚀 CONCLUSÃO

"""
Você aprendeu:

✔ listas dentro de listas
✔ acesso com múltiplos índices
✔ for aninhado (loop dentro de loop)

👉 Isso é base para:
- matrizes
- tabelas
- banco de dados
- sistemas reais

Você está subindo de nível 🔥
"""