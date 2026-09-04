"""
Questão 2: Classificador de Vogais e Consoantes
Escreva um programa que peça para o usuário digitar uma única letra do alfabeto (pode ser minúscula).
Usando match / case, verifique se a letra digitada é uma vogal (a, e, i, o, u).
Se for uma vogal, exiba: "Você digitou uma vogal."
Caso contrário (qualquer outro caractere ou consoante), exiba: "Não é uma vogal."
Dica: Utilize a barra vertical (|) para agrupar todas as vogais em um único case.
"""

letra = input("Digite uma letra em minúslulo: ")
match letra:
    case "a" | "e" | "i" | "o" | "u":
        print("Você digitou uma vogal.")
    case _:
        print("Não é uma vogal.")
print("FIM")
