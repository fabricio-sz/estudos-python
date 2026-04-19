"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 5)
print(lista[4])


# ==========================================================
# AULA 48 — LISTAS (MUTÁVEIS) + CRUD + MÉTODOS
# ==========================================================

# 📌 O QUE É LISTA
# - Tipo: list
# - Mutável (pode alterar valores)
# - Aceita vários tipos de dados

lista = [10, 20, 30, 40]

# ==========================================================

# 1️⃣ ACESSAR (READ)

# Índices:
#  0   1   2   3
# 10  20  30  40

print(lista[2])  # 30

# ==========================================================

# 2️⃣ ALTERAR (UPDATE)

lista[2] = 300
# Agora: [10, 20, 300, 40]

# ==========================================================

# 3️⃣ DELETAR (DELETE)

del lista[2]
# Agora: [10, 20, 40]

# ⚠️ IMPORTANTE:
# Ao deletar, os índices são reorganizados!

# ==========================================================

# 4️⃣ ADICIONAR NO FINAL (append)

lista = [10, 20, 30, 40]

lista.append(50)
# [10, 20, 30, 40, 50]

# ==========================================================

# 5️⃣ REMOVER DO FINAL (pop)

lista.pop()
# remove 50

# ==========================================================

# 6️⃣ REMOVER E PEGAR VALOR

lista.append(60)
lista.append(70)

ultimo_valor = lista.pop(3)
# remove índice 3 (40)

print(lista, 'Removido,', ultimo_valor)

# ==========================================================

# 🧠 CONCEITO IMPORTANTE

"""
Listas são MUTÁVEIS → mudam em memória
Tudo que altera a lista afeta ela inteira
"""

# ==========================================================

# 🚀 BOA PRÁTICA (PERFORMANCE)

"""
✔ Trabalhe no FINAL da lista (append / pop)
❌ Evite mexer no início/meio (del / insert em listas grandes)

Motivo:
Python precisa mover todos os elementos → lento
"""

# ==========================================================
# AULA 48.2 — MÉTODOS IMPORTANTES
# ==========================================================

lista = [10, 20, 30, 40]

# ----------------------------------------------------------

# 1️⃣ append → adiciona no final
lista.append('Luiz')

# ----------------------------------------------------------

# 2️⃣ pop → remove e retorna
nome = lista.pop()

# ----------------------------------------------------------

# 3️⃣ append novamente
lista.append(1233)

# ----------------------------------------------------------

# 4️⃣ del → remove por índice
del lista[-1]

# ----------------------------------------------------------

# 5️⃣ clear → limpa tudo
# lista.clear()

# ----------------------------------------------------------

# 6️⃣ insert → adiciona em índice específico

lista.insert(100, 5)
# ⚠️ Se o índice não existe → vai para o final

# Resultado:
# [10, 20, 30, 40, 5]

# ----------------------------------------------------------

print(lista[4])  # 5

# ==========================================================

# 📌 RESUMO DOS MÉTODOS

"""
append() → adiciona no final
insert() → adiciona em posição específica
pop()    → remove e retorna valor
del      → apaga índice
clear()  → limpa lista
extend() → junta listas (ver próxima aula)
+        → concatena listas
"""

# ==========================================================

# ⚠️ ERROS COMUNS

# ❌ Acessar índice que não existe
# lista[10] → IndexError

# ❌ Achar que insert cria índice específico
# Ele NÃO cria índice novo → só adapta

# ==========================================================

# 🧠 CRUD EM LISTAS

"""
Create → append / insert
Read   → lista[i]
Update → lista[i] = valor
Delete → del / pop
"""

# ==========================================================

# 💡 CONCLUSÃO

# Lista é um dos tipos MAIS importantes do Python
# Você vai usar MUITO em:
# - loops
# - dados
# - APIs
# - projetos reais

# Dominar lista = subir MUITO de nível 🚀


# ==========================================================
# AULA 48.3 — JUNTANDO LISTAS (+ e extend)
# ==========================================================

# 📌 OBJETIVO
# Aprender duas formas de juntar listas:
# - Usando +
# - Usando extend()

# ==========================================================

# 1️⃣ LISTAS INICIAIS

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

# ==========================================================

# 2️⃣ USANDO + (concatenação)

lista_c = lista_a + lista_b

print(lista_c)
# [1, 2, 3, 4, 5, 6]

# 📌 IMPORTANTE:
# - Cria uma NOVA lista
# - NÃO altera lista_a nem lista_b

# ==========================================================

# 3️⃣ USANDO extend()

lista_a.extend(lista_b)

print(lista_a)
# [1, 2, 3, 4, 5, 6]

# 📌 IMPORTANTE:
# - NÃO cria nova lista
# - ALTERA a lista original (lista_a)

