nome = str(input("Digite seu nome: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))


imc = peso / (altura * altura)

if imc >= 40:
    
    print(f"| {nome} | IMC: {imc:.2f} | CLASSIFICAÇÃO: OBESIDADE GRAVE III")

elif imc >= 30 and imc <= 39.9:

    print(f"| {nome} | IMC: {imc:.2f} | CLASSIFICAÇÃO: OBESIDADE II")
    
elif imc >= 25 and imc <= 29.9:

    print(f"| {nome} | IMC: {imc:.2f} | CLASSIFICAÇÃO: SOBREPESO I")

elif imc >= 18.5 and imc <= 24.9:

    print(f"| {nome} | IMC: {imc:.2f} | CLASSIFICAÇÃO: NORMAL 0")

elif imc >= 0.1 and imc < 18.5:

    print(f"| {nome} | IMC: {imc:.2f} | CLASSIFICAÇÃO: MAGREZA 0")

else:

    print("Informações invalidas!")