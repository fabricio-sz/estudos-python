lista_original = [10, 15, 20, 25, 30, 35, 40]
lista_filtrada_par = []
lista_filtrada_impar = []

for item in lista_original:
    
    if (item % 2 == 0) and (item > 20):
        print(f"Item: {item} é PAR e maior que 20.")
        lista_filtrada_par.append(item)

    if (item % 2 != 0) and (item > 20):
        print(f"Item: {item} é ÍMPAR e maior que 20.")
        lista_filtrada_impar.append(item)

print(f"Lista filtrada (Par): {lista_filtrada_par}")
print(f"Lista filtrada (Ímpar): {lista_filtrada_impar}")