# ==========================================================

# 🧠 DIFERENÇA PRINCIPAL

"""
+       → cria nova lista
extend  → modifica a lista existente
"""

# ==========================================================

# ⚠️ ERRO COMUM

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

resultado = lista_a.extend(lista_b)

print(resultado)  # None ❌

# 📌 Por quê?
# extend NÃO retorna nada → retorna None

# ==========================================================

# 🧠 EXPLICAÇÃO

"""
Quando um método retorna None:
→ Ele está modificando o próprio objeto

Ou seja:
lista_a.extend(lista_b)
→ muda diretamente lista_a
"""

# ==========================================================

# 🔥 POLIMORFISMO DO +

"""
+ se comporta diferente dependendo do tipo:

int    → soma
str    → concatena texto
list   → junta listas
"""

# ==========================================================

# 🧪 COMPARAÇÃO FINAL

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

# Forma 1 (nova lista)
lista_c = lista_a + lista_b

# Forma 2 (modifica original)
lista_a.extend(lista_b)

print(lista_a)  # [1, 2, 3, 4, 5, 6]
print(lista_c)  # [1, 2, 3, 4, 5, 6]

# ==========================================================

# 💡 QUANDO USAR CADA UM?

"""
Use + quando:
✔ quiser preservar listas originais
✔ quiser criar nova lista

Use extend quando:
✔ quiser modificar a lista existente
✔ quiser performance melhor (evita cópia)
"""

# ==========================================================

# 🚀 CONCLUSÃO

# Você acabou de aprender:
# - Como juntar listas
# - Diferença entre cópia e modificação
# - Conceito importante: mutabilidade

# Isso é MUITO importante em projetos reais ⚡



# ==========================================================
# AULA 48.4 — CUIDADOS COM DADOS MUTÁVEIS
# ==========================================================

# 📌 IDEIA PRINCIPAL
# O operador "=" NÃO copia sempre
# Depende do tipo de dado:
# - Imutável → "copia"
# - Mutável   → aponta para o MESMO lugar na memória

# ==========================================================

# 1️⃣ DADOS IMUTÁVEIS (str, int, float, bool)

nome = 'Luiz'
outro_nome = nome

nome = 'João'

print(nome)        # João
print(outro_nome)  # Luiz

# 📌 Aqui parece cópia
# Porque strings NÃO podem ser alteradas (imutáveis)

# ==========================================================

# 2️⃣ DADOS MUTÁVEIS (list)

lista_a = ['Luiz', 'Maria']
lista_b = lista_a  # ⚠️ NÃO é cópia!

lista_a[0] = 'Qualquer coisa'

print(lista_a)
print(lista_b)

# Resultado:
# Ambas mudam!

# 📌 Porque:
# lista_a e lista_b apontam para o MESMO objeto na memória

# ==========================================================

# 🧠 VISUALIZAÇÃO MENTAL

"""
lista_a ─┐
         ├──> ['Qualquer coisa', 'Maria']
lista_b ─┘
"""

# ==========================================================

# 3️⃣ COMO COPIAR DE VERDADE (copy)

lista_a = ['Luiz', 'Maria', 1, True, 1.2]

lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'

print(lista_a)
print(lista_b)

# Agora são listas diferentes!

# ==========================================================

# 🧠 VISUALIZAÇÃO

"""
lista_a ───> ['Qualquer coisa', 'Maria', ...]
lista_b ───> ['Luiz', 'Maria', ...]
"""

# ==========================================================

# 📌 REGRA DE OURO

"""
imutável → = "copia"
mutável  → = "referência" (mesmo objeto)
"""

# ==========================================================

# ⚠️ ERRO COMUM

lista1 = [1, 2, 3]
lista2 = lista1

lista2.append(4)

print(lista1)  # [1, 2, 3, 4] 😱

# Você achou que só mudou lista2… mas mudou as duas

# ==========================================================

# ✅ FORMA CORRETA

lista1 = [1, 2, 3]
lista2 = lista1.copy()

lista2.append(4)

print(lista1)  # [1, 2, 3]
print(lista2)  # [1, 2, 3, 4]

# ==========================================================

# 💡 OBSERVAÇÃO IMPORTANTE

"""
.copy() funciona bem para listas simples

⚠️ Se tiver lista dentro de lista:
→ isso fica mais complexo (deep copy)

Isso será visto mais pra frente
"""

# ==========================================================

# 🚀 CONCLUSÃO

"""
- "=" pode enganar em Python
- Listas compartilham memória
- Use .copy() quando quiser independência
- Esse conceito é MUITO importante em projetos reais
"""

# ==========================================================

# 🔥 RESUMO FINAL

"""
imutável → seguro usar =
mutável  → cuidado! use .copy()
"""