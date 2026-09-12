"""Crie uma lista que ela armazene um numero X de funcionários.
Usando While, adicione quantos funcionários quiser.

Com o for, voçê irá imprimir duas listas:
Uma lista com todos os funcionários que receberão um aumento.
Outra lista, com todos os funcionários que serão demitidos.

Voçê irá decidir qual funcionário será demitido ou receberá
aumento pelo index do funcinário lista[]
"""
# Atividade 7

lista_funcionarios = [] # cria vazia, modifica no while

while True:
    lista_funcionarios.append(input("Digite o nome do funcionario: "))

    opcao = input("Digite 1 para continuar, 2 para sair: ")
    if opcao != "1":
        print(f"Todos os funcionários: {lista_funcionarios}")
        print("Quantidade de funcionários",len(lista_funcionarios)) # tamanho
        break

lista_demitidos = []
lista_aumento = []

# while len(lista_funcionarios) > repeticao:
#     print(f"Funcionário {repeticao}: {lista_funcionarios[repeticao]}")
#     repeticao += 1

print("Lista de TODOS os funcionários: ")
for index in range(len(lista_funcionarios)):
    print(f"Funcionário {index}: {lista_funcionarios[index]}")

repeticao = 0
print("Lista dos funcionários DEMITIDOS: ")
for index in range(len(lista_funcionarios)):
    repeticao += 1
    resultado = repeticao % 2
    if repeticao < len(lista_funcionarios) and resultado == 0:
        lista_demitidos.append(lista_funcionarios[index])
print(lista_demitidos)

repeticao = 0
print("Lista dos funcionários AUMENTO: ")
for index in range(len(lista_funcionarios)):
    repeticao += 1
    resultado = repeticao % 2
    if repeticao < len(lista_funcionarios) and resultado != 0:
        lista_aumento.append(lista_funcionarios[index])
print(lista_aumento)

lista_numeros = [10, 9, 6, 7]

print(max(lista_numeros))
print(min(lista_numeros))

media = sum(lista_numeros) / len(lista_numeros)
print("Média das suas notas: ",media)