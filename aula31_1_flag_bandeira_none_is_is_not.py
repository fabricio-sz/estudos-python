"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')

# ==========================================================
# AULA 30.1 — FLAG (BANDEIRA), NONE, IS e IS NOT
# ==========================================================

# 1️⃣ Conceito de algoritmo

# Um algoritmo é uma sequência de passos
# para resolver um problema.

# Tudo que estamos programando até agora
# são algoritmos.

# ----------------------------------------------------------

# 2️⃣ O problema apresentado

# Às vezes queremos saber se o interpretador
# passou por um determinado ponto do código.

# Exemplo de situação:
# saber se entrou dentro de um IF.

# ----------------------------------------------------------

# 3️⃣ Uma solução ruim

# Criar uma variável dentro do IF e usar fora dele.

# Problema:
# se a condição do IF não for executada,
# a variável nunca será criada.

# Isso gera erro:
# NameError (variável não definida)

# ----------------------------------------------------------

# 4️⃣ A solução correta

# Declarar a variável antes do IF.

# Assim ela sempre existirá,
# independente da condição.

# ----------------------------------------------------------

# 5️⃣ Uso de None

# None representa "nenhum valor".

# É usado quando queremos indicar que
# uma variável ainda não recebeu valor.

# Exemplo conceitual:

# passou_no_if = None

# ----------------------------------------------------------

# 6️⃣ Funcionamento da Flag (Bandeira)

# A variável funciona como uma bandeira.

# Ela indica se determinado trecho
# do código foi executado ou não.

# Fluxo lógico:

# passou_no_if = None   → ainda não passou no IF

# se a condição for verdadeira:
# passou_no_if = True   → passou no IF

# ----------------------------------------------------------

# 7️⃣ Verificação usando "is"

# Em Python usamos "is" para verificar
# identidade de objetos.

# Especialmente com None.

# Exemplo conceitual:

# if passou_no_if is None

# Significa:
# "a variável ainda não recebeu valor"

# ----------------------------------------------------------

# 8️⃣ Uso de "is not"

# "is not" faz a verificação inversa.

# Exemplo:

# if passou_no_if is not None

# Significa:
# "a variável já recebeu valor"

# ----------------------------------------------------------

# 9️⃣ Por que usar "is" com None

# Comparações com None são feitas com "is"
# porque estamos verificando identidade,
# não apenas valor.

# Exemplo correto:

# variavel is None
# variavel is not None

# ----------------------------------------------------------

# 🔟 O conceito de Flag

# Uma FLAG é uma variável usada para marcar
# se algo aconteceu ou não.

# Exemplo de uso comum:

# verificar se entrou em um bloco
# verificar se um processo terminou
# verificar se um erro aconteceu

# ----------------------------------------------------------

# 11️⃣ Vantagem dessa abordagem

# A variável sempre existe no código.

# Isso evita erros e deixa o fluxo
# do programa mais claro.

# ----------------------------------------------------------

# 12️⃣ Relação com identidade (id)

# Toda variável aponta para um objeto
# na memória.

# Quando usamos "is",
# estamos comparando a identidade
# do objeto.

# Exemplo conceitual:

# passou_no_if is None

# Significa:
# a variável aponta para o objeto None.

# ----------------------------------------------------------

# 13️⃣ Conclusão

# None → indica ausência de valor

# is → verifica identidade

# is not → verifica identidade inversa

# Flag → variável usada para marcar
# se algo aconteceu no código