"""
Contagem Regressiva
Crie um programa que exiba uma contagem regressiva para o lançamento de um foguete.
O programa deve definir uma variável iniciando em 10 e, usando o while, exibir os números
de 10 até 1. Ao final, quando o laço terminar, exiba a mensagem: "Foguete lançado!".
"""
from bdb import Breakpoint

regressiva = 10
while regressiva > 0:
    regressiva -= 1
    print(regressiva)
    if regressiva == 1:
        print("Foguete lançado")
        break



