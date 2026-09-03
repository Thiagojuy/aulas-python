"""
Questão 5: O Sistema de Desconto (Lógica OR)
Uma loja está em promoção: o cliente ganha frete grátis se o valor da compra for
maior que R$ 200.00 OU se ele possuir o cartão VIP da loja. Peça ao usuário o valor
da compra e pergunte se ele é VIP (peça para digitar 1 para "Sim, sou VIP" ou 0 para
"Não sou VIP"). Crie a lógica usando o operador or e imprima True se ele tem direito
ao frete grátis ou False caso não tenha.
"""

valor_compra = float(input("Digite o valor da compra: "))
vip = int(input("Voçê possui o cartão VIP da loja?, digite 1 para sim, ou 0 para não"))
frete_gratis = bool(valor_compra >= 200.00 or vip == 1)
print("O cliente ganhou frete gratis?", frete_gratis)



