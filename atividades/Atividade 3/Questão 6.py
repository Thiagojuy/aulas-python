"""
Questão 6: O Erro de Verificação (Análise e Correção de Código)
Um programador iniciante tentou criar um validador de senhas e escreveu o seguinte código:
senha_cadastrada = 1234
senha_digitada = input("Digite sua senha: ")
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado)

Mesmo que o usuário digite os números 1234 no teclado, o programa sempre responde False.
Explique tecnicamente por que isso acontece (lembre-se dos tipos de dados estudados em sala)
e reescreva o código corrigindo o erro como comentário no seu próprio código (no arquivo .py).

Resposta: é necessário declarar a variável senha_digitada do tipo "inteiro", pois o interpretador
considerará a respsta inputada como do tipo "String".
"""
senha_cadastrada = 1234
senha_digitada = int(input("Digite sua senha: "))
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado)
