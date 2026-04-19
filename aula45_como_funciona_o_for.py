"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luiz'  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)


# # ==========================================================
# # AULA 45 — COMO O FOR FUNCIONA (POR BAIXO DOS PANOS)
# # ==========================================================

# # 📌 IDEIA PRINCIPAL
# # Você NÃO precisa saber isso para usar for,
# # mas entender isso te dá um nível mais avançado em Python.

# # ----------------------------------------------------------

# # 1️⃣ Conceitos importantes

# # Iterável:
# # Objeto que pode ser percorrido (str, list, range, etc)
# # Possui o método: __iter__()

# # Iterador:
# # Objeto que sabe entregar UM valor por vez
# # Possui o método: __next__()

# # ----------------------------------------------------------

# # 2️⃣ Funções importantes

# # iter(obj)  -> pega o iterador do objeto
# # next(obj)  -> pega o próximo valor do iterador

# # ----------------------------------------------------------

# # 3️⃣ Exemplo com string (iterável)

# texto = 'Luiz'

# # Pegando o iterador manualmente
# iterador = iter(texto)

# print(next(iterador))  # L
# print(next(iterador))  # u
# print(next(iterador))  # i
# print(next(iterador))  # z

# # Se chamar mais uma vez:
# # next(iterador)
# # ❌ Vai dar erro: StopIteration

# # ----------------------------------------------------------

# # 4️⃣ StopIteration

# # Esse erro acontece quando NÃO existem mais valores
# # Ele é usado para PARAR a iteração

# # ----------------------------------------------------------

# # 5️⃣ Simulando o FOR com while (como funciona internamente)

# texto = 'Luiz'
# iterador = iter(texto)

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

# # Isso aqui faz EXATAMENTE o que o for faz

# # ----------------------------------------------------------

# # 6️⃣ O que o FOR faz por baixo dos panos

# # for letra in texto:
# #     print(letra)

# # 🔽 Equivalente a:

# # 1. Pega o iterador:
# # iterador = iter(texto)

# # 2. Loop:
# # while True:
# #     try:
# #         letra = next(iterador)
# #         print(letra)
# #     except StopIteration:
# #         break

# # ----------------------------------------------------------

# # 7️⃣ Resumo final

# """
# Iterável -> possui __iter__()
# Iterador -> possui __next__()
# iter()   -> pega o iterador
# next()   -> pega próximo valor
# for      -> automatiza tudo isso
# """

# # ----------------------------------------------------------

# # 8️⃣ Exemplo final (forma simples e correta)

# for letra in texto:
#     print(letra)

# # ✔ Simples
# # ✔ Limpo
# # ✔ Pythonico

# # ----------------------------------------------------------

# # 💡 CONCLUSÃO

# # O for NÃO é mágico.
# # Ele só automatiza:
# # - pegar iterador
# # - chamar next()
# # - tratar StopIteration

# # Você não precisa escrever isso na mão,
# # mas agora você entende como funciona por trás.
