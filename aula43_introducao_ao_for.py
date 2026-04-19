# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')
texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')

# ==========================================================
# AULA 43 — INTRODUÇÃO AO FOR
# ==========================================================

# 1️⃣ O que é o for

# for é um laço de repetição (loop) no Python.

# Ele é usado para percorrer elementos
# de uma sequência (iterável), como:

# strings
# listas
# tuplas

# ----------------------------------------------------------

# 2️⃣ Diferença entre while e for

# while é usado quando NÃO sabemos
# quantas repetições vão acontecer.

# Exemplo:
# entrada de usuário
# validação de senha

# for é usado quando SABEMOS
# quantas repetições vão ocorrer.

# Exemplo:
# percorrer uma string
# percorrer uma lista

# ----------------------------------------------------------

# 3️⃣ Problema com while

# Para percorrer uma string com while:

# precisamos:
# criar índice
# controlar manualmente
# usar len()
# incrementar índice

# Isso torna o código mais complexo.

# ----------------------------------------------------------

# 4️⃣ Quando usar for

# Usamos for quando:

# sabemos o tamanho da sequência
# queremos acessar cada elemento
# a quantidade de repetições é previsível

# O Python já controla tudo automaticamente.

# ----------------------------------------------------------

# 5️⃣ Estrutura do for

# for variavel in iteravel:
#     código

# Leitura:

# "para cada elemento dentro do iterável,
# faça alguma coisa"

# ----------------------------------------------------------

# 6️⃣ Exemplo com string

# texto = 'Python'

# for letra in texto:
#     print(letra)

# O for percorre cada letra da string.

# ----------------------------------------------------------

# 7️⃣ Variável do for

# A variável (ex: letra) é criada por você.

# Ela recebe, a cada repetição:

# um elemento do iterável

# Exemplo:

# 'P' → 'y' → 't' → 'h' → 'o' → 'n'

# ----------------------------------------------------------

# 8️⃣ Iterável

# Um iterável é um objeto que pode
# ser percorrido elemento por elemento.

# Exemplos:

# string
# lista
# tupla

# O for usa automaticamente o iterador interno.

# ----------------------------------------------------------

# 9️⃣ Vantagem do for

# Não precisamos:

# controlar índice
# usar len()
# incrementar variável

# O Python faz tudo automaticamente.

# Código fica mais simples e limpo.

# ----------------------------------------------------------

# 🔟 Comparação prática

# while:
# mais manual
# mais controle
# usado quando não sabemos o fim

# for:
# mais simples
# mais direto
# usado quando sabemos o fim

# ----------------------------------------------------------

# 1️⃣1️⃣ Exemplo criando nova string

# texto = 'Python'
# novo_texto = ''

# for letra in texto:
#     novo_texto += f'*{letra}'

# print(novo_texto + '*')

# Resultado:
# *P*y*t*h*o*n*

# ----------------------------------------------------------

# 1️⃣2️⃣ Fluxo do for

# Para cada elemento:

# Python:
# pega o próximo valor
# coloca na variável
# executa o bloco

# Repete até acabar os elementos.

# ----------------------------------------------------------

# 1️⃣3️⃣ Conclusão

# for é ideal para:

# percorrer sequências
# código mais simples
# evitar controle manual

# while continua útil quando:

# não sabemos quantas repetições ocorrerão

# Nas próximas aulas veremos:

# range()
# for com números
# break e continue no for