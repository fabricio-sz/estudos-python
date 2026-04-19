"""
Tipo tupla - Uma lista imutável
"""
nomes = ('Maria', 'Helena', 'Luiz')
# nomes = tuple(nomes)
# nomes = list(nomes)
print(nomes[-1])
print(nomes)

# ==========================================================
# AULA 52 — TUPLAS (LISTA IMUTÁVEL)
# ==========================================================

"""
Tipo tupla - Uma lista imutável
"""

# ==========================================================

# 1️⃣ CRIANDO UMA TUPLA

nomes = ('Maria', 'Helena', 'Luiz')

print(nomes)

# ==========================================================

# 2️⃣ ACESSANDO VALORES

print(nomes[0])   # Maria
print(nomes[-1])  # Luiz

# ==========================================================

# 🧠 IMPORTANTE

"""
Tupla funciona igual lista em:
✔ índices
✔ for
✔ len
✔ acesso

Mas NÃO permite alteração
"""

# ==========================================================

# 3️⃣ TUPLA É IMUTÁVEL

# nomes[0] = 'João'  ❌ ERRO

# TypeError:
# tuple object does not support item assignment

# ==========================================================

# 4️⃣ DIFERENÇA ENTRE LISTA E TUPLA

"""
Lista:
- Mutável
- Pode alterar
- Tem métodos (append, pop...)

Tupla:
- Imutável
- NÃO altera
- Mais leve e rápida
"""

# ==========================================================

# 5️⃣ FORMAS DE CRIAR TUPLA

# Forma comum
nomes = ('Maria', 'Helena', 'Luiz')

# Sem parênteses (também funciona)
nomes = 'Maria', 'Helena', 'Luiz'

# ==========================================================

# 6️⃣ CONVERSÃO

# Lista → Tupla
lista = ['Maria', 'Helena', 'Luiz']
nomes = tuple(lista)

# Tupla → Lista
nomes = list(nomes)

# ==========================================================

# 🧠 QUANDO USAR TUPLA?

"""
✔ Quando NÃO precisa alterar dados
✔ Para dados fixos
✔ Para performance melhor
"""

# ==========================================================

# 💡 EXEMPLOS REAIS

"""
- Coordenadas (x, y)
- Dias da semana
- Configurações fixas
"""

# ==========================================================

# 🚀 RESUMO FINAL

"""
Tupla = lista imutável

✔ Mais rápida
✔ Mais segura
❌ Não pode alterar

Use quando os dados NÃO mudam
"""

# ==========================================================

# 🔥 CONCLUSÃO

# Se não precisa alterar → use tupla
# Se precisa alterar → use lista