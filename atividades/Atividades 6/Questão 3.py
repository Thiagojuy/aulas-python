"""
Somador de Números
Faça um programa que peça ao usuário para digitar números inteiros repetidamente.
O programa deve continuar pedindo números até que o usuário digite o número 0 (zero).
Quando o usuário digitar 0, o laço deve ser encerrado e o programa deve exibir a soma de
todos os números que foram digitados até aquele momento.
"""


soma = 0
while True:
    numero = int(input("Digite um numero inteiro: "))

    if numero == 0:
        break

    soma += numero
print(f"A soma de todos os mumeros digitas é", soma)
