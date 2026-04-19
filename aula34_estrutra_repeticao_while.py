"""
Repetição = while (enquanto)
"""

numero_secreto = 93
tentativa = " "

while numero_secreto != tentativa: ## Enquanto número secreto for diferente que a tentyativa, se for igual ele para o laço de repeticao.

    tentativa = input("Qual o número secreto ? ")

    try:

        tentativa = int(tentativa) ## Variavel virou do tipo inteiro

        tentativa_correta = tentativa == numero_secreto
        tentativa_incorreta = tentativa != numero_secreto
        tentativa_incorreta_maior = (tentativa != numero_secreto) and (tentativa > numero_secreto)
        tentativa_incorreta_menor = (tentativa != numero_secreto) and (tentativa < numero_secreto)
        tentativa_maior_longe = tentativa_incorreta and tentativa > numero_secreto + 50
        tentativa_menor_longe = tentativa_incorreta and tentativa < numero_secreto - 50

        if tentativa_correta:
            print(f"Parabens, você acertou o número secreto!")

        elif tentativa_maior_longe:
            print("Nossa, esse número é muito maior que o número secreto")

        elif tentativa_menor_longe:
            print("Nossa, esse número é muito menor que o número secreto")

        elif tentativa_incorreta_menor:
            print("Ah não você errou, esse número é menor que o número secreto, tente novamente.")

        elif tentativa_incorreta_maior:
            print("Ah não você errou, esse número é maior que o número secreto, tente novamente.")


    except:

        print("Valor digitado inválido, somente utilize números.")
        