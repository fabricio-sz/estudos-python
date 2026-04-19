"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
# condicao = 10 == 11
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)
# digito = 9  # > 9 = 0
# novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)
print('Valor' if False else 'Outro valor' if False else 'Fim')

# ==========================================================
# AULA 60 — OPERAÇÃO TERNÁRIA (IF EM UMA LINHA)
# ==========================================================

"""
Operação ternária (condicional de uma linha)

Estrutura:

<valor_se_verdadeiro> if <condição> else <valor_se_falso>
"""

# ==========================================================

# 1️⃣ EXEMPLO SIMPLES

condicao = 10 == 10

resultado = 'Valor' if condicao else 'Outro valor'

print(resultado)  # Valor

# ==========================================================

# 🧠 COMO FUNCIONA

"""
Se a condição for TRUE:
→ retorna o valor antes do IF

Se for FALSE:
→ retorna o valor depois do ELSE
"""

# Explicação baseada na aula :contentReference[oaicite:0]{index=0}

# ==========================================================

# 2️⃣ EXEMPLO DIRETO NO PRINT

print('Valor' if False else 'Outro valor')

# 👉 Saída:
# Outro valor

# ==========================================================

# 3️⃣ EXEMPLO PRÁTICO (VALIDAÇÃO)

digito = 9

novo_digito = digito if digito <= 9 else 0

print(novo_digito)

# ==========================================================

# 🧠 LÓGICA

"""
Se digito <= 9:
→ mantém valor

Se digito > 9:
→ vira 0
"""

# ==========================================================

# 4️⃣ FORMA INVERTIDA

digito = 10

novo_digito = 0 if digito > 9 else digito

print(novo_digito)

# ==========================================================

# 🧠 MESMA COISA, OUTRA LEITURA

"""
Se digito > 9:
→ retorna 0

Caso contrário:
→ retorna digito
"""

# ==========================================================

# 5️⃣ IF TERNÁRIO ENCADEADO (NÃO RECOMENDADO)

print('Valor' if False else 'Outro valor' if False else 'Fim')

# 👉 Saída:
# Fim

# ==========================================================

# 🧠 COMO ISSO FUNCIONA

"""
É como:

if False:
    'Valor'
else:
    if False:
        'Outro valor'
    else:
        'Fim'
"""

# ==========================================================

# ⚠️ CUIDADO

"""
Evite encadear muitos ternários:

❌ difícil de ler
❌ difícil de manter

✔ prefira if normal quando ficar complexo
"""

# ==========================================================

# 6️⃣ COMPARAÇÃO

# ❌ IF normal
if digito > 9:
    novo = 0
else:
    novo = digito

# ✅ Ternário
novo = 0 if digito > 9 else digito

# ==========================================================

# 📌 QUANDO USAR

"""
✔ Condições simples
✔ Código pequeno
✔ Retorno direto

❌ NÃO usar:
- lógica complexa
- múltiplas condições
"""

# ==========================================================

# 🚀 CONCLUSÃO

"""
Você aprendeu:

✔ if em uma linha
✔ melhorar código simples
✔ evitar exageros

👉 Muito usado em código profissional,
mas com responsabilidade 🔥
"""