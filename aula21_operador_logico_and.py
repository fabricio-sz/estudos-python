# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)

# ==========================================================
# AULA 21 — OPERADOR LÓGICO AND
# ==========================================================

# 1️⃣ O que são operadores lógicos
# Operadores lógicos são usados para combinar condições.
# Eles permitem verificar mais de uma condição ao mesmo tempo.

# Operadores lógicos principais:
# and → E
# or  → OU
# not → NÃO

# Nesta aula foi estudado apenas o operador AND.

# 2️⃣ Operador AND
# O operador AND significa "E".

# Exemplo lógico:
# condição1 AND condição2

# Para que a expressão seja verdadeira,
# TODAS as condições precisam ser verdadeiras.

# Se qualquer condição for falsa,
# toda a expressão será falsa.

# 3️⃣ Uso comum
# AND é usado quando precisamos validar
# mais de uma condição ao mesmo tempo.

# Exemplo:
# verificar usuário E senha
# verificar idade E autorização
# verificar entrada E senha correta

# 4️⃣ Funcionamento dentro do IF
# O if executa o bloco de código apenas
# se a expressão completa for True.

# Se qualquer parte da expressão for False,
# o código entra no else.

# 5️⃣ Avaliação de curto-circuito
# Python usa algo chamado "short-circuit evaluation".

# Isso significa:
# Se uma condição já for falsa,
# o Python para de avaliar o resto da expressão.

# Exemplo lógico:
# True AND False AND True

# O Python para no False
# porque já sabe que o resultado final será False.

# Isso economiza processamento.

# 6️⃣ Valores considerados falsos (Falsy)
# Alguns valores não são False diretamente,
# mas são tratados como False em avaliações lógicas.

# Exemplos de valores falsy:

# False
# 0
# 0.0
# ''
# None

# 7️⃣ Valor None
# None representa "nenhum valor".

# É usado quando uma variável não possui valor.
# Também é considerado falsy em avaliações lógicas.

# 8️⃣ Conclusão
# O operador AND é usado para verificar múltiplas condições.
# Todas as condições precisam ser verdadeiras.
# Python usa avaliação de curto circuito para otimizar execução.