lista_numeros = [50, 60, 10, 30, 11, 99]
maior_numero = lista_numeros[0]
menor_numero = lista_numeros[0]

for numero in lista_numeros:
    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero

print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")

# =====================================================
# Segundo maior número
# =====================================================

lista_numeros = [1, 2, 3, 4, 5]
maior_numero = lista_numeros[0]
segundo_maior = lista_numeros[0]

for numero in lista_numeros:

    if numero > maior_numero:
        segundo_maior = maior_numero
        maior_numero = numero

    elif numero > segundo_maior:
        segundo_maior = numero

print(f"Maior número: {maior_numero}")
print(f"Segundo maior número: {segundo_maior}")

