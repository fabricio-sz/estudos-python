frase = 'aaaooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual


    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)

# ==========================================================
# AULA 42 — LETRA QUE MAIS SE REPETE (ALGORITMO)
# ==========================================================

# 1️⃣ Objetivo da aula

# Dada uma frase, queremos descobrir:
# qual letra apareceu mais vezes.

# ----------------------------------------------------------

# 2️⃣ Ideia do algoritmo

# Precisamos:
# - percorrer a string (while)
# - pegar cada letra
# - contar quantas vezes ela aparece
# - comparar com a maior quantidade já encontrada
# - salvar se for maior

# ----------------------------------------------------------

# 3️⃣ Variáveis principais

frase = 'aaaooo'

i = 0

# guarda a maior quantidade encontrada
qtd_apareceu_mais_vezes = 0

# guarda a letra correspondente
letra_apareceu_mais_vezes = ''

# ----------------------------------------------------------

# 4️⃣ Percorrendo a string

while i < len(frase):

    letra_atual = frase[i]

    # ------------------------------------------------------
    # 5️⃣ Ignorando espaços
    # ------------------------------------------------------

    if letra_atual == ' ':
        i += 1
        continue

    # ------------------------------------------------------
    # 6️⃣ Contando quantas vezes a letra aparece
    # ------------------------------------------------------

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    # ------------------------------------------------------
    # 7️⃣ Comparando com a maior quantidade
    # ------------------------------------------------------

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:

        # atualiza a maior quantidade
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual

        # salva a letra correspondente
        letra_apareceu_mais_vezes = letra_atual

    i += 1

# ----------------------------------------------------------

# 8️⃣ Resultado final

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)

# ----------------------------------------------------------

# 9️⃣ Passo a passo mental (IMPORTANTE)

# Exemplo: 'aaaooo'

# letra = 'a' → count = 3
# maior = 0 → atualiza → maior = 3

# letra = 'o' → count = 3
# maior = 3 → NÃO atualiza (empate)

# Resultado:
# 'a' ganhou porque apareceu primeiro

# ----------------------------------------------------------

# 🔟 Conceito chave: "guardar estado"

# Esse algoritmo funciona porque:

# - guardamos a melhor resposta até agora
# - comparamos com o novo valor
# - atualizamos se for melhor

# Isso é MUITO usado em programação.

# ----------------------------------------------------------

# 1️⃣1️⃣ Cuidado com continue

# Se você usar continue antes do i += 1
# você cria loop infinito.

# ERRADO:

# if letra == ' ':
#     continue   ❌ trava o loop

# CORRETO:

# if letra == ' ':
#     i += 1
#     continue

# ----------------------------------------------------------

# 1️⃣2️⃣ Melhorias possíveis

# ✔️ ignorar maiúsculas/minúsculas:

# frase = frase.lower()

# ✔️ ignorar espaços:

# if letra_atual == ' ':
#     ...

# ✔️ ignorar acentos (mais avançado)

# ----------------------------------------------------------

# 1️⃣3️⃣ Versão alternativa (mais avançada)

# Usando dicionário (nível mais alto)

# frequencia = {}

# for letra in frase:
#     if letra == ' ':
#         continue

#     frequencia[letra] = frequencia.get(letra, 0) + 1

# # pegando a maior

# maior_letra = ''
# maior_qtd = 0

# for letra, qtd in frequencia.items():
#     if qtd > maior_qtd:
#         maior_qtd = qtd
#         maior_letra = letra

# ----------------------------------------------------------

# 1️⃣4️⃣ Conclusão

# Você aprendeu um padrão MUITO importante:

# ✔️ percorrer dados
# ✔️ contar ocorrências
# ✔️ comparar valores
# ✔️ guardar o melhor resultado

# Esse padrão aparece em:
# - algoritmos
# - entrevistas técnicas
# - sistemas reais