## Valor do saque para sacar
## Dividir o valor pela nota 100, nisso gera a quantidade de notas de 100
## 

valor_saque = int(input("Digite valor do saque: "))

nota_100 = 100
nota_50 = 50
nota_20 = 20
nota_10 = 10
nota_5 = 5
nota_2 = 2

divisao_nt100 = valor_saque // nota_100

resto_nt100 = valor_saque % nota_100
resto_nt50 = resto_nt100 % nota_50
resto_nt20 = resto_nt50 % nota_20
resto_nt10 = resto_nt20 % nota_10
resto_nt5 = resto_nt10 % nota_5

troco_100 = resto_nt100 // nota_50
troco_50 = resto_nt50 // nota_20
troco_20 = resto_nt20 // nota_10
troco_10 = resto_nt10 // nota_5
troco_5 = resto_nt5 // nota_2


print(f"Nota de R$ 100: {divisao_nt100}")
print(f"Nota de R$ 50: {troco_100}")
print(f"Nota de R$ 20: {troco_50}")
print(f"Nota de R$ 10: {troco_20}")
print(f"Nota de R$ 5: {troco_10}")
print(f"Nota de R$ 2: {troco_5}")


