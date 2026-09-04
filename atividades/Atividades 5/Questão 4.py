"""
Questão 4: Estações do Ano
Crie um programa que peça ao usuário para digitar o número correspondente a um mês do ano
(de 1 a 12). Com base no mês digitado, mostre em qual estação do ano (no Hemisfério Sul)
ele se encontra predominantemente:
Meses 12, 1 ou 2: "Verão"
Meses 3, 4 ou 5: "Outono"
Meses 6, 7 ou 8: "Inverno"
Meses 9, 10 ou 11: "Primavera"
Qualquer outro número: "Mês inválido!"
"""

mes = (input("Digite o mês do ano. (1 - 12): "))
match mes:
    case "12" | "1" | "2":
        print("Verão")
    case "3" | "4" | "5":
        print("Outono")
    case "6" | "7" | "8":
        print("Inverno")
    case "9" | "10" | "11":
        print("Primavera")
    case _:
        print("Mês inválido!")
print("FIM")



