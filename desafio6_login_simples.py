## Solicitar nome do usuario
## Solicitar senha do usaurio

## Se nome e senha for igual aos cadastrados, login realizado
## Com logins realizado ele tem acesso a separação WMS

## Se não, sair

usuario_cadastrado = "fabricio.souza"
senha_cadastrada = "123!@"

nome = input("Nome de Usuario: ") 
senha = input("Senha do Usuario: ") 

if (nome == usuario_cadastrado) and (senha == senha_cadastrada): ## Utilizando um desafio anterior para usar no login, muito legal

    print("Login Realizado!")
    print("=============== WMS - ALVES EXPRESS =====================")

    nome_produto = input("Nome do Produto: ")
    qt_total = int(input("Quantidade total: "))
    qt_pallet = int(input("Quantidade do pallet: "))
    qt_emb = int(input("Quantidade da embalagem: "))

    emb_fechada = qt_total // qt_emb
    emb_fracionada = qt_total % qt_emb
    plt_fechado = qt_total // qt_pallet
    plt_fracionado = (qt_total % qt_pallet) // qt_emb ## (Resto da divisão entre quantidade total e quantidade pallet) resultado // por inteiro para a quantidade da embalagem

    if plt_fechado > 0:

        print("=============== WMS - ALVES EXPRESS =====================")
        print(f"| NOME_PROD: {nome_produto}")
        print(f"| QT_TOTAL: {qt_total}")
        print(f"| QT_EMB: {qt_emb}")
        print(f"| QT_PALLET: {qt_pallet}")
        print(f"| PLT_SEP: {plt_fechado}")
        print(f"| EMB_SEP: {plt_fracionado}")
        print(f"| QT_EMB_AVULSA: {emb_fracionada}")
        print("=========================================================")

    elif emb_fracionada > 0:

        print("=============== WMS - ALVES EXPRESS =====================")
        print(f"| NOME_PROD: {nome_produto}")
        print(f"| QT_TOTAL: {qt_total}")
        print(f"| QT_EMB: {qt_emb}")
        print(f"| QT_PALLET: {qt_pallet}")
        print(f"| PLT_SEP: {plt_fechado}")
        print(f"| EMB_SEP: {emb_fechada}")
        print(f"| QT_EMB_AVULSA: {emb_fracionada}")
        print("=========================================================")

    else:

        print("=============== WMS - ALVES EXPRESS =====================")
        print(f"| NOME_PROD: {nome_produto}")
        print(f"| QT_TOTAL: {qt_total}")
        print(f"| QT_EMB: {qt_emb}")
        print(f"| QT_PALLET: {qt_pallet}")
        print(f"| PLT_SEP: {plt_fechado}")
        print(f"| EMB_SEP: {emb_fechada}")
        print(f"| QT_EMB_AVULSA: {emb_fracionada}")
        print("=========================================================")

elif not nome or not senha:

    print("Nome ou senha não foram preecnhidos!")

else:

    print("Usuario ou Senha inválidos!")