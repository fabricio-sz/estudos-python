
# Peça três números ao usuário e mostre qual é o maior deles.

# Exemplo:

# Digite o primeiro número: 5
# Digite o segundo número: 9
# Digite o terceiro número: 2

# O maior número é: 9

numero_1 = input("Digite o primeiro número: ")
numero_2 = input("Digite o segundo número: ")
numero_3 = input("Digite o terceiro número: ")

try:

    numero_1 = int(numero_1)
    numero_2 = int(numero_2)
    numero_3 = int(numero_3)

    
    numero_1_maior = numero_1 >= numero_2 and numero_1 > numero_3
    numero_2_maior = numero_2 >= numero_1 and numero_2 > numero_3
    numero_3_maior = numero_3 >= numero_1 and numero_3 > numero_2
    numeros_iguais = (numero_1 == numero_2 and numero_1 == numero_3) and (numero_2 == numero_1 and numero_2 == numero_3) and (numero_3 == numero_1 and numero_3 == numero_2)

    if numero_1_maior:

        print(f"Número {numero_1} é o primeiro número, ele é o maior número digitado")

    elif numero_2_maior:

        print(f"Número {numero_2} é o segundo número, ele é o maior número digitado")
    
    elif numero_3_maior:

        print(f"Número {numero_3} é o terceiro número, ele é o maior número digitado")

    elif numeros_iguais:

        print("Todos os números digitados são iguais.")

except:

    print("Apenas números são permitidos.")