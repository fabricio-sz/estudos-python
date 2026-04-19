"""
For + Range
range -> range(start, stop, step)
"""
numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)

# # ==========================================================
# # AULA 44 — FOR + RANGE
# # ==========================================================

# # 1️⃣ O que é range

# # range é uma função do Python que gera uma sequência de números.
# # Ela é um iterável (pode ser percorrido com for).

# # Sintaxe:
# # range(start, stop, step)

# # ----------------------------------------------------------

# # 2️⃣ Parâmetros do range

# # start -> onde começa (padrão = 0)
# # stop  -> onde termina (NÃO inclui o último valor)
# # step  -> de quanto em quanto vai pular (padrão = 1)

# # Exemplos:

# range(10)
# # Vai de 0 até 9

# range(5, 10)
# # Vai de 5 até 9

# range(0, 10, 2)
# # Vai de 2 em 2 → 0, 2, 4, 6, 8

# # ----------------------------------------------------------

# # 3️⃣ Cuidado com nomes de variáveis

# # NÃO use nomes reservados como:
# # range, min, max, etc.

# # Errado:
# # range = range(10)

# # Correto:
# numeros = range(10)

# # ----------------------------------------------------------

# # 4️⃣ Usando range com for

# # O for percorre o iterável (range)
# # e entrega um valor por vez

# for numero in range(10):
#     print(numero)

# # Aqui NÃO usamos índice
# # O for já entrega o valor direto

# # ----------------------------------------------------------

# # 5️⃣ Começando de outro número

# for numero in range(5, 10):
#     print(numero)

# # Saída:
# # 5, 6, 7, 8, 9

# # ----------------------------------------------------------

# # 6️⃣ Pulando valores (step)

# for numero in range(5, 10, 2):
#     print(numero)

# # Saída:
# # 5, 7, 9

# # ----------------------------------------------------------

# # 7️⃣ Step negativo (contagem reversa)

# for numero in range(0, -10, -1):
#     print(numero)

# # Saída:
# # 0, -1, -2, -3...

# # IMPORTANTE:
# # Se o step é negativo, o início deve ser maior que o fim

# # ----------------------------------------------------------

# # 8️⃣ Usos práticos

# # Números pares de 0 a 100
# for numero in range(0, 101, 2):
#     print(numero)

# # Múltiplos de 8
# for numero in range(0, 101, 8):
#     print(numero)

# # ----------------------------------------------------------

# # 9️⃣ Como o for funciona (resumo)

# # O for pega o iterável (range)
# # Cria um iterador
# # Pede o próximo valor
# # Executa o código
# # Repete até acabar

# # Quando acaba, ocorre um "StopIteration"
# # e o for encerra automaticamente

# # ----------------------------------------------------------

# # 🔟 Exemplo final

# """
# For + Range
# range -> range(start, stop, step)
# """

# numeros = range(0, 100, 8)

# for numero in numeros:
#     print(numero)