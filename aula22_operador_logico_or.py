# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)

# ==========================================================
# AULA 22 — OPERADOR LÓGICO OR
# ==========================================================

# 1️⃣ O que é o operador OR
# OR significa "OU".
# Ele é usado quando queremos que apenas UMA das condições seja verdadeira.

# Exemplo lógico:
# condição1 OR condição2

# Se qualquer uma das condições for True,
# a expressão inteira será considerada True.

# 2️⃣ Diferença entre AND e OR

# AND
# Todas as condições precisam ser verdadeiras.

# OR
# Apenas uma condição precisa ser verdadeira.

# 3️⃣ Uso comum
# O operador OR é usado quando queremos permitir
# múltiplas possibilidades para a mesma condição.

# Exemplos:
# usuário pode digitar E ou e
# usuário pode escolher opção A ou B
# validar dois possíveis valores de entrada

# 4️⃣ Uso de parênteses
# Quando misturamos operadores AND e OR
# a expressão pode ficar confusa.

# Para evitar ambiguidade usamos parênteses.

# Exemplo conceitual:
# (condição1 OR condição2) AND condição3

# Primeiro o Python avalia o que está dentro dos parênteses.

# 5️⃣ Avaliação de curto-circuito (Short-circuit)

# Python para de avaliar a expressão
# assim que encontra um valor que determina o resultado.

# Exemplo lógico:
# True OR False OR False

# O Python encontra True no primeiro valor
# e para a avaliação ali.

# 6️⃣ Valores considerados falsos (Falsy)

# False
# 0
# 0.0
# ''
# None

# Qualquer outro valor diferente desses
# será considerado True.

# 7️⃣ Retorno do OR
# O operador OR não retorna apenas True ou False.
# Ele retorna o valor que fez a expressão ser verdadeira.

# Exemplo conceitual:
# valor1 OR valor2

# Se valor1 for verdadeiro
# ele será retornado.

# Se valor1 for falso
# o Python retorna valor2.

# 8️⃣ Uso prático comum

# Podemos usar OR para definir valores padrão.

# Exemplo conceitual:
# valor = input() OR "valor padrão"

# Se o usuário não digitar nada
# o programa usa o valor padrão.

# 9️⃣ Conclusão
# OR é usado quando queremos aceitar
# múltiplas possibilidades em uma condição.

# Ele também permite criar expressões úteis
# usando avaliação de curto-circuito.