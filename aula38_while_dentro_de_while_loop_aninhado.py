

# qtd_linhas = 5
# qtd_colunas = 5


# linha = 1

# while linha <= qtd_linhas:

#     coluna = 1

#     while coluna <= qtd_colunas:

#         print(f"|__ {linha} __| |__ {coluna} __|")
#         coluna += 1


#     linha += 1

# print("Final")
senha_oficial = "JOSE"
idade = 20

senha = " "

while senha != senha_oficial:

    print("Errou, tente novamente")
    
    senha = input("Qual sua senha ? ")

    if senha == senha_oficial:

        verifica_idade = 0

        while verifica_idade != idade:

            verifica_idade = int(input("Parabens, agora diga sua idade: "))

            print(f"{senha_oficial}, sua idade está errada, tente novamente.")

            if verifica_idade == idade:

                print("Parabens! Voce conseguiu.")

# ==========================================================
# AULA 38 — WHILE DENTRO DE WHILE (LOOP ANINHADO)
# ==========================================================

# 1️⃣ O que é um while dentro de while

# Um while dentro de outro while é chamado
# de "loop aninhado".

# Isso significa que temos:
# um loop externo (principal)
# e um loop interno (que roda várias vezes
# dentro do primeiro).

# Estrutura conceitual:

# while condição_externa:
#     while condição_interna:
#         código

# ----------------------------------------------------------

# 2️⃣ Ideia de linhas e colunas

# Um exemplo clássico de loop aninhado
# é trabalhar com:

# linhas
# colunas

# Exemplo real:
# tabelas
# matrizes
# mapas
# grids
# jogos

# ----------------------------------------------------------

# 3️⃣ Loop externo (linhas)

# O primeiro while controla
# quantas linhas teremos.

# Exemplo conceitual:

# linha = 1
# while linha <= qtd_linhas:

# A cada volta do loop
# estamos em uma nova linha.

# ----------------------------------------------------------

# 4️⃣ Loop interno (colunas)

# Dentro de cada linha
# teremos várias colunas.

# Então criamos outro while
# dentro do primeiro.

# Exemplo conceitual:

# coluna = 1
# while coluna <= qtd_colunas:

# Esse loop roda várias vezes
# para cada linha.

# ----------------------------------------------------------

# 5️⃣ Como o loop funciona na prática

# Para cada linha:
# o loop interno roda várias vezes.

# Exemplo:

# linha 1 -> coluna 1,2,3,4,5
# linha 2 -> coluna 1,2,3,4,5
# linha 3 -> coluna 1,2,3,4,5

# Ou seja:

# 1 volta do loop externo
# executa várias voltas do loop interno.

# ----------------------------------------------------------

# 6️⃣ Reiniciando a coluna

# Muito importante:

# A variável coluna precisa
# ser reiniciada dentro do loop externo.

# Exemplo:

# while linha <= qtd_linhas:
#     coluna = 1

# Isso garante que cada nova linha
# comece novamente da coluna 1.

# ----------------------------------------------------------

# 7️⃣ Exemplo completo da aula

qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:

    coluna = 1  # reinicia coluna a cada nova linha

    while coluna <= qtd_colunas:

        print(f"|__ {linha} __| |__ {coluna} __|")

        coluna += 1  # controla o loop interno

    linha += 1  # controla o loop externo


# ----------------------------------------------------------

# 8️⃣ Como o programa executa

# Linha 1
# coluna 1
# coluna 2
# coluna 3
# coluna 4
# coluna 5

# Linha 2
# coluna 1
# coluna 2
# coluna 3
# coluna 4
# coluna 5

# Isso continua até linha 5.

# ----------------------------------------------------------

# 9️⃣ Analogia das engrenagens

# Imagine duas engrenagens:

# engrenagem grande → loop das linhas
# engrenagem pequena → loop das colunas

# Cada vez que a engrenagem grande gira,
# a pequena gira várias vezes.

# ----------------------------------------------------------

# 🔟 Conclusão

# Loops aninhados permitem:

# criar tabelas
# percorrer matrizes
# gerar padrões
# fazer algoritmos mais complexos

# Estrutura geral:

# while linhas:
#     while colunas:
#         executar código

# É um conceito muito importante
# em programação.
 
print("Final")