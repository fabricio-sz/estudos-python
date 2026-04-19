""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')

# ==========================================================
# AULA 41 — WHILE / ELSE
# ==========================================================

# 1️⃣ O que é o while com else

# No Python, o while pode ter um else.

# O bloco else será executado somente se:
# o while terminar normalmente (sem break)

# ----------------------------------------------------------

# 2️⃣ Estrutura básica

# while condição:
#     código
# else:
#     código executado se NÃO houve break

# ----------------------------------------------------------

# 3️⃣ Exemplo simples

i = 0

while i < 3:
    print(i)
    i += 1
else:
    print("Loop terminou normalmente.")

# ✔️ Aqui o else executa
# porque o while terminou sem break

# ----------------------------------------------------------

# 4️⃣ Quando o else NÃO executa

i = 0

while i < 3:
    if i == 1:
        break
    print(i)
    i += 1
else:
    print("Loop terminou normalmente.")

# ❌ Aqui o else NÃO executa
# porque houve break

# ----------------------------------------------------------

# 5️⃣ Ideia principal

# while + else funciona assim:

# ✔️ Terminou naturalmente → executa else
# ❌ Teve break → NÃO executa else

# ----------------------------------------------------------

# 6️⃣ Exemplo da aula (procurando espaço)

string = 'Valor qualquer'

i = 0

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break  # encontrou espaço → sai do loop

    print(letra)
    i += 1

else:
    print('Não encontrei um espaço na string.')

print('Fora do while.')

# ----------------------------------------------------------

# 7️⃣ O que acontece nesse código

# Caso 1:
# string = "Valor qualquer"
# → tem espaço
# → break acontece
# → else NÃO executa

# Caso 2:
# string = "Valorqualquer"
# → NÃO tem espaço
# → loop vai até o fim
# → else executa

# ----------------------------------------------------------

# 8️⃣ Uso prático

# while/else é útil quando queremos:

# - procurar algo
# - saber se NÃO encontrou

# Exemplo mental:

# while procurando:
#     if achou:
#         break
# else:
#     não achou

# ----------------------------------------------------------

# 9️⃣ Forma equivalente sem else

# Muitos programadores preferem fazer assim:

encontrou = False

i = 0
string = "Valorqualquer"

while i < len(string):
    if string[i] == ' ':
        encontrou = True
        break
    i += 1

if not encontrou:
    print("Não encontrou espaço")

# ✔️ Mesmo resultado
# ✔️ Mais comum na prática

# ----------------------------------------------------------

# 🔟 Conclusão

# while/else:

# ✔️ executa else se o loop terminar normalmente
# ❌ não executa else se houver break

# É um recurso específico do Python
# e pouco usado na prática,
# mas importante conhecer.