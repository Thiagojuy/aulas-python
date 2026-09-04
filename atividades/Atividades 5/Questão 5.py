"""Questão 5: Calculadora Básica de Dois Números
Escreva um programa que peça ao usuário dois números reais (ex: 10 e 5) e, em seguida,
solicite o operador matemático desejado como texto ("+", "-", "*" ou "/").
Utilize o match / case para verificar o operador e realizar o cálculo direto na exibição:
Se for "+", mostre a soma dos dois números.
Se for "-", mostre a subtração.
Se for "*", mostre a multiplicação.
Se for "/", mostre a divisão.
Se for qualquer outro caractere, exiba "Operação inválida!".
"""
numero_1 = int(input("Digite o primeiro numero real"))
numero_2 = int(input("Digite o segundo numero real"))
operador = input("Digite o operador matemático de sua escolha: +, -, *, /, ")
match operador:
    case "+":
        print(numero_1 + numero_2)
    case "-":
        print(numero_1 - numero_2)
    case "*":
        print(numero_1 * numero_2)
    case "/":
        print(numero_1 / numero_2)
    case _:
        print("Operação inválida!")
