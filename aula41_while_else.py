string = "Letras Numericas"

indice = 0 ## Indice da letra

while indice < len(string): ## Enquanto o indice for menor que o tamanho da string

    letra = string[indice] ## Pecorrendo as letras, cada letra vai para uma variavel, a variavel letra

    if " " in letra: ## Caso tenha espaço em alguma letra, ele para

        break

    print(letra) ## Variavel letra apenas com um valor sendo exibida
    indice += 1 ## Inclementando para pecorrer as letras

else:
    print("Final do Else.")

print("Fora do Else.")

# palavra = "Rebimboca"
# i = 0 

# while i < len(palavra):

#     letra = palavra[i]
#     print(letra)
#     i += 1


