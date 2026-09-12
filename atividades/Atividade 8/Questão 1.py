"""
Crie uma única função que receba como parâmetro o nome de um aluno, sua nota do
primeiro, segundo, terceiro e quarto bimestre.
Sua função deve calcular a média final desse aluno, e imprimir na tela todos os valores,
e informar se o aluno foi reprovado ou aprovado pela média final.

OBS: valor da média = 7
"""
def media_final():
    aluno = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota do primeiro semestre do aluno: "))
    nota2 = float(input("Digite a nota do segundo semestre do aluno: "))
    nota3 = float(input("Digite a nota do terceiro semestre do aluno: "))
    nota4 = float(input("Digite a nota do quarto semestre do aluno: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print("As notas do aluno são:" nota1, nota2, nota3, nota4,)
    if media >= 7:
        print("Aluno", aluno, "com media", media,  "Aprovado")
    else:
    print("Aluno", aluno, "Reprovado")
    print(media)
