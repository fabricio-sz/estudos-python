## Nome do produto
## Quantidade total para separar
## Quantidade da embalagem
## Pallet fechado

## Embalagem fechada: QT_TOTAL // QT_EMB
## Embalagem fracionada: QT_TOTAL % QT_EMB
## Pallet fechado: QT_TOTAL // QT_PALLET 
## Pallet fracionado: (QT_TOTAL % QT_PALLET) // QT_EMB 

## Verifica se a quantidade total é maior que um pallet fechado, retorna o resto de embalagem fechada e a quantidade avulsa.
## Verificar se a embalagem fracionada é maior que 0 e se o pallet fechado é maior que 0
## Else usado para quando não ha resto da divisão entre embalagem e quantidade total

## Exibir a quantidade total, quantidade da embalagem, quantidade do pallet
## Quantos pallets fechados, quantas embalagens fechadas, unidades avulsas
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


