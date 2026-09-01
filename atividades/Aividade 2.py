from operator import truediv

nome = str(input("Digite seu nome:"))
idade = int(input("Digite sua idade:"))
plano = bool(input("tem plano de saúde?:"))
aceito = idade >= 18 and idade <= 65 and plano == True
print("meu nome é", nome, "tenho", idade, "anos de idade e", "Voçê foi aceito?", aceito)


