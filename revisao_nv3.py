#Nível 3 — Listas + lógica
# 7.

# Dada uma lista:

# [3, 7, 2, 9, 5]

# Mostre:

# Maior número
# Menor número

# 👉 Sem usar max() ou min()

# lista = [1, 2, 3, 4, 5]
# maior = lista[0]
# menor = lista[0]


# for numero in lista:

#     if numero > maior:
#         maior = numero

#     if numero < menor:
#         menor = numero

# print(f"Maior número da lista: {maior}")
# print(f"Menor número da lista: {menor}")

######################################

# 8.

# Crie uma lista vazia e peça 5 números ao usuário, depois mostre a lista.

# lista = []
# soma = 0


# while True:
#     numero = input("Digite um número: ")

#     try:
#         numero = int(numero)
#         lista.append(numero)
#         soma += numero

#         if len(lista) == 5:
#             maior = lista[0]
#             menor = lista[0]

#             for n in lista:

#                 if n > maior:
#                     maior = n

#                 if n < menor:
#                     menor = n
  
#             print(f"Números digitados: {lista}")
#             print(f"Maior número digitado: {maior}")
#             print(f"Menor número digitado: {menor}")
#             print(f"Soma total da lista: {soma}")
#             break

#     except ValueError:
#         print("Valor digitado inválido.")

######################################

#Nível 4 — Misturando tudo (nível real)
# 10.

# Faça um sistema com menu:

# 1 - Adicionar número
# 2 - Mostrar lista
# 3 - Mostrar soma
# 4 - Sair

# 👉 Regras:

# Use while
# Guarde números em lista
# Continue rodando até escolher sair

lista_numeros = []
soma = 0

while True:

    print("[1] | Adicionar número")
    print("[2] | Mostrar lista")
    print("[3] | Mostrar números pares")
    print("[4] | Mostrar números ímpares")
    print("[5] | Mostrar soma")
    print("[6] | Sair\n")

    entrada = input("Escolha uma opção: ")

    try:
        escolha = int(entrada)

        if escolha == 1:
            numero = int(input("Digite um número para colocar na lista: "))

            if numero in lista_numeros:
                print(f"Número {numero} já foi adicionado na lista.\n")

            else:
                lista_numeros.append(numero)
                soma += numero
                print(f"Número {numero} adicionado na lista.\n")

        elif escolha == 2:

            if len(lista_numeros) == 0:
                print("Lista está vazia.\n")

            else:
                print(f"Lista de números: {lista_numeros}")

        elif escolha == 3:

            for item in lista_numeros:

                if item % 2 == 0:
                    print(f"Número PAR: {item}")

                else:
                    print("Não há números pares nessa lista.\n")
                    continue

        elif escolha == 4:

            for item in lista_numeros:

                if item % 2 != 0:
                    print(f"Número ÍMPAR: {item}")

                else:
                    print("Não há números ímpares nessa lista.\n")
                    continue  

        elif escolha == 5:
            
            if len(lista_numeros) == 0:
                print("Não foi possivel somar, lista está vazia.\n")

            else:
                print(f"Soma de todos os números da lista: {soma}\n")

        else:
            print("Saindo...")
            break

    except ValueError:
        print("Valor digitado inválido.")