id_1 = "ABC" # Toda variavel criada gera um ID para o python
id_2 = "ABC" # Será o mesmo ID

print(id(id_1))
print(id(id_2))

# ==========================================================
# AULA 30 — IDENTIDADE DE OBJETOS (FUNÇÃO id)
# ==========================================================

# 1️⃣ O que acontece quando criamos uma variável

# Quando criamos uma variável em Python,
# estamos criando um "apelido" para um objeto
# que está armazenado na memória.

# Exemplo conceitual:
# v1 = "A"

# A variável v1 não guarda o valor diretamente.
# Ela aponta para um objeto que está na memória.

# ----------------------------------------------------------

# 2️⃣ Identidade de um objeto

# Cada objeto criado na memória possui
# uma identidade única.

# Essa identidade é como um "endereço"
# usado pelo Python para localizar o objeto.

# ----------------------------------------------------------

# 3️⃣ Função id()

# A função id() mostra a identidade
# (identificador único) de um objeto.

# Exemplo conceitual:

# id(objeto)

# Isso retorna um número que representa
# a identidade do objeto na memória.

# ----------------------------------------------------------

# 4️⃣ Objetos iguais podem compartilhar memória

# Em alguns casos, quando dois valores são iguais,
# o Python pode usar o mesmo objeto na memória
# para economizar recursos.

# Exemplo conceitual:

# v1 = "ABC"
# v2 = "ABC"

# Mesmo sendo duas variáveis diferentes,
# elas podem apontar para o mesmo objeto.

# Por isso:

# id(v1) == id(v2)

# pode ser True.

# ----------------------------------------------------------

# 5️⃣ Otimização do Python

# O Python tenta ser eficiente.

# Se dois valores literais são iguais,
# ele pode reutilizar o mesmo objeto
# em vez de criar outro.

# Isso economiza memória.

# ----------------------------------------------------------

# 6️⃣ Quando o valor muda

# Se mudarmos o valor de uma variável,
# ela passa a apontar para outro objeto.

# Exemplo conceitual:

# v2 = "B"

# Agora:

# v1 → aponta para "ABC"
# v2 → aponta para "B"

# Portanto os IDs serão diferentes.

# ----------------------------------------------------------

# 7️⃣ Importante entender

# Variáveis não guardam valores diretamente.

# Elas guardam uma referência
# para um objeto na memória.

# ----------------------------------------------------------

# 8️⃣ Conceitos envolvidos

# objeto
# identidade
# referência
# memória

# Esses conceitos serão importantes
# quando começarmos a trabalhar com:

# listas
# dicionários
# classes
# objetos personalizados

# ----------------------------------------------------------

# 9️⃣ Conclusão

# A função id() serve para ver
# qual objeto está sendo referenciado.

# Ela mostra a identidade do objeto
# na memória do Python.

# Isso ajuda a entender como o Python
# gerencia variáveis e objetos.