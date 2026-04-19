# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)

# ==========================================================
# AULA 11 — Precedência de Operadores
# ==========================================================

# 1️⃣ O que essa aula ensina?
# - A ordem em que os operadores são executados.
# - Uso de parênteses para controlar a ordem.
# - Que variáveis podem ter seus valores sobrescritos.

# 2️⃣ O que é precedência?
# - É a prioridade que certos operadores têm sobre outros.
# - Nem toda conta é feita da esquerda para a direita.

# 3️⃣ Ordem de precedência (do mais forte para o mais fraco):

# 1. (n + n)          -> Parênteses (de dentro para fora)
# 2. **               -> Exponenciação (potência)
# 3. * / // %         -> Multiplicação, divisão, divisão inteira, módulo
# 4. + -              -> Adição e subtração

# 4️⃣ Regras importantes:
# - Parênteses internos são resolvidos primeiro.
# - Operadores de mesma prioridade são executados da esquerda para a direita.
# - Podemos usar parênteses para forçar a ordem da conta.

# 5️⃣ Exemplo sem parênteses:
# 1 + 1 ** 5 + 5
# A potência é feita antes da soma.

# 6️⃣ Exemplo com parênteses:
# (1 + 1) ** (5 + 5)
# Agora as somas são feitas antes da potência.

# 7️⃣ Sobrescrevendo variável:
# x = 10
# x = 5
# O valor antigo é substituído.
# O Python lê o código de cima para baixo.

# 8️⃣ Conclusão:
# - Sempre que a conta parecer confusa, use parênteses.
# - Parênteses deixam o código mais previsível e legível.