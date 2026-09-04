"""
Questão 1: Menu da Lanchonete
Crie um programa que receba o código de um item do menu de uma lanchonete (de 1 a 4)
e mostre o nome do produto e o preço correspondente, conforme a tabela abaixo:
Código
Produto
Preço

1
Cachorro-quente
R$ 10,00
2
Hambúrguer
R$ 15,00
3
Batata Frita
R$ 8,00
4
Refrigerante
R$ 5,00

Caso o usuário digite qualquer outro número, exiba a mensagem: "Código inválido".
"""
codigo = (input("Digite o código do produto: (de 1 a 4)"))
match codigo:
    case "1":
        print("Cachorro-quente - R$ 10,00")
    case "2":
        print("Hambúrguer - R$ 15,00")
    case "3":
        print("Batata Frita - R$ 8,00")
    case "4":
        print("Refrigerante - R$ 5,00")
    case _:
        print("Código Inválido")
print("FIM")
"Boa Noite!"
