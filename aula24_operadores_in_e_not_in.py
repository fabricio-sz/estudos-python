# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

# ==========================================================
# AULA 24 — OPERADORES IN E NOT IN
# ==========================================================

# 1️⃣ O que são os operadores IN e NOT IN

# IN significa:
# "está dentro de"

# NOT IN significa:
# "não está dentro de"

# Esses operadores servem para verificar
# se um valor existe dentro de outro.

# 2️⃣ Uso comum

# Eles são muito usados com:

# strings
# listas
# tuplas
# conjuntos
# dicionários

# Nesta aula foi mostrado o uso com strings.

# 3️⃣ Strings são iteráveis

# Em Python, strings são iteráveis.

# Isso significa que podemos percorrer
# caractere por caractere.

# Exemplo conceitual:

# palavra = "Otavio"

# O Python pode acessar cada letra individualmente.

# Índices positivos:
# O = 0
# t = 1
# a = 2
# v = 3
# i = 4
# o = 5

# Índices negativos:
# o = -1
# i = -2
# v = -3
# a = -4
# t = -5
# O = -6

# 4️⃣ Acesso por índice

# Podemos acessar um caractere usando colchetes.

# Exemplo conceitual:

# nome[2]

# Isso retorna a letra no índice 2.

# Também podemos acessar de trás para frente
# usando índices negativos.

# 5️⃣ Uso do operador IN

# O operador IN verifica
# se algo existe dentro de uma string.

# Exemplo conceitual:

# "a" in "Otavio"

# O Python verifica letra por letra
# até encontrar o valor.

# Se encontrar → True
# Se não encontrar → False

# 6️⃣ Uso do operador NOT IN

# NOT IN faz a verificação inversa.

# Exemplo conceitual:

# "z" not in "Otavio"

# Se o valor não existir na string,
# o resultado será True.

# 7️⃣ Funcionamento interno

# O Python percorre a string
# caractere por caractere
# até encontrar o valor procurado.

# Se encontrar → retorna True
# Se não encontrar → retorna False

# 8️⃣ Aplicações práticas

# Podemos usar IN para:

# validar senhas
# verificar caracteres proibidos
# buscar palavras em textos
# criar jogos de palavras
# validar entradas de usuário

# 9️⃣ Conclusão

# Os operadores IN e NOT IN são usados
# para verificar a existência de valores
# dentro de estruturas iteráveis.

# Eles são muito utilizados em validações
# e verificações de dados.