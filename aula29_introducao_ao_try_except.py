"""
try/except
try -> Tenta executar o código
except -> ocorreu algum erro ao tentar executar

"""



numero = input("Dobrador de número: ")

try: 
    print(f"String: {numero}")
    numero_float = float(numero)
    print(f"Float: {numero_float}")
    print(f"O dobro de {numero} é {numero_float * 2}")

except:

    print("Esse não é um número.")

# if numero.isdigit(): ## isdigit() valida se foi inserido um numero

#     numero_float = float(numero)
#     print(f"O dobro de {numero} é {numero_float * 2}")

# else:

#     print("Esse não é um número.")


# ==========================================================
# AULA 29 — INTRODUÇÃO AO TRY / EXCEPT
# ==========================================================

# 1️⃣ O que é try / except

# try / except é usado para tratar erros no Python.

# try significa:
# "tente executar este código"

# except significa:
# "se ocorrer um erro, execute este outro código"

# Isso permite que o programa continue rodando
# mesmo quando ocorre algum erro.

# ----------------------------------------------------------

# 2️⃣ O que é uma exceção

# No Python, erros em tempo de execução
# são chamados de EXCEÇÕES.

# Exemplo comum:
# tentar converter uma letra para número.

# int("a")

# Isso gera um erro porque "a"
# não pode ser convertido para número.

# Quando isso acontece o Python:

# - interrompe a execução do programa
# - mostra o erro no terminal

# ----------------------------------------------------------

# 3️⃣ Problema sem tratamento de erro

# Se ocorrer um erro e não houver tratamento:

# o programa PARA imediatamente.

# Exemplo conceitual:

# print(123)
# int("a")      ← erro aqui
# print(456)

# O segundo print nunca será executado.

# ----------------------------------------------------------

# 4️⃣ Estrutura básica do try / except

# try:
#     código que pode gerar erro
# except:
#     código executado se ocorrer erro

# Fluxo:

# Python tenta executar o bloco try.
# Se ocorrer erro → pula para o except.

# ----------------------------------------------------------

# 5️⃣ Exemplo com input do usuário

# Quando usamos input(), o valor sempre
# chega como STRING.

# Se quisermos fazer cálculos,
# precisamos converter para número.

# Exemplo conceitual:

# numero = input(...)
# numero_float = float(numero)

# Se o usuário digitar letras,
# essa conversão gera erro.

# ----------------------------------------------------------

# 6️⃣ Tratando o erro com try / except

# Colocamos a conversão dentro do try.

# try:
#     numero_float = float(numero)
# except:
#     print("Isso não é um número")

# Se o usuário digitar algo inválido,
# o programa não quebra.

# ----------------------------------------------------------

# 7️⃣ Fluxo de execução

# Quando ocorre erro dentro do try:

# Python:
# interrompe o try
# pula imediatamente para o except

# Todo código abaixo da linha do erro
# dentro do try é ignorado.

# ----------------------------------------------------------

# 8️⃣ Caso não ocorra erro

# Se o código dentro do try
# executar normalmente:

# o except é ignorado.

# Ou seja:

# try executa normalmente
# except não roda.

# ----------------------------------------------------------

# 9️⃣ Comparação com if

# if verifica condições lógicas.

# try / except trata erros.

# Exemplo:

# if numero.isdigit()
# verifica se o texto tem apenas números.

# Já try / except simplesmente
# tenta executar e captura o erro.

# ----------------------------------------------------------

# 🔟 Validação com isdigit()

# isdigit() verifica se a string
# contém apenas números inteiros.

# Porém não aceita:

# números decimais
# números negativos
# ponto decimal

# Por isso try / except costuma
# ser mais flexível.

# ----------------------------------------------------------

# 1️⃣1️⃣ Conceito importante

# try / except segue a ideia de:

# "fail fast"

# Ou seja:

# tente executar
# se falhar → trate o erro.

# ----------------------------------------------------------

# 1️⃣2️⃣ Conclusão

# try / except permite:

# evitar que o programa quebre
# capturar erros de execução
# mostrar mensagens amigáveis ao usuário

# Esse é apenas o uso básico.

# Mais para frente veremos:

# tipos de exceção
# except específicos
# else
# finally
# criação de exceções