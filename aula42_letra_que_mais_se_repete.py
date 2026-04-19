
frase = """Estrutura de repetição While.""".lower()
 

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = " "

while i < len(frase):

    letra_atual = frase[i]

    if " " in letra_atual:
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f"Letra que apareceu mais vezes: {letra_apareceu_mais_vezes}")
print(f"A letra: {letra_apareceu_mais_vezes}, aparece num total de {qtd_apareceu_mais_vezes} vezes.")

## .count() = Quantidade de palavras, ou letras
## .lower() = Deixa tudo em Minusculo
## .upper() = Deixa tudo em Maiusculo

