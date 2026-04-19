nome = "Fabrício" ## Nome

posicao = 0
novo_nome = " "

while posicao < len(nome):

    letra = nome[posicao]
    novo_nome += f"*{letra}* "
    posicao += 1

print(novo_nome)