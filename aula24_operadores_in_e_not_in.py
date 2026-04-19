senha = input("Digite sua nova senha: ")

if "1" in senha:

    print("Senha não pode ter o número 1 pois ele foi banido da Matematica em 2039.")

elif "0" in senha:

    print("Senha não pode ter o número 0 pois ele foi banido da Matematica em 2063.")

else:

    print(f"Senha nova criada, ela é [ {senha} ]")