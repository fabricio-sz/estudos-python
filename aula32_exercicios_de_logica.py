"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')

try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')


# ==========================================================
# AULA 32 — EXERCÍCIOS DE LÓGICA (3 PROBLEMAS)
# ==========================================================

# ----------------------------------------------------------
# EXERCÍCIO 1 — NÚMERO PAR OU ÍMPAR
# ----------------------------------------------------------

# Objetivo do algoritmo:
# Pedir um número ao usuário e informar se ele é PAR ou ÍMPAR.

# Passos da lógica:

# 1️⃣ Receber um valor digitado pelo usuário.
# O input sempre retorna uma STRING.

# 2️⃣ Precisamos transformar esse valor em número inteiro
# para poder fazer operações matemáticas.

# 3️⃣ Como o usuário pode digitar algo inválido,
# usamos TRY/EXCEPT para evitar que o programa quebre.

# 4️⃣ Depois de converter para inteiro,
# usamos o operador de resto da divisão (%).

# regra matemática:
# número % 2 == 0 → PAR
# número % 2 != 0 → ÍMPAR

# 5️⃣ Caso ocorra erro na conversão,
# informamos que o valor digitado não é um número inteiro.

# Conceitos utilizados:
# - input
# - try / except
# - conversão de tipo (int)
# - operador módulo %
# - estrutura condicional if / else


# ----------------------------------------------------------
# EXERCÍCIO 2 — SAUDAÇÃO BASEADA NA HORA
# ----------------------------------------------------------

# Objetivo do algoritmo:
# Pedir ao usuário a hora atual e mostrar uma saudação.

# Regras:

# 0 até 11  → Bom dia
# 12 até 17 → Boa tarde
# 18 até 23 → Boa noite

# Passos da lógica:

# 1️⃣ Receber a hora digitada pelo usuário.

# 2️⃣ Converter para número inteiro,
# pois iremos comparar valores numéricos.

# 3️⃣ Usar TRY/EXCEPT para evitar erro caso
# o usuário digite texto ou algo inválido.

# 4️⃣ Criar condições utilizando intervalos numéricos:

# hora >= 0  e hora <= 11
# hora >= 12 e hora <= 17
# hora >= 18 e hora <= 23

# 5️⃣ Cada intervalo corresponde a uma saudação.

# 6️⃣ Caso a hora seja diferente de 0 a 23,
# informar que a hora é inválida.

# Conceitos utilizados:
# - input
# - conversão int()
# - try / except
# - operadores lógicos AND
# - comparação numérica
# - elif


# ----------------------------------------------------------
# EXERCÍCIO 3 — TAMANHO DO NOME
# ----------------------------------------------------------

# Objetivo do algoritmo:
# Analisar o tamanho do primeiro nome do usuário.

# Regras:

# até 4 letras → nome curto
# 5 ou 6 letras → nome normal
# mais de 6 letras → nome muito grande

# Passos da lógica:

# 1️⃣ Receber o nome do usuário.

# 2️⃣ Usar a função len()
# para contar quantos caracteres o nome possui.

# 3️⃣ Criar variáveis booleanas
# para identificar o tamanho do nome.

# Exemplo conceitual:

# nome_curto
# nome_normal
# nome_longo

# 4️⃣ Usar IF para verificar cada condição.

# 5️⃣ Mostrar uma mensagem explicando
# o tamanho do nome e a quantidade de caracteres.

# Observação importante:
# TRY/EXCEPT não é necessário aqui,
# pois len() funciona normalmente com strings.

# Conceitos utilizados:
# - input
# - função len()
# - operadores lógicos
# - variáveis booleanas
# - estrutura condicional


# ----------------------------------------------------------
# CONCEITOS IMPORTANTES PRATICADOS NESSES EXERCÍCIOS
# ----------------------------------------------------------

# ✔ entrada de dados (input)
# ✔ tratamento de erro (try/except)
# ✔ conversão de tipos (int)
# ✔ operadores matemáticos (%)
# ✔ operadores lógicos (and)
# ✔ estruturas condicionais
# ✔ intervalos numéricos
# ✔ função len()
# ✔ criação de variáveis booleanas
# ✔ construção de lógica de programação


# ----------------------------------------------------------
# OBJETIVO REAL DESSES EXERCÍCIOS
# ----------------------------------------------------------

# O foco não é a matemática.

# O foco é desenvolver:

# ✔ raciocínio lógico
# ✔ controle de fluxo
# ✔ validação de entrada
# ✔ organização do código

# Essas são habilidades fundamentais
# para qualquer programador.