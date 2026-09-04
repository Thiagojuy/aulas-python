"""
Questão 5: A Catraca VIP de Eventos (Uso de AND e OR no if)
Uma festa exclusiva possui regras específicas para a entrada de convidados.
Para ter o acesso liberado, a pessoa precisa atender a uma das seguintes combinações de condições:
Ter idade maior ou igual a 18 anos E possuir o convite VIP;
OU ser um dos organizadores do evento (independente da idade).
Crie um formulário no Python que solicite:
A idade da pessoa (inteiro);
Se ela possui convite VIP (digitar 1 para Sim, 0 para Não);
Se ela é organizadora do evento (digitar 1 para Sim, 0 para Não).
Escreva uma única estrutura if combinando os operadores and e or para validar a regra.
Se a condição for verdadeira, exiba: "Entrada PERMITIDA! Seja bem-vindo(a)". Caso contrário (else),
exiba: "Entrada NEGADA! Você não atende aos requisitos".
"""

idade = int(input("Digite sua idade: "))
convite = int(input("possui convite VIP: digitar 1 para Sim, 0 para Não "))
orgnaizador = int(input("É organizadora do evento (digitar 1 para Sim, 0 para Não)"))
entrada = convite == 1 and idade >= 18 or orgnaizador == 1
if entrada == True:
    print("Entrada PERMITIDA! Seja bem-vindo(a)")
else:
    print("Entrada NEGADA! Você não atende aos requisitos")

