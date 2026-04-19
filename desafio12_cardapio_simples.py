## Cardapio simples
## Menu com escolhas de produtos
## Usuario seleciona o item do menu
## Cada item tem valor unitario
## Enquanto o usuario não selecionar o item "Finalizar compra" ele repeti e acrescenta o valor de cada item no valor total
## Variveis: QTD_PROD, VLR_UNIT, VLR_TOTAL
## Cada item será criado uma variavel

item_1 = "Pão"
item_2 = "Café"
vlr_item_1 = 2.50
vlr_item_2 = 1.50
vlr_total = 0
qtd_item_1 = 0
qtd_item_2 = 0

esc_menu = " "

while True:

    print("================== Cardapio ==================")
    print(f"[1] - {item_1} | R$ {vlr_item_1:.2f}")
    print(f"[2] - {item_2} | R$ {vlr_item_2:.2f}")
    print(f"[0] - Finalizar compra")
    print("==============================================")

    esc_menu = input("Selecine uma opção: ")

    try:

        esc_menu = int(esc_menu)

        if esc_menu == 1:
            
            qtd = int(input(f"{item_1} | R$ {vlr_item_1:.2f} | Digite a quantidade: "))
            qtd_item_1 += qtd
            vlr_total += qtd * vlr_item_1
            print(f"{item_1} | R$ {vlr_item_1:.2f} | Quantidade: {qtd_item_1}")

        elif esc_menu == 2:

            qtd = int(input(f"{item_2} | R$ {vlr_item_2:.2f} | Digite a quantidade: "))
            qtd_item_2 += qtd
            vlr_total += qtd * vlr_item_2
            print(f"{item_2} | R$ {vlr_item_2:.2f} | Quantidade: {qtd_item_2}")
    
        elif esc_menu == 0:

            print("================================== Nota Fiscal ==================================")

            if qtd_item_1 > 0:
                print(f"[1] - {item_1} | Valor unitario: R$ {vlr_item_1:.2f} | Quantidade: {qtd_item_1}")

            if qtd_item_2 > 0:
                print(f"[2] - {item_2} | Valor unitario: R$ {vlr_item_2:.2f} | Quantidade: {qtd_item_2}")

            print(f"Valor total: R$ {vlr_total:.2f}")
            print("=================================================================================")

            break

        else:

            print("Opção inválida, tente novamente.")
    
    except ValueError:

        print("Valor digitado inválido, somente números são permitidos.")