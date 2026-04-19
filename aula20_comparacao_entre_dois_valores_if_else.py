primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )

# ==========================================================
# AULA 20 — COMPARAÇÃO ENTRE DOIS VALORES (IF / ELSE)
# ==========================================================

# 1️⃣ Objetivo da aula
# Comparar dois valores digitados pelo usuário
# e informar qual é maior.

# 2️⃣ Fluxo do programa
# - Recebe o primeiro valor com input().
# - Recebe o segundo valor com input().
# - Compara os dois usando operador relacional.
# - Exibe o resultado com base na condição.

# 3️⃣ Estrutura usada
# if / else

# Se a condição for verdadeira:
# Executa o bloco do if.

# Se a condição for falsa:
# Executa o bloco do else.

# 4️⃣ Operador utilizado
# >=  (maior ou igual)
# ou
# >   (maior)

# 5️⃣ Ponto importante
# Se usar apenas >,
# quando os valores forem iguais,
# o código cairá no else.

# Se usar >=,
# cobre também o caso de igualdade.

# 6️⃣ Sobre input()
# input() sempre retorna string.
# Se for necessário comparar numericamente,
# deve-se converter para int() ou float().

# 7️⃣ Lógica da comparação
# O programa faz uma pergunta:
# "O primeiro valor é maior (ou maior ou igual) que o segundo?"

# Se True:
# Mostra que o primeiro é maior.

# Se False:
# Mostra que o segundo é maior.

# 8️⃣ Conclusão
# Esse exercício reforça:
# - Uso de input()
# - Conversão de tipos
# - Operadores relacionais
# - Estrutura condicional
# - Fluxo lógico simples
