vogais = "aeiou"
palavra = "fabricio"
contador = 0

for letra in palavra:

    if letra in vogais:
        contador += 1

print(f"Palavra: {palavra}")
print(f"Quantiadade de vogais: {contador}")