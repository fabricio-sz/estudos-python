"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite o seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:

    print(f"Seu nome é {nome}")
    print(f"Seu nome é {nome[::-1]}")

    if " " in nome:

        print(f"Seu nome contém espaços")

    else:

        print(f"Seu nome não contém espaços")

    print(f"Seu nome tem {len(nome)} letras.")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")

else:

    print("Desculpe, você deixou campos vazios.")


# ==========================================================
# AULA 28 — EXERCÍCIO COM STRINGS, CONDIÇÕES E FUNÇÕES
# ==========================================================

# 1️⃣ Objetivo do exercício

# Criar um pequeno programa que:
# - peça o nome do usuário
# - peça a idade do usuário
# - valide se os campos foram preenchidos
# - mostre algumas informações sobre o nome

# Esse exercício mistura vários conceitos
# aprendidos nas aulas anteriores.

# ----------------------------------------------------------

# 2️⃣ Entrada de dados

# O programa usa a função input() para
# receber informações do usuário.

# nome = input(...)
# idade = input(...)

# Essas informações são armazenadas
# em variáveis.

# ----------------------------------------------------------

# 3️⃣ Verificando se os campos foram preenchidos

# A condição usada foi:

# if nome and idade:

# Isso funciona porque strings vazias ("")
# são consideradas False em Python.

# Então:

# se o usuário não digitar nada
# a condição será False.

# Se ambos tiverem conteúdo
# a condição será True.

# ----------------------------------------------------------

# 4️⃣ Caso o usuário não digite nada

# Se algum campo estiver vazio,
# o programa entra no else.

# Exibe a mensagem:

# "Desculpe, você deixou campos vazios."

# ----------------------------------------------------------

# 5️⃣ Exibindo o nome

# Caso os dados existam,
# o programa mostra o nome digitado.

# Exemplo:

# print(f"Seu nome é {nome}")

# Usa f-string para inserir a variável.

# ----------------------------------------------------------

# 6️⃣ Invertendo o nome

# Para inverter o nome foi usado
# fatiamento de strings.

# nome[::-1]

# Explicação:

# inicio: vazio
# fim: vazio
# passo: -1

# Isso faz a string ser percorrida
# de trás para frente.

# ----------------------------------------------------------

# 7️⃣ Verificando se o nome tem espaço

# Para verificar espaços foi usado:

# " " in nome

# Isso verifica se existe um espaço
# dentro da string.

# Se existir → nome possui espaço
# Se não existir → nome não possui espaço

# ----------------------------------------------------------

# 8️⃣ Contando caracteres

# Foi usada a função len().

# len(nome)

# Essa função retorna a quantidade
# total de caracteres.

# Importante:

# espaços também contam como caractere.

# ----------------------------------------------------------

# 9️⃣ Pegando a primeira letra

# A primeira letra está no índice 0.

# nome[0]

# Porque os índices começam do zero.

# ----------------------------------------------------------

# 🔟 Pegando a última letra

# A última letra pode ser acessada
# com índice negativo.

# nome[-1]

# -1 sempre representa
# o último caractere.

# ----------------------------------------------------------

# 1️⃣1️⃣ Conceitos praticados nesse exercício

# input()
# if / else
# operadores lógicos
# operador in
# fatiamento de strings
# função len()
# índices positivos
# índices negativos
# f-strings

# ----------------------------------------------------------

# 1️⃣2️⃣ Conclusão

# Esse exercício é importante porque
# combina vários conceitos básicos
# do Python em um único programa.

# Esse tipo de exercício ajuda
# a fixar lógica de programação
# e manipulação de strings.