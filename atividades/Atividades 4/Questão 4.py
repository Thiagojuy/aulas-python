"""
Questão 4: O Teste do Saldo Bancário
Desenvolva um algoritmo que simule um saque bancário. O programa deve receber o saldo atual
do cliente (ex: 500.00) e o valor que ele deseja sacar. Se o valor do saque for menor ou igual
ao saldo disponível, o programa deve subtrair o valor sacado, atualizar o saldo e exibir:
"Saque realizado com sucesso! Saldo atual: R$ [Novo Saldo]". Caso o saque seja maior que o saldo,
exiba: "Saldo insuficiente para realizar esta operação".
"""
saldo = 1000
saque = float(input("Digite o valor do saque: "))
if saque <= saldo:
    novo_saldo = saldo - saque
    print("Saque realizado com sucesso! Saldo atual: R$", novo_saldo)
else:
    print("Saldo insuficiente para realizar esta operação")
