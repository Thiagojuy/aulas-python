"""
Jogo da Adivinhação com Tentativas
Crie um programa onde o computador "pensa" em um número secreto (você pode definir um número
fixo diretamente no código, por exemplo, numero_secreto = 14). O usuário deve tentar adivinhar
qual é esse número. Usando a estrutura while, o programa deve continuar pedindo um novo palpite
enquanto o usuário não acertar.
Requisito extra: Crie uma variável para contar quantas tentativas o usuário fez.
Quando ele finalmente acertar o número, exiba a mensagem: "Parabéns! Você acertou o
número secreto em [X] tentativas!" (onde X é o número de vezes que ele tentou).
"""
# Define o número secreto fixo

# Define o número secreto fixo
numero_secreto = 14

# Inicializa as variáveis do palpite e do contador de tentativas
palpite = 0
tentativas = 0

print("Tente adivinhar o número secreto que eu estou pensando!")

# O laço continua rodando enquanto o palpite for diferente do número secreto
while palpite != numero_secreto:
    palpite = int(input("Digite o seu palpite: "))

    # Aumenta o contador em 1 a cada tentativa feita
    tentativas += 1

    # Dá uma dica baseada no palpite do usuário
    if palpite < numero_secreto:
        print("O número secreto é MAIOR! Tente novamente.")
    elif palpite > numero_secreto:
        print("O número secreto é MENOR! Tente novamente.")

# Mensagem final mostrando o total de tentativas acumuladas
print(f"\nParabéns! Você acertou o número secreto em {tentativas} tentativas!")
