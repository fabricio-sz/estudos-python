# if / elif      / else
# se / se não se / se não

condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')

# ==========================================================
# AULA 18 — DEBUGGER (DEPURAÇÃO DE CÓDIGO)
# ==========================================================

# 1️⃣ O que é Debug?
# "Bug" significa erro.
# "Debug" significa remover erro (depurar).
# É o processo de analisar o código passo a passo.

# 2️⃣ O que é Debugger?
# Ferramenta que permite executar o código linha por linha.
# Ajuda a entender exatamente como o interpretador está lendo o programa.

# 3️⃣ Breakpoint
# É um ponto de parada no código.
# O interpretador para antes de executar aquela linha.
# Permite analisar o estado do programa naquele momento.

# 4️⃣ Como o Python executa o código
# O interpretador lê:
# - Da esquerda para a direita
# - De cima para baixo
# - Linha por linha

# 5️⃣ Step Over
# Executa uma linha por vez.
# Permite visualizar:
# - Qual linha está sendo executada
# - Quais variáveis já existem
# - Quais valores elas possuem

# 6️⃣ Debug e estruturas condicionais (if / elif / else)

# Quando o interpretador encontra um if:
# - Ele testa a condição.
# - Se for verdadeira → executa o bloco.
# - Depois sai da estrutura.
# - Não testa os próximos elif.

# Se for falsa:
# - Testa o próximo elif.
# - Continua até encontrar uma condição verdadeira.
# - Se nenhuma for verdadeira → executa o else.

# 7️⃣ Apenas um bloco é executado
# Dentro de um conjunto if / elif / else
# Apenas UMA condição será executada.

# 8️⃣ Fluxo visual com Debug
# O debugger mostra:
# - O caminho real que o código percorre.
# - Quando ele pula blocos.
# - Quando ele sai da estrutura condicional.

# 9️⃣ Conclusão da aula
# Debugger é uma ferramenta essencial.
# Ajuda a entender o fluxo do programa.
# Permite visualizar o comportamento real do interpretador.
# Muito útil para aprender lógica e corrigir erros.