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

# RESUMO — Estrutura IF / ELIF / ELSE

# - O "if" executa um bloco de código somente se a condição for verdadeira.
# - A indentação (4 espaços ou TAB) define o bloco de código.
# - Código fora do bloco do if sempre será executado.

# - O "else" executa quando nenhuma condição anterior for verdadeira.
# - O "else" sempre é o último bloco.
# - Não pode existir "else" sem um "if".

# - O "elif" permite testar várias condições diferentes.
# - Podem existir vários "elif".
# - O Python verifica as condições de cima para baixo.

# FLUXO DE EXECUÇÃO:
# 1. Python verifica o if.
# 2. Se for falso, verifica os elif em ordem.
# 3. Ao encontrar a primeira condição verdadeira:
#    -> executa o bloco correspondente
#    -> sai da estrutura
#    -> não verifica os próximos.
# 4. Se nenhuma condição for verdadeira, executa o else.

# OBSERVAÇÕES:
# - Apenas UM bloco é executado dentro do if/elif/else.
# - É possível ter vários if separados no mesmo código.
# - Um bloco pode conter várias linhas de código.
# - "pass" ou "..." podem ser usados como placeholder (código vazio temporário).