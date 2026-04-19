nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987

# ==========================================================
# AULA 13 — f-strings (Formatação de Strings)
# ==========================================================

# 1️⃣ O que essa aula ensina?
# - Como formatar strings de forma moderna usando f-strings.
# - Como inserir variáveis diretamente dentro do texto.
# - Como formatar números (casas decimais).

# 2️⃣ Conceito principal:
# - Colocar a letra f antes da string ativa a formatação.
#   Exemplo:
#   f"texto {variavel}"

# - Tudo que estiver dentro de {} será interpretado como variável ou expressão.

# 3️⃣ Por que usar f-strings?
# - Evita usar concatenação (+)
# - Evita usar vírgulas no print
# - Código fica mais legível e profissional

# 4️⃣ Formatação de números:
# - Para limitar casas decimais:
#   {variavel:.2f}
#
#   .2  -> quantidade de casas decimais
#   f   -> número float

# 5️⃣ Exemplos:
#   altura = 1.80
#   print(f"{altura:.2f}")  -> 1.80
#
#   print(f"{altura:.1f}")  -> 1.8
#   print(f"{altura:.5f}")  -> 1.80000

# 6️⃣ Também é possível formatar milhares:
#   {valor:,.2f}
# - Coloca separador de milhar automaticamente.

# 7️⃣ Observação importante:
# - Dentro das {} pode existir cálculo:
#   f"{peso / altura ** 2:.2f}"

# 8️⃣ Conclusão:
# - f-strings são a forma mais moderna e recomendada
#   para formatar strings em Python.