"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])


# ==========================================================
# AULA 27 — FATIAMENTO DE STRINGS (STRING SLICING)
# ==========================================================

# 1️⃣ Strings são imutáveis (inalteráveis)

# Em Python, strings são imutáveis.
# Isso significa que não podemos alterar um caractere
# diretamente dentro da string.

# Porém podemos:
# acessar caracteres
# percorrer caracteres
# pegar partes da string (fatiamento)

# ----------------------------------------------------------

# 2️⃣ Índices das strings

# Cada caractere possui um índice.

# Índices positivos (da esquerda para direita):
# começam em 0

# Exemplo conceitual:

#  0 1 2 3 4 5 6 7 8
#  O l á   m u n d o

# Índices negativos (da direita para esquerda):

# -9 -8 -7 -6 -5 -4 -3 -2 -1

# O índice negativo começa do final da string.

# ----------------------------------------------------------

# 3️⃣ Acessando caracteres

# Podemos acessar caracteres usando colchetes.

# Exemplo conceitual:

# variavel[1]

# Isso retorna o caractere do índice 1.

# Também podemos usar índice negativo.

# Exemplo conceitual:

# variavel[-1]

# Isso retorna o último caractere.

# ----------------------------------------------------------

# 4️⃣ O que é fatiamento (slicing)

# Fatiamento significa pegar uma "fatia"
# da string.

# Estrutura geral:

# variavel[inicio:fim:passo]

# Onde:

# inicio → índice inicial
# fim → índice final (não incluído)
# passo → de quantos em quantos caracteres avançar

# ----------------------------------------------------------

# 5️⃣ Índice final NÃO é incluído

# No Python, o índice final NÃO entra no resultado.

# Exemplo conceitual:

# variavel[0:4]

# retorna os caracteres do índice
# 0,1,2,3

# O índice 4 não entra.

# ----------------------------------------------------------

# 6️⃣ Omitindo valores

# Podemos omitir partes do slicing.

# variavel[:5]

# começa do início e vai até índice 5.

# variavel[4:]

# começa no índice 4 e vai até o final.

# variavel[:]

# retorna a string inteira.

# ----------------------------------------------------------

# 7️⃣ Passo (step)

# O passo define de quantos em quantos
# caracteres o Python irá pular.

# Exemplo conceitual:

# variavel[::2]

# pega um caractere
# pula um
# pega outro
# pula outro

# Ou seja, pega de 2 em 2.

# ----------------------------------------------------------

# 8️⃣ Invertendo strings

# Podemos inverter uma string usando
# passo negativo.

# Exemplo conceitual:

# variavel[::-1]

# Isso faz o Python percorrer a string
# de trás para frente.

# Resultado: string invertida.

# ----------------------------------------------------------

# 9️⃣ Espaço também é caractere

# Espaços contam como caracteres.

# Mesmo que não apareçam visualmente,
# eles ocupam posição dentro da string.

# ----------------------------------------------------------

# 🔟 Função len()

# A função len() retorna a quantidade
# de caracteres da string.

# Exemplo conceitual:

# len("Olá mundo")

# retorna 9

# Importante lembrar:

# quantidade de caracteres
# é diferente de índice.

# Se a string tem 9 caracteres:

# índices vão de:
# 0 até 8

# ----------------------------------------------------------

# 1️⃣1️⃣ Estrutura geral do slicing

# variavel[inicio:fim:passo]

# inicio → onde começa
# fim → onde termina (não incluído)
# passo → salto entre caracteres

# ----------------------------------------------------------

# 1️⃣2️⃣ Conclusão

# O fatiamento permite:

# pegar partes da string
# pular caracteres
# inverter strings
# navegar pelos caracteres

# É uma ferramenta muito usada
# em manipulação de textos.




