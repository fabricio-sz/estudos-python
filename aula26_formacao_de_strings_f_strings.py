"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')


# ==========================================================
# AULA 26 — FORMATAÇÃO DE STRINGS (F-STRINGS)
# ==========================================================

# 1️⃣ O que é formatação de strings

# Formatação de strings é a capacidade de controlar
# como um valor será exibido dentro de uma string.

# Isso inclui:
# largura do texto
# alinhamento
# casas decimais
# sinais positivos/negativos
# preenchimento com caracteres
# conversão de números (ex: hexadecimal)

# Nesta aula o foco é nas F-STRINGS,
# que são a forma moderna de formatar strings no Python.

# Estrutura básica:

# f"{variavel:formatação}"

# A parte após ":" define como o valor será exibido.

# ----------------------------------------------------------

# 2️⃣ Padding (largura fixa)

# Podemos definir um tamanho mínimo para o texto.

# Exemplo conceitual:
# f"{variavel:10}"

# Se a variável tiver menos caracteres,
# o Python completa com espaços.

# Isso é chamado de PADDING.

# ----------------------------------------------------------

# 3️⃣ Alinhamento de texto

# Podemos escolher onde o texto será alinhado.

# >  alinhamento à direita
# <  alinhamento à esquerda
# ^  alinhamento centralizado

# Exemplos conceituais:

# f"{texto:>10}"   direita
# f"{texto:<10}"   esquerda
# f"{texto:^10}"   centro

# O número representa a largura total.

# ----------------------------------------------------------

# 4️⃣ Preenchimento com caracteres

# Podemos escolher qual caractere preencherá o espaço.

# Exemplo conceitual:

# f"{texto:_>10}"

# Isso preencheria os espaços com "_".

# Podemos usar qualquer caractere:
# 0
# $
# -
# *

# ----------------------------------------------------------

# 5️⃣ Formatação de números float

# Para limitar casas decimais usamos:

# .nf

# Onde n é a quantidade de casas decimais.

# Exemplos conceituais:

# f"{valor:.2f}"  → duas casas decimais
# f"{valor:.1f}"  → uma casa decimal

# ----------------------------------------------------------

# 6️⃣ Separador de milhares

# Podemos usar vírgula para separar milhares.

# Exemplo conceitual:

# f"{numero:,.2f}"

# Resultado possível:
# 1,000.45

# Obs:
# No Brasil usamos ponto e vírgula invertidos,
# mas o Python segue padrão internacional.

# ----------------------------------------------------------

# 7️⃣ Mostrar sinal positivo e negativo

# Podemos forçar o Python a mostrar o sinal.

# +  → mostra + ou -
# -  → mostra apenas o negativo (padrão)

# Exemplo conceitual:

# f"{numero:+}"

# Resultado:
# +10
# -10

# ----------------------------------------------------------

# 8️⃣ Preenchimento com zeros

# Podemos preencher números com zeros à esquerda.

# Exemplo conceitual:

# f"{numero:010}"

# Isso cria um número com largura 10
# preenchido com zeros.

# ----------------------------------------------------------

# 9️⃣ Ajuste do sinal com zeros

# Às vezes o sinal fica depois do zero.

# Para corrigir usamos "=".

# Exemplo conceitual:

# f"{numero:0=+10}"

# Isso garante que o sinal venha antes dos zeros.

# ----------------------------------------------------------

# 🔟 Hexadecimal

# Podemos converter números para hexadecimal.

# x → hexadecimal minúsculo
# X → hexadecimal maiúsculo

# Exemplo conceitual:

# f"{1500:x}"
# f"{1500:X}"

# Também podemos definir largura:

# f"{1500:08X}"

# Resultado exemplo:
# 000005DC

# ----------------------------------------------------------

# 1️⃣1️⃣ Conversion flags

# Às vezes vemos algo como:

# f"{variavel!r}"
# f"{variavel!s}"
# f"{variavel!a}"

# Isso chama métodos internos do Python.

# !r → repr()
# !s → str()
# !a → ascii()

# Esses conceitos envolvem métodos e objetos,
# que serão estudados mais para frente.

# Por enquanto apenas saiba que eles existem.

# ----------------------------------------------------------

# 1️⃣2️⃣ Conclusão

# F-strings são a forma moderna e recomendada
# para formatação de strings em Python.

# Elas permitem controlar facilmente:

# alinhamento
# largura
# casas decimais
# conversão numérica
# preenchimento
# sinais

# Ao longo do curso essas técnicas serão
# usadas frequentemente.