"""
Questão 3: Turno de Estudo
Faça um programa que pergunte em qual turno o aluno estuda. O usuário deve digitar uma letra:
"M" ou "m" para Matutino
"V" ou "v" para Vespertino
"N" ou "n" para Noturno
Usando o match / case, exiba a mensagem correspondente:
"Bom Dia!"
"Boa Tarde!"
"Boa Noite!"
"Turno inválido!" (para qualquer outro caractere)
"""
turno = input("Qual é o seu turno de estudo: (M ou m para Matutino, V ou v para Vespertino, N ou n para Noturno")
match turno:
    case "M" | "m":
        print("Bom Dia!")
    case "N" | "n":
        print("Boa Noite!")
    case "V" | "v":
        print("Boa Tarde!")
    case _:
        print("Turno inválido!")
print("FIM")
