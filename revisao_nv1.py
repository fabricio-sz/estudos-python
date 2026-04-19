# 🔁 🔹 Nível 1 — Aquecimento (básico)

# Faz rápido, sem pensar muito.

# 1.

# Crie uma lista com 5 números e mostre todos eles com for.

# 👉 Esperado:

# 1
# 2
# 3
# 4
# 5
# 2.

# Some todos os números de uma lista usando for.

# 👉 Exemplo:

# [10, 20, 30] → 60
# 3.

# Conte quantos números pares existem na lista.

# 👉 Dica:

# if numero % 2 == 0

lista = [1,2,3,4,5]
soma = 0
pares = []
for numero in lista:
    soma += numero
    print(numero)

    if numero % 2 == 0:
        pares.append(numero)


print(f"Soma total: {soma}")
print(f"Pares: {len(pares)}")