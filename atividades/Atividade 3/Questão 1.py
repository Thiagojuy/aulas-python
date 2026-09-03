"""Questão 1: A Divisão da Conta (Calculadora)
Crie um programa para um restaurante que funciona como uma calculadora de divisão de conta.
O sistema deve solicitar ao usuário o valor total da conta (ex: 150.00) e a quantidade de pessoas
na mesa. O programa deve calcular o valor que cada um deve pagar e exibir a mensagem:
"O valor total foi de R$ [Total], e cada pessoa deve pagar R$ [Valor Dividido]".
"""
valor_total = float(input("Digite sua valor total da conta:"))
pessoas = int(input("Quantas pessoas na mesa?"))
valor_pesoa = float(valor_total / pessoas)
print("O valor total foi de R$", valor_total, "e cada pessoa deve pagar R$", valor_pesoa)

