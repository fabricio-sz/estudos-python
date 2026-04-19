"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')


# # ==========================================================
# # AULA 54 — LISTA DE COMPRAS (VERSÃO PROFESSOR)
# # ==========================================================

# """
# Faça uma lista de compras com listas

# O usuário deve poder:
# - Inserir valores
# - Apagar valores
# - Listar valores

# O programa NÃO deve quebrar com erros
# """

# import os

# # ----------------------------------------------------------

# # 1️⃣ CRIAÇÃO DA LISTA

# lista = []

# # ----------------------------------------------------------

# # 2️⃣ LOOP PRINCIPAL

# while True:

#     print('Selecione uma opção')
#     opcao = input('[i]nserir [a]pagar [l]istar: ')

# # ----------------------------------------------------------

# # 3️⃣ INSERIR

#     if opcao == 'i':

#         # Limpa o terminal (Linux/Mac)
#         os.system('clear')

#         valor = input('Valor: ')
#         lista.append(valor)

# # ----------------------------------------------------------

# # 4️⃣ APAGAR

#     elif opcao == 'a':

#         indice_str = input('Escolha o índice para apagar: ')

#         try:
#             indice = int(indice_str)

#             # Remove o item pelo índice
#             del lista[indice]

#         # Usuário digitou algo que não é número
#         except ValueError:
#             print('Por favor digite número inteiro.')

#         # Índice não existe na lista
#         except IndexError:
#             print('Índice não existe na lista')

#         # Qualquer outro erro inesperado
#         except Exception:
#             print('Erro desconhecido')

# # ----------------------------------------------------------

# # 5️⃣ LISTAR

#     elif opcao == 'l':

#         os.system('clear')

#         # Lista vazia
#         if len(lista) == 0:
#             print('Nada para listar')

#         # enumerate → índice + valor
#         for i, valor in enumerate(lista):
#             print(i, valor)

# # ----------------------------------------------------------

# # 6️⃣ OPÇÃO INVÁLIDA

#     else:
#         print('Por favor, escolha i, a ou l.')

# # ==========================================================
# # 🧠 EXPLICAÇÃO DA AULA
# # ==========================================================

# """
# 1️⃣ while True
# → Mantém o sistema rodando

# 2️⃣ input()
# → Recebe comando do usuário

# 3️⃣ if / elif
# → Decide o que fazer

# 4️⃣ append()
# → Adiciona item na lista

# 5️⃣ del lista[indice]
# → Remove item pelo índice

# 6️⃣ enumerate()
# → Retorna índice + valor

# 7️⃣ try / except
# → Evita que o programa quebre
# """

# # ==========================================================
# # ⚠️ TRATAMENTO DE ERROS
# # ==========================================================

# """
# ValueError → usuário digitou texto
# IndexError → índice não existe
# Exception  → erro inesperado
# """

# # ==========================================================
# # 📌 PADRÃO CRUD
# # ==========================================================

# """
# Create → append()
# Read   → listar com for
# Delete → del lista[indice]
# """

# # ==========================================================
# # 💡 OBSERVAÇÃO

# """
# os.system('clear'):

# - Linux / Mac → clear
# - Windows → cls

# Se não funcionar:
# → troque 'clear' por 'cls'
# """

# # ==========================================================
# # 🚀 CONCLUSÃO

# """
# Esse código é um MINI SISTEMA real

# ✔ Entrada do usuário
# ✔ Manipulação de dados
# ✔ Tratamento de erro

# Se você entende isso:
# → Você já saiu do básico 🔥
# """