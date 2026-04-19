"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break


print('Acabou')

# ==========================================================
# AULA 37 — BREAK E CONTINUE NO WHILE
# ==========================================================

# 1️⃣ Palavra-chave break

# A palavra break serve para
# interromper (parar) o loop imediatamente.

# Quando o Python encontra break,
# ele encerra o laço naquele momento
# e continua executando o código
# que vem depois do loop.

# ----------------------------------------------------------

# 2️⃣ Exemplo conceitual de break

contador = 0

while contador <= 10:
    contador += 1

    if contador == 5:
        break  # o loop para aqui imediatamente

    print(contador)

# Quando contador for 5
# o loop termina.

# ----------------------------------------------------------

# 3️⃣ Ordem do código importa

# Se o break aparecer antes do print,
# aquele valor não será exibido.

# Exemplo conceitual:

contador = 0

while contador <= 10:
    contador += 1

    if contador == 5:
        break

    print(contador)

# O número 5 não aparece,
# porque o break acontece antes do print.

# ----------------------------------------------------------

# 4️⃣ Palavra-chave continue

# A palavra continue não encerra o loop.

# Ela apenas pula a execução
# do restante do código daquele ciclo
# e volta para o começo do loop.

# ----------------------------------------------------------

# 5️⃣ Exemplo conceitual de continue

contador = 0

while contador <= 10:
    contador += 1

    if contador == 5:
        continue  # pula o restante do código

    print(contador)

# O número 5 não será exibido,
# pois o loop volta ao início.

# ----------------------------------------------------------

# 6️⃣ Pulando vários valores

contador = 0

while contador <= 10:
    contador += 1

    if contador >= 4 and contador <= 7:
        continue  # pula os números de 4 até 7

    print(contador)

# Resultado esperado:
# 1 2 3 8 9 10

# ----------------------------------------------------------

# 7️⃣ Muito cuidado com continue

# Se a variável que controla o loop
# não for atualizada corretamente,
# pode acontecer um loop infinito.

# Exemplo perigoso:

contador = 0

while contador <= 5:

    if contador == 2:
        continue

    contador += 1

# Aqui o contador nunca muda
# quando é 2.

# Isso cria um loop infinito.

# ----------------------------------------------------------

# 8️⃣ Regra importante

# Sempre garanta que a variável
# que controla o while seja atualizada.

# Exemplo correto:

contador = 0

while contador <= 5:
    contador += 1

    if contador == 2:
        continue

    print(contador)

# ----------------------------------------------------------

# 9️⃣ Resumo mental

# break
# → encerra o loop imediatamente

# continue
# → pula o restante do código
#   e volta para o início do loop

# ----------------------------------------------------------

# 🔟 Exemplo da aula

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break

# O loop para no 40
# e continua o código abaixo.

print('Acabou')