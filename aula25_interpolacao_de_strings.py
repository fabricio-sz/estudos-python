"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))

# ==========================================================
# AULA 25 — INTERPOLAÇÃO DE STRINGS
# ==========================================================

# 1️⃣ O que é interpolação de strings

# Interpolação é uma forma de inserir valores de variáveis
# dentro de uma string.

# É semelhante ao que já vimos com:
# - f-strings
# - método format()

# Porém aqui usamos o operador de porcentagem (%).

# 2️⃣ Estrutura da interpolação

# Estrutura básica:

# "texto %tipo texto" % (variavel)

# Os símbolos % dentro da string são chamados de
# placeholders (marcadores de posição).

# Eles indicam onde os valores serão inseridos.

# 3️⃣ Tipos de placeholders

# %s → string
# %d → inteiro
# %i → inteiro
# %f → float (número decimal)
# %x → hexadecimal minúsculo
# %X → hexadecimal maiúsculo

# 4️⃣ Ordem dos valores

# Quando usamos mais de um placeholder,
# os valores são passados em uma tupla.

# Exemplo conceitual:

# '%s custa %.2f' % (nome, preco)

# O primeiro valor substitui o primeiro placeholder.
# O segundo valor substitui o segundo placeholder.

# 5️⃣ Formatação de casas decimais

# Podemos limitar casas decimais com:

# %.2f

# Isso significa:
# mostrar apenas 2 casas decimais.

# Exemplo conceitual:
# %.3f → três casas decimais
# %.1f → uma casa decimal

# 6️⃣ Conversão para hexadecimal

# Podemos converter números para hexadecimal
# usando %x ou %X.

# %x → hexadecimal minúsculo
# %X → hexadecimal maiúsculo

# Exemplo conceitual:
# 15 → f
# 255 → ff

# 7️⃣ Preenchimento com zeros

# Podemos definir largura mínima do número.

# Exemplo conceitual:

# %08X

# Isso significa:
# número hexadecimal com 8 dígitos
# preenchendo com zeros à esquerda.

# Exemplo resultado:
# 000005DC

# 8️⃣ Cuidados importantes

# A quantidade de placeholders deve ser
# exatamente igual à quantidade de valores.

# Caso contrário o Python gera erro.

# Exemplo errado conceitualmente:

# "%s %s" % (nome)

# Pois existem dois placeholders
# mas apenas um valor.

# 9️⃣ Observação do professor

# Existem três formas principais de formatar strings:

# - Interpolação com %
# - método format()
# - f-strings

# A forma mais moderna e recomendada hoje
# geralmente é usar f-strings.

# Mesmo assim é importante conhecer
# a interpolação porque ela aparece
# em códigos antigos de Python.