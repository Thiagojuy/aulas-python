"""Questão 2: A Fábrica de Caixas (Operador de Módulo)
Uma fábrica empacota maçãs em caixas que cabem exatamente 12 unidades. Crie um programa que pergunte ao
usuário a quantidade total de maçãs colhidas no dia. Utilizando o operador de módulo (%),
calcule e exiba na tela quantas maçãs sobrarão fora das caixas (ou seja, o resto da divisão por 12).
"""
vt_maca = int(input("Quantas maçãs foram colhidas?"))
caixa = vt_maca // 12
resto = vt_maca % 12
print("Foram colhidas", caixa,"caixas" " e sobraram", resto, "maças")