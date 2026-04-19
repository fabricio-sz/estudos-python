inicio_tabuada = ""
final_tabuada = ""
numero = ""

while True:

    
    numero = input("Digite o numero para gerar a tabuada: ")
    inicio_tabuada = input("Digite o numero inicial da tabuada: ")
    final_tabuada = input("Digite o numero final da tabuada: ")

    try:
        numero = int(numero)
        inicio_tabuada = int(inicio_tabuada)
        final_tabuada = int(final_tabuada)

        if inicio_tabuada > final_tabuada:

            print("Slk truta, tá chapadão jão")
            continue

        for i in range(inicio_tabuada, final_tabuada + 1): ## Esse "+1" é uma gambiarra kkkkkkk
            print(f"{numero} X {i} = {numero * i}")
            
        continuar = input("Deseja continuar Sim [s] | Não [n] ?: ")

        if continuar.lower() == "s":
            print("Calma aê paizão...")
            continue

        elif continuar.lower() == "n":
            print("e nóis na pista jão, tmj...")
            break

        else:
            print("que ? fala português alienigina fdp")
    
    except ValueError:

        print("Valor digitado inválido, tente apenas números!")