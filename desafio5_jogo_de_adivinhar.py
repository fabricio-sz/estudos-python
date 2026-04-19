## Informar o numero secreto
## Pedir o numero para o usuario

## Validar se o numero é igual, se não, informar se é e menos ou mais
## Ultima verificação para o acerto

numero_secreto = 8
tentativa = int(input("Digite sua tentativa: "))

if (tentativa > numero_secreto):

    print(f"Você escolheu o numero {tentativa}, é maior que o numero secreto")

elif (tentativa < numero_secreto):

    print(f"Você escolheu o numero {tentativa}, é menor que o numero secreto")

else:

    print(f"Parabens! Você escolheu o numero {tentativa}, está correto!!!")