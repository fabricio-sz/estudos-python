"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

Exercicio 01
"""

num_inteiro = input("Digite um numero inteiro: ")

try:

     num_inteiro = int(num_inteiro) ## Dentro do Try transformando ele em inteiro

     if num_inteiro % 2 == 0 : ## Se o resto da divisão for igual a Zero

         print(f"O número {num_inteiro} é par.")

     else:

         print(f"O número {num_inteiro} é ímpar.")

except:

         print(f"O número digitado não é um numero inteiro.")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudaçao apropriada  Ex
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23 

Exercicio 02
"""

horario = input("Qual é o horario atual? ")
minutos = input("Quantos minutos? ")

try:
     
    horario = int(horario)
    minutos = int(minutos)

    horario_manha = (horario >= 0 and horario <= 11) and (minutos > 0 and minutos <= 59)
    horario_tarde = (horario >= 12 and horario <= 17) and (minutos > 0 and minutos <= 59)
    horario_noite = (horario >= 18 and horario <= 23) and (minutos > 0 and minutos <= 59)

    if horario_noite:

        print(f"Boa noite! | {horario}h{minutos}")
    
    elif horario_tarde:

        print(f"Boa tarde! | {horario}h{minutos}")

    elif horario_manha:

        print(f"Bom dia! | {horario}h{minutos}")

    else:

        print("Horario digitado invalido!")

except:
     
     print("Valor digitado invalido, apenas números.")

"""
Faça  um programa que peca o primeiro nome do usuario Se o nome tiver 4 letras ou
menos  escreva  "Seu  nome  e curto"; se tiver entre 5 e 6 letras, escreva
"Seu  nome e normal"; maior que 6 escreva "Seu nome e muito grande" 

Exercicio 03
"""

nome = input("Digite seu primeiro nome: ")

try:
     
     nome_curto = len(nome) <= 4
     nome_normal = len(nome) >= 5 and len(nome) <= 6
     nome_longo = len(nome) > 6
     qt_caracter = len(nome)

     if nome_longo:
          
          print(f"Seu nome é {nome} e possue {qt_caracter} caracteres, ele é muito grande.")

     if nome_normal:
          
          print(f"Seu nome é {nome} e possue {qt_caracter} caracteres, ele é normal.")

     if nome_curto:
          
          print(f"Seu nome é {nome} e possue {qt_caracter} caracteres, ele é curto.")

except:
     
     print("Valor invalido, utilize apenas texto.")
