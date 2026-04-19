

entrada = input("Entrar [E] ou Sair [S]? ")
senha_usuario = input("Digite sua Senha: ")

senha_correta = "123"

if entrada == "E" and senha_usuario == senha_correta: ## Usando o and, as duas condições precisam ser verdadeira

    print("Seja bem vindo!")

else:

    print("Saindo...")