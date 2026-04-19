

entrada = input("Entrar [E] ou Sair [S]? ")
senha_usuario = input("Digite sua Senha: ")

senha_correta = "123"

if (entrada == "E" or entrada == "e") and senha_usuario == senha_correta: ## Usando o or, apenas uma das condições precisam ser verdadeira

    print("Seja bem vindo!")

else:

    print("Saindo...")

teste = input("Testar ?") or "Teste isso então"
print(teste)