"""
Interpolação básica de string

s - String
d e i - Int
f - Float
x e X - Hexadecimal (ABCDEF0123456789)

"""

nome = "Jorge"
preco = 95.63
variavel = "%s, o preço é R$ %.2f" % (nome, preco)

print(variavel)

print("O hexadecimal de %d é de %08X" % (96, 96))