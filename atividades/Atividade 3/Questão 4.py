"""Questão 4: O Boletim Escolar Automático (Aritmética + Lógica AND)
Construa um sistema escolar que leia a Nota 1 e a Nota 2 de um aluno,
além da sua Porcentagem de Frequência. O programa deve primeiro calcular a
média das notas. Para o aluno ser aprovado, ele precisa de duas coisas ao
mesmo tempo: uma média maior ou igual a 6.0 E uma frequência maior ou igual a 75.
Exiba a média calculada e, em seguida, exiba True se ele foi aprovado ou False se reprovou,
usando o operador and.
"""

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = float(nota1 + nota2) / 2
faltas = int(input("Quantas faltas o aluno obteve?"))
aulas = 200
frequencia = float((aulas - faltas))
limite_falta = 200 * 0.75
aprovado = bool(media >= 60 and frequencia >= limite_falta)
print("O aluno obteve média:", media,  "aluno foi aprovado?", aprovado)


