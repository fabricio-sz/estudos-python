texto = "Concistência todos os dias."
texto_split = texto.split(" ")
print(texto_split)

for i, palavra in enumerate(texto_split):
    print(f"[{i}] | {palavra}")


frase_unida = " ".join(texto_split)
print(frase_unida)