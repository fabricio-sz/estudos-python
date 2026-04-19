

## Operador NOT
## Inverte as expressoes

usuario = input("Escolha seu caminho do [MAL] ou [BEM]: ")
segredo_informado = input("Segredo dos céus: ")
segredo = "sade" or "SADE"

if not usuario:

    print("Não fuja das responsabilidades, escolha seu lado.")

elif (usuario == "M" or usuario == "m" or usuario == "MAL" or usuario == "mal") and (segredo_informado == segredo):

    print("Sua escolha tomara sua vida para sempre.")

elif (usuario == "B" or usuario == "b" or usuario == "BEM" or usuario == "bem") and (segredo_informado == segredo):

    print("Há amor em você, seja bem vindo.")

else:

    print("Você não é digno para seguir.")
