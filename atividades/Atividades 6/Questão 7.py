"""
Controle de Orçamento
Imagine que você tem um orçamento total para uma viagem, por exemplo, R$ 500.
Escreva um programa que defina esse valor em uma variável e peça ao usuário para
digitar o valor de cada gasto que ele realizar.
Usando um laço while, o programa deve subtrair cada gasto do orçamento total e exibir
o saldo restante. O laço deve continuar pedindo novos gastos enquanto o orçamento for
maior que zero.
Se o usuário gastar todo o dinheiro (ou seja, o orçamento chegar a zero ou ficar negativo),
o programa deve encerrar o laço e exibir a mensagem: "Atenção: Você ficou sem saldo ou estourou
seu orçamento!"
"""

# Define o orçamento inicial da viagem
orcamento = 500.0

print(f"Orçamento inicial da viagem: R$ {orcamento:.2f}")

# O laço continua rodando enquanto houver dinheiro no orçamento (maior que zero)
while orcamento > 0:
    # Pede o valor do gasto atual
    gasto = float(input("\nDigite o valor do gasto realizado: R$ "))

    # Subtrai o gasto do orçamento total
    orcamento -= gasto

    # Se o saldo ainda for positivo, mostra o quanto sobrou
    if orcamento > 0:
        print(f"Saldo restante: R$ {orcamento:.2f}")

# Mensagem exibida quando o orçamento zera ou fica negativo (fora do while)
print("\nAtenção: Você ficou sem saldo ou estourou seu orçamento!")
print(f"Saldo final: R$ {orcamento:.2f}")
