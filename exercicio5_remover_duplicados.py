lista_duplicada = [11, 1, 1, 3, 2, 2, 10, 10, 6, 6, 6, 5, 4, 8, 9, 8, 9]
lista_unica = []

for item in lista_duplicada:

    if item not in lista_unica:
        lista_unica.append(item)
        print(f"Item {item} não estava na lista.")

print(f"Lista original: {lista_duplicada}")
print(f"Lista Corrigida: {lista_unica}")