"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321


nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)

# ==========================================================
# AULA 39 — RESOLUÇÃO (ITERANDO STRING COM WHILE)
# ==========================================================

# 1️⃣ Objetivo

# Percorrer uma string usando while
# e criar uma nova string modificada.

# ----------------------------------------------------------

# 2️⃣ Problema inicial (loop infinito)

# Se não atualizarmos o índice,
# o while nunca termina.

# Exemplo errado:

# indice = 0
# while indice < len(nome):
#     print(nome[indice])
#     # faltou indice += 1

# Isso gera loop infinito.

# ----------------------------------------------------------

# 3️⃣ Estrutura correta

# Precisamos de:
# - índice inicial
# - condição
# - incremento

nome = 'Maria Helena'

indice = 0

while indice < len(nome):
    print(nome[indice])
    indice += 1

# Isso percorre todas as letras.

# ----------------------------------------------------------

# 4️⃣ Criando nova string (acumulador)

# Podemos criar uma variável vazia
# e ir adicionando valores nela.

novo_nome = ''
indice = 0

while indice < len(nome):
    letra = nome[indice]

    # concatenação (acumulação)
    novo_nome += letra

    indice += 1

print(novo_nome)

# ----------------------------------------------------------

# 5️⃣ Modificando o resultado

# Podemos alterar cada letra durante o loop.

novo_nome = ''
indice = 0

while indice < len(nome):
    letra = nome[indice]

    novo_nome += f'*{letra}'

    indice += 1

# adiciona o último *
novo_nome += '*'

print(novo_nome)

# Resultado:
# *M*a*r*i*a* *H*e*l*e*n*a*

# ----------------------------------------------------------

# 6️⃣ Conceito importante: ACUMULADOR

# novo_nome começa vazio:
# ''

# A cada loop:
# ele recebe o valor antigo + novo valor

# Exemplo mental:

# '' + M -> M
# 'M' + a -> Ma
# 'Ma' + r -> Mar

# ----------------------------------------------------------

# 7️⃣ Tudo é dinâmico

# Funciona com qualquer string:

nome = 'Fabricio'

indice = 0
novo_nome = ''

while indice < len(nome):
    novo_nome += f'*{nome[indice]}'
    indice += 1

novo_nome += '*'

print(novo_nome)

# ----------------------------------------------------------

# 8️⃣ Conclusão

# Para iterar strings com while:

# 1. usar len() como limite
# 2. controlar índice manualmente
# 3. acessar com string[indice]
# 4. usar += para acumular valores

# Estrutura base:

# indice = 0
# while indice < len(string):
#     usar string[indice]
#     indice += 1

# Esse padrão é MUITO importante
# para lógica de programação.