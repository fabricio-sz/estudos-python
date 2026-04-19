"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = "amor"
letras_acertadas = ""
tentativas = 0

while True:

    letra_digitada = input("Digite a letra: ")

    if len(letra_digitada) > 1:

        print("Insira apenas uma letra.")
        continue

    elif letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_criada = ""

    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_criada += letra

        else:
            palavra_criada += "*"
    
    print(palavra_criada)
    tentativas += 1

    if palavra_criada == palavra_secreta:

        print("Parabens, você conseguiu!")
        print(f"Tentativas: {tentativas}")
        break
