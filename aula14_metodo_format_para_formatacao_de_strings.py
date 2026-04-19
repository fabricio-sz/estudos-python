a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)

# ==========================================================
# AULA 14 — Método .format() para formatação de strings
# ==========================================================

# 1️⃣ O que essa aula ensina?
# - Outra forma de formatar strings usando o método .format().
# - Como inserir valores dentro de uma string usando chaves {}.

# 2️⃣ Conceito principal:
# - Strings são objetos em Python.
# - Objetos possuem métodos (funções internas).
# - format() é um método da string usado para substituir valores nas {}.

# 3️⃣ Formas de usar o format():

# 🔹 Por ordem:
#   string = "a={} b={}".format(a, b)
#   -> A primeira {} pega o primeiro argumento.
#   -> A segunda {} pega o segundo argumento.

# 🔹 Por índice:
#   string = "a={0} b={1}"
#   -> 0 é o primeiro argumento.
#   -> 1 é o segundo argumento.
#   -> Índices começam em 0.

# 🔹 Por parâmetro nomeado (mais organizado):
#   string = "a={nome1} b={nome2}"
#   string.format(nome1=a, nome2=b)
#   -> Mais legível e não depende da ordem.

# 4️⃣ Formatação de números:
# - Pode usar : dentro das chaves.
# - Exemplo: {valor:.2f}
#   -> Mostra 2 casas decimais.

# 5️⃣ Erro comum:
# - Se houver mais {} do que argumentos no format(),
#   ocorre erro "out of range".
# - Isso significa que você tentou acessar algo que não existe.

# 6️⃣ Regra importante:
# - Se usar parâmetro nomeado uma vez,
#   todos os próximos argumentos também devem ser nomeados.

# 7️⃣ Observação:
# - f-strings são mais modernas e mais usadas hoje.
# - format() ainda é muito útil e aparece em códigos antigos.