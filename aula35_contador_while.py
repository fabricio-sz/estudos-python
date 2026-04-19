
contador = input("Digite o valor inicial da contagem: ")
final_contador = input("Digite o valor final da contagem: ")
qtd_contagem = input("Digite o valor de quantos e quantos números deseja contar: ")

try:

    contador = float(contador) ## Valor inicial da contagem
    final_contador = float(final_contador) ## Valor final da contagem
    qtd_contagem = float(qtd_contagem) ## Valor de quantos em quantos deseja contar

    if contador >= final_contador:
        print("O valor do contador é o inicio da contagem, não pode ser igual ou maior que o valor final. ")

    elif final_contador > 1000:
        print("Insira um valor menor, muito alto para o sistema.")

    elif qtd_contagem >= final_contador:

        print("Valor da quantidades que deseja contar não pode ser maior ou igual ao valor final da contagem.")

    elif qtd_contagem <= 0:

        print("Valor da quantidade não pode ser zero ou negativo.")

    else:

        while contador <= final_contador:

            print(f"Contagem: [ {contador:.2f} ]")
            contador = contador + qtd_contagem


except:

    print("Texto em contador amigo ? somente utilize números meu caro.")

print("Final do laço While.")

