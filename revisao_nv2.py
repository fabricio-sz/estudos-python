## Nivel 2: PT4

# numero_final = 10
# contagem = 0

# while contagem <= numero_final:

#     print(f"Número: {contagem}")
#     contagem += 1

######################################

## Nivel 2: PT5

# soma = 0

# while True:

#     escolha = input("Digite um número: ")

#     try:
#         escolha = int(escolha)
#         print(f"Número digitado: {escolha}")

#         if escolha == 0:
#             print(f"Soma total dos números digitados: {soma}")
#             break

#         soma += escolha

#     except ValueError:
#         print("Valor digitado inválido.")

######################################

## Nivel 2: PT6

# Faça um sistema que só aceita senha correta.

# 👉 Regras:

# Senha = 1234
# Enquanto errar, pede de novo
# Quando acertar: "Acesso liberado"

# senha = "1234"
# contador = 0

# while True:

#     entrada = input("Digite a senha para entrar: ")

#     if entrada == senha:
#         print("Login realizados com sucesso!")
#         break
    
#     else:
#         print("Senha incorreta, tente novamente!")
#         contador += 1
#         print(f"Tentativas: {contador}")

#         if contador == 3:
#             print("Feitas 3 tentativas, sistema bloqueado.")
#             break




