# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')

# ==========================================================
# AULA 15 — Função input() e Conversão de Tipos
# ==========================================================

# 1️⃣ O que essa aula ensina?
# - Como coletar dados do usuário usando a função input().
# - Entender que input() sempre retorna uma string (str).

# 2️⃣ Conceito principal:
# - input() pausa o programa e espera o usuário digitar algo no terminal.
# - O valor digitado é retornado como string.
# - Para fazer cálculos, é necessário converter o tipo (int(), float(), etc).

# 3️⃣ Como o Python executa:
# - O programa para na linha do input().
# - O usuário digita algo e pressiona Enter.
# - O valor digitado vai para a variável.
# - Se for necessário cálculo, deve-se converter o tipo antes.

# 4️⃣ Conversão de tipos (Type Casting):
# - int() converte para número inteiro.
# - float() converte para número decimal.
# - Se o valor digitado não puder ser convertido, o programa gera erro.

# 5️⃣ Boa prática mostrada na aula:
# - Primeiro armazenar o valor como string.
# - Depois converter em outra variável.
# - Isso permite validar antes de converter.

# 6️⃣ Problema importante:
# - Se converter direto no input e o usuário digitar letra,
#   o programa quebra imediatamente.
# - Por isso é melhor separar:
#     numero = input()
#     int_numero = int(numero)

# 7️⃣ Observação:
# - input() funciona corretamente no terminal.
# - Ele sempre retorna string, mesmo que o usuário digite números.
