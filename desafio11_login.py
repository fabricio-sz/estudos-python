## Sistema basico de login
## Usuario: admin | Senha: 1234
## Perguntar para o usuario o usuario e senha
## Contar as tentativas com uma variavel
## Usar While para repetir até acertar

usuario = "admin"
senha = "1234"
contador = 0

while True:

    login_usuario = input("Digite o nome de Usuario: ")
    senha_usuario = input("Digite a senha do Usuario: ")
    senha_ou_usuario_incorreto = (login_usuario != usuario) or (senha_usuario != senha)

    if senha_ou_usuario_incorreto:

        contador += 1
        print("Senha ou usuario incorreto! Tente novamente.")
        print(f"Permitido apenas 3 tentativas, você tentou {contador} vezes.")

        if contador == 3:

            print("Foram feitas 3 tentativas, sistema bloqueado.")
            break

    else:

        print("Seja bem vindo!")
        break

