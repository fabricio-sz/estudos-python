frase = 'aaaaooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes <= qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)

# ==========================================================
# AULA 42.1 — LETRA QUE MAIS SE REPETE (LÓGICA DE ITERAÇÃO)
# ==========================================================

# 1️⃣ O que estamos fazendo

# Descobrir qual letra aparece mais vezes em uma frase.

# ----------------------------------------------------------

# 2️⃣ Ideia principal

# Para cada letra:
# - contar quantas vezes ela aparece
# - comparar com o maior valor já encontrado
# - atualizar se for maior

# ----------------------------------------------------------

# 3️⃣ Estrutura mental

# para cada letra:
#     contar quantas vezes ela aparece
#     se for maior que o atual:
#         atualizar

# ----------------------------------------------------------

# 4️⃣ Código base

frase = "aaabbb"

quantidade_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ""

for letra in frase:

    if letra == " ":
        continue

    quantidade_atual = 0

    for outra_letra in frase:
        if outra_letra == letra:
            quantidade_atual += 1

    if quantidade_apareceu_mais_vezes < quantidade_atual:
        quantidade_apareceu_mais_vezes = quantidade_atual
        letra_apareceu_mais_vezes = letra

print(letra_apareceu_mais_vezes, quantidade_apareceu_mais_vezes)

# ----------------------------------------------------------

# 5️⃣ Como o código "pensa"

# letra = 'a'
# quantidade_atual = 3
# maior = 0 → atualiza → maior = 3, letra = 'a'

# próxima 'a'
# quantidade_atual = 3
# maior = 3 → NÃO atualiza

# letra = 'b'
# quantidade_atual = 3
# maior = 3 → NÃO atualiza

# ----------------------------------------------------------

# 6️⃣ Ponto MAIS importante

# Essa parte aqui:

# if quantidade_apareceu_mais_vezes < quantidade_atual:

# é o coração da lógica

# ----------------------------------------------------------

# 7️⃣ Empate (muito importante)

# 3 < 3 → FALSE

# Então:
# - NÃO atualiza
# - mantém a PRIMEIRA letra

# Resultado: 'a'

# ----------------------------------------------------------

# 8️⃣ Mudando o comportamento (<=)

# if quantidade_apareceu_mais_vezes <= quantidade_atual:

# Agora:

# 3 <= 3 → TRUE

# Então:
# - atualiza no empate
# - pega a ÚLTIMA letra

# Resultado: 'b'

# ----------------------------------------------------------

# 9️⃣ Ideia geral (padrão de programação)

# Esse tipo de lógica é MUITO usado:

# - encontrar maior valor
# - ranking
# - estatísticas
# - jogos

# ----------------------------------------------------------

# 🔟 Conclusão

# ✔️ percorre dados
# ✔️ conta valores
# ✔️ compara com o maior
# ✔️ atualiza quando necessário

# Isso é base de lógica de programação