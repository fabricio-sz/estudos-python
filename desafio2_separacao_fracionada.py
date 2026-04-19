# nome do produto

# quantidade para separar
# quantidade da embalagem

# mostrar quantas embalagem para separar fechada
# mostrar quantas embalagem para separar fracionada

produto = input("Nome do produto: ")
separar = int(input("Quantidade para separar: "))
qtd_embalagem = int(input("Quantidade da embalagem: "))

resultado = separar // qtd_embalagem ## Resultado em numero inteiro
resultado_fracionado = separar % qtd_embalagem ## Resto da divisão com o restante a ser separado

if resultado % 2 == 0:

    print(f"| Produto: {produto}")
    print(f"| Quantidade: {separar}")
    print(f"| Embalagem para Separar: {resultado:.0f}")

else:

    print(f"| Produto: {produto}")
    print(f"| Quantidade: {separar}")
    print(f"| Embalagem para Separar: {resultado:.0f}")
    print(f"| Embalagem Fracionada: {resultado_fracionado:.0f}")