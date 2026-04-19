a = "AB"
b = "BC"
c = 4.5

# string = "a = {} | b = {} | c = {:.2f}" ## Acessando por ordem
## string = "a = {0} | b = {1} | c = {2:.2f}" ## Acessando por indice
string = "a = {nome1} | b = {nome2} | c = {nome3:.2f}" ## Acessando por parametro nomeado

# formato = string.format(a, b, c)
formato = string.format(nome1 = a, nome2 = b, nome3 = c)

print(formato)