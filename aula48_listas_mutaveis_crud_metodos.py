"""
Listas em Python
"""
# Aula 48.1

# lista = [123, True, "Jonas", 1.2]
# print(lista[2].upper())

# lista[2] = "Salamalegosala"
# lista[0] = "Salamalegosala"
# print(lista[2].upper())
# print(lista[0])


# for i, itens in enumerate(lista):

#     print(f"[{i}] |{itens}")

# Aula 48.2

# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(lista)
# del lista[1]
# print(lista)
# lista.append(110)
# lista.append(120)
# print(lista)
# lista.pop()
# print(lista)

# Aula 48.3

# Tipo list - Mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis- índices e fatiamento
# Métodos úteis:
# append - Adiciona um item ao final
# insert - Adiciona um item no índice escolhido
# pop - Remove do final ou do índice escolhido
# del - apaga um índice
# clear - limpa a lista
# extend - estende a lista
# + - concatena listas
# Create Read Update Delete
# Criar, ler, alterar, apagar = lista[i](CRUD)


# lista_a = [10, 20, 30]
# lista_b = [40, 50, 60]
# lista_c = lista_a + lista_b ## Concatena duas ou mais lista
# lista_d = lista_a.extend(lista_b) ## Mexe diretamente na lista B, não retorna nada (ira juntar a lista A e B)
# print(lista_a)

# Aula 48.4

# Cuidados com dados mutáveis
# copiado o valor(imutáveis)
# =- aponta para o mesmo valor na memória (mutável)

# nome = "Fabrício"
# outro_valor = nome
# nome = "Souza"

# print(nome)
# print(outro_valor)

lista_1 = ["Souza", "Alves"]
lista_2 = lista_1.copy() # Lista copiada

lista_1[0] = "Outro" 

print(lista_2)
print(lista_1)