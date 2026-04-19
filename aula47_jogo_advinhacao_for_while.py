"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0

# ==========================================================
# AULA 47 — JOGO DE ADIVINHAÇÃO (FOR + WHILE)
# ==========================================================

# 📌 OBJETIVO
# Criar um jogo onde o usuário precisa adivinhar uma palavra:
# - Digitando apenas UMA letra por vez
# - Mostrando letras corretas
# - Mostrando * para letras não descobertas
# - Contando tentativas

# ==========================================================

import os

# 1️⃣ VARIÁVEIS PRINCIPAIS (fora do while)
palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

# ==========================================================

# 2️⃣ LOOP PRINCIPAL DO JOGO
while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    # ------------------------------------------------------
    # 3️⃣ VALIDAÇÃO (apenas 1 letra)
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    # ------------------------------------------------------
    # 4️⃣ VERIFICA SE A LETRA EXISTE
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    # ------------------------------------------------------
    # 5️⃣ FORMAR A PALAVRA (lógica principal)
    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    # ------------------------------------------------------
    # 6️⃣ CONDIÇÃO DE VITÓRIA
    if palavra_formada == palavra_secreta:
        os.system('clear')  # Windows: 'cls'

        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era:', palavra_secreta)
        print('Tentativas:', numero_tentativas)

        # Reset do jogo
        letras_acertadas = ''
        numero_tentativas = 0

# ==========================================================

# 🧠 COMO FUNCIONA (RESUMO)

"""
1. while True → roda o jogo infinito
2. input → usuário digita uma letra
3. validação → impede mais de 1 letra
4. verifica → se a letra está na palavra
5. guarda → salva letras corretas
6. for → percorre palavra secreta
7. monta → palavra com letras + *
8. compara → se ganhou
9. reset → reinicia o jogo
"""

# ==========================================================

# 🔥 CONCEITOS USADOS

"""
- while (loop infinito)
- for (percorrer palavra)
- if / else
- continue
- concatenação de string
- operador "in"
- contador de tentativas
- import os (executar comando do sistema)
"""

# ==========================================================

# 💡 DICAS IMPORTANTES

# ✔ Variáveis fora do while NÃO resetam
# ✔ Variáveis dentro do while resetam a cada loop
# ✔ for percorre letra por letra automaticamente
# ✔ lógica de jogo = juntar tudo que você já aprendeu

# ==========================================================

# 🚀 CONCLUSÃO

# Esse exercício é MUITO importante porque:
# - mistura vários conceitos
# - simula lógica real de jogo
# - treina raciocínio

# Se você entendeu isso aqui,
# você já está evoluindo MUITO na programação 💪
