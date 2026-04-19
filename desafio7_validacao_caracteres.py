## Solicitar nome e senha

## Validar se no nome ou senha não foi inserido nada
## Nome e senha não pode ter espaços
## Senha tem que ter mais de 8 caracteres
## Senha deve possuir algum caracter especial

nome = input("Digite o nome: ")
senha = input("Digite a senha: ")

if not nome or not senha:

    print("Informações não foram preenchidas.")

elif (" " in nome) or (" " in senha):

    print("Nome e senha não pode ter espaços")

elif len(senha) < 8:

    print("Senha tem que ter mais de 8 caracteres")

elif "!" or "@" not in senha:

    print("Senha tem que ter algum caracter especial")

else:

    print(f"Nome: {nome} | Senha: {senha}")
    print(f"Primeira letra do nome é {nome[0]}.")
    print(f"Ultima letra do nome é {nome[-1]}.")
    print(f"Nome possui {len(nome)} letras.")
    print(f"Senha possui {len(senha)} caracteres.")
    print(f"Nome invertido é {nome[::-1]}.")