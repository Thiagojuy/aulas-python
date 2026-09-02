

"""

ATIVIDADE 2 - OPERADORES
Crie um algoritmo, que faça um formulário em que o usuário DIGITE seu nome, sua idade e se ele tem plano de saúde (True ou False)
O eu sistema deve retornar em um único print(), todas as informações, e se ele for menor de idade ou idoso ou se não tiver plano de saúde, que ele não será aceito no nosso formulário;

Exemplo de retorno no terminal: Seu nome é João, você tem 22 anos.
Tem plano? False. Você foi aceito? False.


""" 



from operator import truediv

nome = str(input("Digite seu nome:"))
idade = int(input("Digite sua idade:"))
plano = bool(input("tem plano de saúde?:"))
aceito = idade >= 18 and idade <= 65 and plano == True
print("meu nome é", nome, "tenho", idade, "anos de idade e", "Voçê foi aceito?", aceito)


