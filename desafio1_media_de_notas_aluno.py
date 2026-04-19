# nome do aluno
# nota materia 1
# nota materia 2
# nota materia 3
# nota materia 4
# media das quatro (4) materias
# nota de 0 a 10
# aprovado >= 7
# recuperacao < 7 e > 3
# reprovado < 3

nome = input("Nome do Aluno(a): ")

materia1 = input("Nota Português: ")
materia2 = input("Nota Matematica: ")
materia3 = input("Nota História: ")
materia4 = input("Nota Ciências: ")

try:

    materia1 = float(materia1)
    materia2 = float(materia2)
    materia3 = float(materia3)
    materia4 = float(materia4)

    media_notas = (materia1 + materia2 + materia3 + materia4) / 4
    valida_negativo = (materia1 < 0) or (materia2 < 0) or (materia3 < 0) or (materia4 < 0)
    valida_nota_acima = (materia1 > 10) or (materia2 > 10) or (materia3 > 10) or (materia4 > 10)
    aluno_aprovado = media_notas >= 7
    aluno_recuperacao = media_notas > 3 and media_notas < 7
    aluno_reprovado = media_notas >= 0 and media_notas <= 3

    if valida_negativo:

        print(f"Notas negativas não são permitidas, apenas de 0 a 10!")

    elif valida_nota_acima:

        print(f"Notas acima de 10 não são permitidas, apenas de 0 a 10!")

    elif aluno_aprovado:

        print(f"| Nome Aluno(a): {nome} | Média: {media_notas:.2f} | Situação: Aprovado |")

    elif aluno_recuperacao:

        print(f"| Nome Aluno(a): {nome} | Média: {media_notas:.2f} | Situação: Recuperação |")

    elif aluno_reprovado:

        print(f"| Nome Aluno(a): {nome} | Média: {media_notas:.2f} | Situação: Reprovado |")

    else:

        print(f"Notas permitidas apenas de 0 a 10!")

except:

    print("Notas devem possuir números.")