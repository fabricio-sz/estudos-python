# 🔥 Desafio 1
# Peça números até o usuário digitar 0
# Mostre:
# quantos números foram digitados
# a soma deles

soma = 0 ## Inicio da soma é 0, será inclementado conforme usuario digitar
numero = " " # Definindo como vazio
contador = 0 ## Contara a quantidade de vezes que o usuario digitou

while numero != 0:
    numero = input("Digite um numero: ")

    try:
        numero = int(numero)

        if numero == 0:
            break

        contador += 1
        soma += numero ## Pega a soma, acrescenta o valor de numero
        print(f"Soma até o momento: {soma}")

    except:
        print("Utilize somente valores inteiros.")

print(f"Soma total: {soma} | Números digitados: {contador}")