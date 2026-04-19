# Faça uma lista de comprar com listas
# O usuário deve ter a possibilidade de
# inserir, apagar e listar valores da sua lista
# Não permita que o programa quebre com
# erros de índices inexistentes na lista.

lista_compras = []

while True:
    print("[1] - Inserir")
    print("[2] - Listar")
    print("[3] - Apagar")
    print("[0] - Sair\n")

    entrada = input("Selecione uma opção: ")

    try: 
        escolha = int(entrada)

        if escolha == 1:
            novo_item = input("Digite o nome do item: ")

            if novo_item in lista_compras:
                print(f"O item {novo_item} já está na lista.\n")

            else:
                lista_compras.append(novo_item)
                print(f"{novo_item} adicionado com sucesso!\n")

        elif escolha == 2:
            
            if len(lista_compras) == 0:
                print("Lista está vazia.\n")
            
            else:
                for i, item in enumerate(lista_compras):
                    print(f"[{i}] | {item}")
                print("\n")

        elif escolha == 3:

            if len(lista_compras) == 0:
                print("Lista está vazia, não há dados para apagar.\n")

            else:

                for i, item in enumerate(lista_compras):
                        print(f"[{i}] | {item}")

                apagar = input("Selecione o item para deletar: ")

                try:
                    apagar = int(apagar)

                    if apagar >= 0 and apagar <= len(lista_compras):
                        del lista_compras[apagar]
                        print("Item excluido da lista.")

                    else:
                        print("Item não está na lista.")


                except ValueError:
                    print("Valor ínvalido.")

        elif escolha == 0:
            print("Saindo...")
            break

        else:
            print("Opção ínvalida.")

    except ValueError:
        print("Valor digitado ínvalido, tente novamente")
