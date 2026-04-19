"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)

# ==========================================================
# AULA 56 — SPLIT, STRIP E JOIN (STRINGS + LISTAS)
# ==========================================================

"""
split e join com list e str

split → divide uma string → retorna LISTA
join  → une uma lista → retorna STRING
strip → remove espaços do início e fim
"""

# ==========================================================

# 1️⃣ FRASE ORIGINAL

frase = '   Olha só que   , coisa interessante          '

# ==========================================================

# 2️⃣ SPLIT (DIVIDIR STRING)

lista_frases_cruas = frase.split(',')

print(lista_frases_cruas)

# 📌 Resultado:
# ['   Olha só que   ', ' coisa interessante          ']

# 👉 split divide baseado no separador
# 👉 a vírgula NÃO aparece no resultado

# Explicação baseada na aula :contentReference[oaicite:0]{index=0}

# ==========================================================

# 3️⃣ PROBLEMA: ESPAÇOS SOBRANDO

# Temos espaços no início e no fim das strings

# ==========================================================

# 4️⃣ STRIP (LIMPAR ESPAÇOS)

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases)

# 📌 strip remove:
# - espaços no início
# - espaços no fim

# ==========================================================

# 🧠 OUTROS TIPOS DE STRIP

"""
strip()  → remove dos dois lados
lstrip() → remove da esquerda
rstrip() → remove da direita
"""

# ==========================================================

# 5️⃣ JOIN (UNIR LISTA EM STRING)

frases_unidas = ', '.join(lista_frases)

print(frases_unidas)

# 📌 Resultado:
# Olha só que, coisa interessante

# ==========================================================

# 🧠 COMO FUNCIONA O JOIN

"""
', '.join(lista)

→ pega cada item da lista
→ une com ", " entre eles

Exemplo:
['A', 'B', 'C']
→ "A, B, C"
"""

# ==========================================================

# 6️⃣ EXEMPLO SIMPLES

lista = ['A', 'B', 'C']

print('-'.join(lista))
# A-B-C

# ==========================================================

# 📌 REGRAS IMPORTANTES

"""
✔ split → retorna LISTA
✔ join  → retorna STRING

✔ join precisa de iterável (lista, tupla, string)

❌ join NÃO aceita número
"""

# ==========================================================

# ⚠️ ERRO COMUM

# '-'.join([1, 2, 3]) ❌ erro

# ✔ correto:
# '-'.join(['1', '2', '3'])

# ==========================================================

# 💡 BOA PRÁTICA

"""
Evite alterar lista original

✔ melhor:
criar nova lista tratada
"""

# ==========================================================

# 🚀 CONCLUSÃO

"""
Você aprendeu:

✔ split → quebrar string
✔ strip → limpar espaços
✔ join → unir lista

👉 Isso é MUITO usado em:
- manipulação de texto
- arquivos
- APIs
- sistemas reais

Você acabou de aprender algo MUITO importante 🔥
"""