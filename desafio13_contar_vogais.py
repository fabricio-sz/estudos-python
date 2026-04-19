## Contar vogais em uma palavra
## 1 - Variavel com as vogais: "bcdfghjklmnpqrstvwxyz"
## 2 - Variavel com as consoantes: "aeiou"
## 3 - Variavel com a palavra escolhida
## 4 - Usar o for para percorrer a palavra
## 5 - Verificar se na variavel da palavra tem algum caracter da variavel de vogal

vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"
palavra = "rebimboca"
vogais_em_palavra = ""
consoantes_em_palavra = ""
contador_vogal = 0
contador_consoante = 0

for letra in palavra:

    if letra in vogais:
        contador_vogal += 1
        vogais_em_palavra += f"[{letra}]"

    elif letra in consoantes:
        contador_consoante += 1
        consoantes_em_palavra += f"[{letra}]"



print(f"A palavra: {palavra} possui {contador_vogal} vogais.")
print(f"A palavra: {palavra} possui {contador_consoante} consoantes.")
print(f"Palavra apenas com Vogais: {vogais_em_palavra}")
print(f"Palavra apenas com Consoantes: {consoantes_em_palavra}")