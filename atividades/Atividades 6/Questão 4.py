"""
Menu Interativo
Crie um programa que mostre repetidamente um menu com duas opções:
1 - Mostrar saudação
2 - Sair do programa
O programa deve pedir para o usuário escolher uma opção. Usando while:
Se ele digitar 1, exiba "Olá, seja muito bem-vindo(a)!".
Se ele digitar qualquer número diferente de 1 e 2, exiba "Opção inválida!".
O programa só deve parar de repetir e encerrar quando o usuário digitar 2,
exibindo a mensagem "Programa encerrado."

"""
opcao = 0

# O loop continua rodando enquanto a opção não for 2
while opcao != 2:
    # Mostra o menu de opções
    print("\n--- MENU ---")
    print("1 - Mostrar saudação")
    print("2 - Sair do programa")

    # Pede para o usuário escolher uma opção
    opcao = int(input("Escolha uma opção: "))

    # Verifica a opção digitada
    if opcao == 1:
        print("Olá, seja muito bem-vindo(a)!")
    elif opcao != 2:
        print("Opção inválida!")

# Mensagem exibida após sair do loop (quando digita 2)
print("Programa encerrado.")

