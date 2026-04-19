"""
Calculadora
Usuario escolhe dois números
Depois disso escolhe a operação

"""

numero_1 = input("Escolha o primeiro número: ")
numero_2 = input("Escolha o primeiro número: ")

try:

    numero_1 = int(numero_1)
    numero_2 = int(numero_2)
    escolha = " "

    while escolha != 0:

        print("====== Calculadora ======")
        print("1 - Multiplicação")
        print("2 - Divisão")
        print("3 - Adição")
        print("4 - Subtração")
        print("0 - Sair")
        print("===========================")

        escolha = input("Selecione uma opção: ")

        print("===========================")

        try:

            escolha = int(escolha)

            if escolha == 1:

                resultado = numero_1 * numero_2
                print(f"| {numero_1} X {numero_2} = {resultado} |")

            elif escolha == 2:

                resultado = numero_1 / numero_2
                print(f"| {numero_1} / {numero_2} = {resultado} |")

                if numero_1 == 0 or numero_2 == 0:

                    print("Não é possivel dividir por zero.")

            elif escolha == 3:

                resultado = numero_1 + numero_2
                print(f"| {numero_1} + {numero_2} = {resultado} |")

            elif escolha == 4:

                resultado = numero_1 - numero_2
                print(f"| {numero_1} - {numero_2} = {resultado} |")

            elif escolha == 0:

                print("Saindo...")
                break

            else:
                print("Opção inválida, tente novamente!")

        except:
            print("Valor inválido, utilize apenas números.")

except:
    print("Valor inválido, utilize apenas números.")

# ==========================================================
# AULA 40 — CALCULADORA COM WHILE (RESUMO + ANÁLISE)
# ==========================================================

# 1️⃣ Objetivo da aula

# Criar uma calculadora que:
# - roda em loop (while True)
# - recebe dois números
# - recebe um operador
# - valida os dados
# - executa a conta
# - permite sair do programa

# ----------------------------------------------------------

# 2️⃣ Estrutura base

# while True:
#     pedir dados
#     validar dados
#     executar operação
#     perguntar se quer sair

# ----------------------------------------------------------

# 3️⃣ Validação de números

# Usamos try/except para evitar erro
# ao converter string para número.

# try:
#     num1 = float("10")
#     num2 = float("5")
#     numeros_validos = True
# except:
 #    numeros_validos = None

# Se der erro → números inválidos

# ----------------------------------------------------------

# 4️⃣ Validação de operador

# operadores_permitidos = '+-/*'
# 
# operador = '+'
# 
# if operador not in operadores_permitidos:
#     print("Operador inválido")
# 
# # Também validamos se tem apenas 1 caractere:
# 
# if len(operador) > 1:
#     print("Digite apenas um operador")
# 
# # ----------------------------------------------------------
# 
# # 5️⃣ Executando operações
# 
# num1 = 10
# num2 = 5
# operador = '+'
# 
# if operador == '+':
#     resultado = num1 + num2
# 
# elif operador == '-':
#     resultado = num1 - num2
# 
# elif operador == '*':
#     resultado = num1 * num2
# 
# elif operador == '/':
#     resultado = num1 / num2

# ----------------------------------------------------------

# 6️⃣ Saída do programa

# Transformamos input em boolean:

# sair = input("Quer sair? [s]im: ").lower().startswith('s')
# 
# if sair:
#     break

# ----------------------------------------------------------

# ==========================================================
# 🔎 ANÁLISE DO SEU CÓDIGO
# ==========================================================

# ✔️ PONTOS FORTES:

# ✔️ Você usou menu (nível mais avançado que a aula)
# ✔️ Usou try/except (muito bom)
# ✔️ Código organizado e legível
# ✔️ Usou operações corretamente

# 👉 Você foi além da aula, isso é MUITO bom.

# ----------------------------------------------------------

# ⚠️ PONTOS PARA MELHORAR:

# 1️⃣ Divisão por zero (lógica invertida)

# Seu código:

# elif escolha == 2:
#     resultado = numero_1 / numero_2
#     print(...)
#     
#     if numero_1 == 0 or numero_2 == 0:
#         print("Não é possivel dividir por zero.")
# 
# ❌ Problema:
# você faz a divisão ANTES de validar

# ✔️ Correto:

# elif escolha == 2:
#     if numero_2 == 0:
#         print("Não é possível dividir por zero.")
#     else:
#         resultado = numero_1 / numero_2
#         print(...)

# ----------------------------------------------------------

# 2️⃣ Opção de saída inconsistente

# Você mostrou:

# 0 - Sair

# Mas no código:

# elif escolha == 5:
#     break
# 
# # ❌ Isso é bug
# 
# # ✔️ Corrigir:
# 
# elif escolha == 0:
#     print("Saindo...")
#     break
# 
# ----------------------------------------------------------

# 3️⃣ Inputs fora do loop

# Você pede os números ANTES do while

# ❌ Isso faz com que:
# o usuário não consiga mudar os números depois

# ✔️ Melhor prática:

# while True:
#     numero_1 = input(...)
#     numero_2 = input(...)

# ----------------------------------------------------------

# 4️⃣ Conversão para int limita o programa

# Você usou:

# numero_1 = int(numero_1)

# ❌ Limita para inteiros

# ✔️ Melhor:

# numero_1 = float(numero_1)

# Aceita números decimais

# ----------------------------------------------------------

# 5️⃣ Uso de except genérico

# Você usou:

# except:

# ⚠️ Funciona, mas não é ideal

# ✔️ Melhor prática futura:

# except ValueError:

# ----------------------------------------------------------

# ==========================================================
# 💡 VERSÃO MELHORADA DO SEU CÓDIGO
# ==========================================================

# while True:
# 
#     try:
#         numero_1 = float(input("Escolha o primeiro número: "))
#         numero_2 = float(input("Escolha o segundo número: "))
#     except:
#         print("Valor inválido, utilize apenas números.")
#         continue
# 
#     print("\n====== Calculadora ======")
#     print("1 - Multiplicação")
#     print("2 - Divisão")
#     print("3 - Adição")
#     print("4 - Subtração")
#     print("0 - Sair")
#     print("===========================")
# 
#     escolha = input("Selecione uma opção: ")
# 
#     try:
#         escolha = int(escolha)
#     except:
#         print("Opção inválida.")
#         continue
# 
#     if escolha == 0:
#         print("Saindo...")
#         break
# 
#     elif escolha == 1:
#         print(f"{numero_1} x {numero_2} = {numero_1 * numero_2}")
# 
#     elif escolha == 2:
#         if numero_2 == 0:
#             print("Não é possível dividir por zero.")
#         else:
#             print(f"{numero_1} / {numero_2} = {numero_1 / numero_2}")
# 
#     elif escolha == 3:
#         print(f"{numero_1} + {numero_2} = {numero_1 + numero_2}")
# 
#     elif escolha == 4:
#         print(f"{numero_1} - {numero_2} = {numero_1 - numero_2}")
# 
#     else:
#         print("Opção inválida.")

# ----------------------------------------------------------

# 7️⃣ Conclusão

# Você já está em um nível MUITO bom porque:

# - criou lógica própria
# - adaptou o exercício
# - organizou código
# - pensou como programador

# Isso é exatamente o que devs fazem no dia a dia.