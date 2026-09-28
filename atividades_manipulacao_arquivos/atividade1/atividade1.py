# ==============================================================================
# QUESTÃO 1: SISTEMA DE CARRINHO DE COMPRAS E PAGAMENTO (VERSÃO COMENTADA)
# ==============================================================================

# 1. CAPTURA DE DADOS DO CLIENTE
# Solicita o nome do usuário e remove espaços extras no início e fim com .strip()
usuario = input("Digite seu nome para iniciar a compra: ").strip()

# Inicializa uma lista vazia que vai funcionar como a nossa matriz/carrinho
produtos = []

# Inicializa a variável acumuladora que vai somar os preços de cada item
total_compra = 0.0

print("\n--- INICIANDO CARRINHO DE COMPRAS ---")
print("(Digite 'fim' no nome do produto para encerrar)")

# 2. LOOP DE INSERÇÃO DE PRODUTOS NO CARRINHO
# Criamos um loop infinito (while True) que só para quando encontrar o comando 'break'
while True:
    # Solicita o nome do produto e limpa espaços extras
    nome_produto = input("\nDigite o nome do produto: ").strip()

    # CONDIÇÃO DE PARADA: Se o usuário digitar 'fim' (independente de maiúsculas/minúsculas)
    if nome_produto.lower() == 'fim':
        break  # Interrompe o laço while imediatamente

    # Tratamento de erro para garantir que o preço digitado seja um número válido
    try:
        preco_produto = float(input(f"Digite o preço de '{nome_produto}': R$ "))

        # Regra de proteção: impede que o usuário digite preços negativos
        if preco_produto < 0:
            print("O preço não pode ser negativo. Tente novamente.")
            continue  # Volta para o início do while, ignorando o código abaixo

    except ValueError:
        # Se o usuário digitar letras ou usar vírgula em vez de ponto, entra aqui
        print("Preço inválido! Digite apenas números usando ponto para centavos.")
        continue  # Volta para o início do while

    # Armazena o produto como uma sublista [nome, preço] dentro da lista principal 'produtos'
    produtos.append([nome_produto, preco_produto])

    # Soma o preço do produto atual ao valor total da compra
    total_compra += preco_produto

# 3. PROCESSAMENTO DO PAGAMENTO (ESCRITA NO ARQUIVO)
print("\n--- FINALIZANDO COMPRA ---")

# O gerenciador de contexto 'with open' garante que o arquivo seja fechado automaticamente.
# O modo "w" (write) cria o arquivo 'pagamento.txt' ou sobrescreve caso ele já exista.
# 'encoding="utf-8"' é usado para evitar problemas com acentos (como no "R$").
with open("pagamento.txt", "w", encoding="utf-8") as arquivo_escrita:
    # Grava o cabeçalho com o nome do cliente
    arquivo_escrita.write(f"Cliente: {usuario}\n")
    arquivo_escrita.write("Produtos:\n")

    # Percorre a lista de produtos para gravar item por item no arquivo
    for item in produtos:
        # item[0] é o nome do produto, item[1] é o preço formatado com 2 casas decimais (.2f)
        arquivo_escrita.write(f"- {item[0]}: R$ {item[1]:.2f}\n")

    # Grava a linha final com a palavra-chave TOTAL de forma estrita e formatada
    arquivo_escrita.write(f"TOTAL: R$ {total_compra:.2f}\n")

print("Arquivo 'pagamento.txt' gerado com sucesso!")

# 4. VALIDAÇÃO E EXIBIÇÃO FINAL (LEITURA DO ARQUIVO)
print("\n--- PROCESSANDO PAGAMENTO ---")

# Abre o mesmo arquivo, mas agora no modo "r" (read) apenas para leitura
with open("pagamento.txt", "r", encoding="utf-8") as arquivo_leitura:
    # Lê todo o conteúdo do arquivo e armazena como uma única string na variável 'conteudo'
    conteudo = arquivo_leitura.read()

    # Define o termo exato que precisamos encontrar para isolar o valor final
    termo_busca = "TOTAL: R$ "

    # .find() retorna o índice (posição do caractere) onde o termo_busca começa no texto.
    # Se o texto não for encontrado, ele retorna -1.
    posicao_inicial = conteudo.find(termo_busca)

    if posicao_inicial != -1:
        # Para pegar só o número, precisamos saltar o tamanho da palavra "TOTAL: R$ ".
        # Portanto, a posição onde o número começa é: posicao_inicial + o tamanho do termo.
        inicio_valor = posicao_inicial + len(termo_busca)

        # FATIAMENTO: Corta a string partindo do 'inicio_valor' até o final do arquivo.
        # O método .strip() limpa qualquer quebra de linha (\n) ou espaço que sobrar no fim.
        valor_extraido = conteudo[inicio_valor:].strip()

        # Exibe no console a mensagem de sucesso exatamente como exigido pela regra de negócio
        print(f"Compra processada com sucesso! Valor cobrado: R$ {valor_extraido}")
    else:
        # Caso ocorra algum erro e a palavra TOTAL não esteja no arquivo
        print("Erro: A informação de TOTAL não foi localizada no arquivo.")
