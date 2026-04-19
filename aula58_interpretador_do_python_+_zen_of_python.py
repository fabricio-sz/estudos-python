"""
Interpretador do Python

python mod.py (executa o mod)
python -u (unbuffered)
python -m mod (lib mod como script)
python -c 'cmd' (comando)
python -i mod.py (interativo com mod)

The Zen of Python, por Tim Peters

Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
Complexo é melhor que complicado.
Plano é melhor que aglomerado.
Esparso é melhor que denso.
Legibilidade conta.
Casos especiais não são especiais o bastante para quebrar as regras.
Embora a praticidade vença a pureza.
Erros nunca devem passar silenciosamente.
A menos que sejam explicitamente silenciados.
Diante da ambiguidade, recuse a tentação de adivinhar.
Deve haver um -- e só um -- modo óbvio para fazer algo.
Embora esse modo possa não ser óbvio à primeira vista a menos que você seja holandês.
Agora é melhor que nunca.
Embora nunca frequentemente seja melhor que *exatamente* agora.
Se a implementação é difícil de explicar, é uma má ideia.
Se a implementação é fácil de explicar, pode ser uma boa ideia.
Namespaces são uma grande ideia -- vamos fazer mais dessas!
"""

# ==========================================================
# AULA 58 — INTERPRETADOR DO PYTHON + ZEN OF PYTHON
# ==========================================================

"""
Nesta aula você aprende:

✔ Como executar Python pelo terminal
✔ Comandos úteis do interpretador
✔ Filosofia do Python (Zen of Python)
"""

# ==========================================================
# 1️⃣ COMANDOS DO PYTHON (TERMINAL)
# ==========================================================

"""
Executar arquivo:
python arquivo.py

Ver versão:
python --version
python -V

Ajuda:
python --help
"""

# Explicação baseada na aula :contentReference[oaicite:0]{index=0}

# ==========================================================
# 2️⃣ EXECUTAR COMANDOS DIRETO NO TERMINAL
# ==========================================================

"""
Executar comando direto:

python -c "print('Olá')"
"""

# 👉 Útil para testes rápidos

# ==========================================================
# 3️⃣ MODO INTERATIVO
# ==========================================================

"""
Entrar no Python interativo:

python

→ permite testar código direto
"""

# Sair:
# exit() ou quit()

# ==========================================================
# 4️⃣ EXECUTAR MÓDULO COMO SCRIPT
# ==========================================================

"""
python -m modulo

Exemplo:
python -m venv venv

→ cria ambiente virtual
"""

# ==========================================================
# 5️⃣ MODO INTERATIVO COM ARQUIVO
# ==========================================================

"""
python -i arquivo.py

→ executa o arquivo
→ mantém modo interativo aberto
"""

# ==========================================================
# 6️⃣ FLAG -u (UNBUFFERED)
# ==========================================================

"""
python -u arquivo.py

→ não usa buffer
→ imprime direto na tela
"""

# 🧠 Explicação:
# Normalmente o Python guarda saídas em "buffer"
# e depois mostra tudo de uma vez

# ==========================================================
# 7️⃣ PONTO E VÍRGULA (NÃO RECOMENDADO)
# ==========================================================

"""
print('Oi'); print(1+1)
"""

# ✔ funciona
# ❌ NÃO usar em código normal

# ==========================================================
# 8️⃣ ZEN OF PYTHON (FILOSOFIA)
# ==========================================================

"""
Execute isso no terminal:

python -c "import this"
"""

# ==========================================================

# 📜 PRINCIPAIS IDEIAS

"""
✔ Bonito é melhor que feio
✔ Explícito é melhor que implícito
✔ Simples é melhor que complexo
✔ Legibilidade conta
✔ Deve haver uma forma óbvia de fazer algo
✔ Erros não devem passar silenciosamente
✔ Se é difícil explicar → é ruim
✔ Se é fácil explicar → pode ser bom
"""

# ==========================================================

# 🧠 INTERPRETAÇÃO PRÁTICA

"""
✔ Escreva código CLARO
✔ Evite "mágica"
✔ Prefira simplicidade
✔ Nomeie bem variáveis
✔ Não esconda erros
"""

# ==========================================================
# 9️⃣ ERRO COMUM (TRY MAL USADO)
# ==========================================================

try:
    print(10 / 0)
except:
    pass  # ❌ erro ignorado

# 👉 Isso quebra regra do Python:
# "Erros nunca devem passar silenciosamente"

# ==========================================================
# 🔟 BOA PRÁTICA
# ==========================================================

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Erro de divisão")

# ✔ tratamento correto

# ==========================================================
# 🚀 CONCLUSÃO
# ==========================================================

"""
Você aprendeu:

✔ comandos do Python no terminal
✔ formas de executar código
✔ filosofia do Python

👉 O Zen do Python é guia de como pensar como programador Python

Isso aqui separa iniciante de profissional 🔥
"""