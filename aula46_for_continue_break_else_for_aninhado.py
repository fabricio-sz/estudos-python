for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)

else:
    print('For completo com sucesso!')



# # ==========================================================
# # AULA 46 — FOR (CONTINUE, BREAK, ELSE E FOR ANINHADO)
# # ==========================================================

# # 📌 IDEIA PRINCIPAL
# # Tudo que funciona no while também funciona no for:
# # - continue
# # - break
# # - else

# # Diferença:
# # while → quando NÃO sabemos quantas repetições
# # for   → quando SABEMOS (ex: range)

# # ----------------------------------------------------------

# # 1️⃣ Exemplo básico com range

# for i in range(10):
#     print(i)

# # Vai de 0 até 9

# # ----------------------------------------------------------

# # 2️⃣ Continue (pula para próxima iteração)

# for i in range(10):
#     if i == 2:
#         print('i é 2, pulando...')
#         continue

#     print(i)

# # O número 2 não será exibido

# # ----------------------------------------------------------

# # 3️⃣ Break (interrompe o laço)

# for i in range(10):
#     if i == 5:
#         print('Parando no 5')
#         break

#     print(i)

# # Para completamente no 5

# # ----------------------------------------------------------

# # 4️⃣ Else no for

# for i in range(5):
#     print(i)
# else:
#     print('For completo com sucesso!')

# # O else só executa se NÃO houver break

# # ----------------------------------------------------------

# # 5️⃣ Else NÃO executa com break

# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print('Não aparece')

# # ----------------------------------------------------------

# # 6️⃣ For aninhado (for dentro de for)

# # i → linha
# # j → coluna

# for i in range(3):
#     for j in range(2):
#         print(i, j)

# # Saída:
# # 0 0
# # 0 1
# # 1 0
# # 1 1
# # 2 0
# # 2 1

# # ----------------------------------------------------------

# # 7️⃣ Exemplo COMPLETO da aula

# for i in range(10):
#     if i == 2:
#         print('i é 2, pulando...')
#         continue

#     if i == 8:
#         print('i é 8, seu else não executará')
#         break

#     for j in range(1, 3):
#         print(i, j)

# else:
#     print('For completo com sucesso!')

# # ----------------------------------------------------------

# # 🧠 O QUE ESTÁ ACONTECENDO

# # - i percorre de 0 a 9
# # - quando i == 2 → pula (continue)
# # - quando i == 8 → para tudo (break)
# # - j cria um "loop interno" (colunas)

# # ----------------------------------------------------------

# # 📌 RESUMO FINAL

# """
# continue → pula para próxima iteração
# break    → encerra o laço
# else     → executa se NÃO houver break
# for      → ideal quando sabemos o intervalo
# for aninhado → linhas e colunas
# """

# # ----------------------------------------------------------

# # 💡 DICA DE OURO

# # i, j, k são padrões para loops
# # (principalmente em loops aninhados)

# # i → linha
# # j → coluna

# # Isso é padrão no mundo da programação 🚀