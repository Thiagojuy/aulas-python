"""
Validação de Senha
Escreva um programa que defina uma senha fixa no código (por exemplo, "123456").
Peça para o usuário digitar a senha. Enquanto a senha digitada não for igual à senha correta,
exiba a mensagem: "Senha incorreta. Tente novamente." e peça a senha de novo
(igual ao exemplo do "Joao" visto em aula). Quando o usuário acertar, exiba: "Acesso permitido!".
"""
senha_fixa = 123456
senha = int(input("Digite a senha: "))
while True:
    if senha_fixa != senha:
        print("Senha incorreta. Tente novamente.")
        senha = int(input("Digite a senha: "))
    if senha_fixa == senha:
        print("Acesso permitido.")
        break


