## Nome da pessoa
## Peso da pessoa
## Altura da pessoa

## IMC = peso / (altura ** 2)

## Verificar todas as condições da maior para a menor, else apenas para informações invalidas

## Exibir em forma bem simples cada informação

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / altura ** 2

if imc >= 40:

    print(f"| Nome: {nome} | Peso: {peso} | Altura: {altura} |")
    print(f"| IMC: {imc:.2f} | Classificação: OBESIDADE GRAVE III |")

elif imc >= 30 and imc <= 39.9:

    print(f"| Nome: {nome} | Peso: {peso} | Altura: {altura} |")
    print(f"| IMC: {imc:.2f} | Classificação: OBESIDADE II |")

elif imc >= 25 and imc <= 29.9:

    print(f"| Nome: {nome} | Peso: {peso} | Altura: {altura} |")
    print(f"| IMC: {imc:.2f} | Classificação: SOBREPESO I |")

elif imc >= 18.5 and imc <= 24.9:

    print(f"| Nome: {nome} | Peso: {peso} | Altura: {altura} |")
    print(f"| IMC: {imc:.2f} | Classificação: NORMAL 0 |")

elif imc < 18.5 and imc >= 0:

    print(f"| Nome: {nome} | Peso: {peso} | Altura: {altura} |")
    print(f"| IMC: {imc:.2f} | Classificação: MAGREZA 0 |")

else:

    print("Informações inválidas!")


