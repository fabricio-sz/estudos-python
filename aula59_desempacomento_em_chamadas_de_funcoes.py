# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# p, b, *_, ap, u = lista
# print(p, u, ap)

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')

# ==========================================================
# AULA 59 — DESEMPACOTAMENTO EM CHAMADAS DE FUNÇÕES (*)
# ==========================================================

"""
Nesta aula você aprende:

✔ Desempacotar iteráveis com *
✔ Usar * em chamadas de função (print)
✔ Diferença entre for e *
✔ Melhorar visualização de dados
"""

# ==========================================================

# 1️⃣ DADOS

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = ('Python', 'é', 'legal')

salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda'],
]

# ==========================================================

# 2️⃣ SEM DESEMPACOTAMENTO

print(lista)

# 👉 Saída:
# ['Maria', 'Helena', 1, 2, 3, 'Eduarda']

# ==========================================================

# 3️⃣ COM DESEMPACOTAMENTO (*)

print(*lista)

# 👉 Saída:
# Maria Helena 1 2 3 Eduarda

# ==========================================================

# 🧠 O QUE O * FAZ?

"""
*lista

→ pega cada item da lista
→ passa como argumento separado

É como fazer:

print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
"""

# Explicação baseada na aula :contentReference[oaicite:0]{index=0}

# ==========================================================

# 4️⃣ FUNCIONA COM QUALQUER ITERÁVEL

print(*string)
# A B C D

print(*tupla)
# Python é legal

# ==========================================================

# 5️⃣ CUSTOMIZANDO SAÍDA

print(*lista, sep=' - ')
# Maria - Helena - 1 - 2 - 3 - Eduarda

# ==========================================================

# 6️⃣ COMPARAÇÃO COM FOR

# FOR (mais controle)
for item in lista:
    print(item, end=' ')

print('\n')

# * (mais simples)
print(*lista)

# ==========================================================

# 🧠 RESUMO

"""
for → você controla a iteração
*   → Python faz automaticamente
"""

# ==========================================================

# 7️⃣ LISTA DE LISTAS

print(salas)

# 👉 Saída:
# [['Maria', 'Helena'], ['Elaine'], ['Luiz', 'João', 'Eduarda']]

# ==========================================================

# 8️⃣ MELHORANDO VISUALIZAÇÃO

print(*salas, sep='\n')

# 👉 Saída:
# ['Maria', 'Helena']
# ['Elaine']
# ['Luiz', 'João', 'Eduarda']

# ==========================================================

# 🧠 EXPLICAÇÃO

"""
*salas

→ desempacota cada lista interna

sep='\n'

→ cada item em uma linha
"""

# ==========================================================

# 9️⃣ CASO REAL

"""
Muito usado em:

✔ print()
✔ funções
✔ APIs
✔ argumentos dinâmicos
"""

# ==========================================================

# 🔟 DIFERENÇA IMPORTANTE

"""
* → desempacota valores
** → desempacota dicionários (futuro)
"""

# ==========================================================

# 🚀 CONCLUSÃO

"""
Você aprendeu:

✔ usar * para desempacotar
✔ aplicar em print()
✔ melhorar visualização

👉 Isso é MUITO usado em código profissional

Você já está entrando no nível intermediário 🔥
"""