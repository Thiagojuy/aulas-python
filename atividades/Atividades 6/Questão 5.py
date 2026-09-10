"""
Tabuada Simples
Crie um programa que peça ao usuário um número inteiro para o qual ele deseja ver a tabuada.
Utilizando uma variável de incremento (como visto no exemplo da idade), crie um laço while
que vá de 1 até 10, exibindo o resultado da multiplicação do número escolhido pelo contador.
Exemplo de saída esperada se o usuário digitar 5:
5 x 1 = 5
5 x 2 = 10
... (até 10)
"""

# Pede ao usuário o número para a tabuada
numero = int(input("Digite um número inteiro para ver a tabuada: "))

# Inicializa o contador (variável de incremento)
contador = 1

print(f"\nTabuada do {numero}:")

# O laço roda enquanto o contador for menor ou igual a 10
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")

    # Incrementa o contador em 1 a cada repetição
    contador += 1
