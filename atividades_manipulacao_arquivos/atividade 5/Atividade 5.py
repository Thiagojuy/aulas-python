# Lista principal que armazenará todos os livros cadastrados
catalogo_livros = []

# Etapa 1 — Lendo o Arquivo TXT Legado
with open("banco_livros.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        # Remove espaços em branco e quebras de linha (\n)
        linha_limpa = linha.strip()

        # Pula a linha de cabeçalho (se houver) ou linhas vazias
        if not linha_limpa or linha_limpa.startswith("id;"):
            continue

        # Separa os dados pelo delimitador ";"
        dados = linha_limpa.split(";")

        # Transforma a linha em um dicionário mapeando os índices corretos
        livro = {
            "id": int(dados[0]),
            "nome": dados[1],
            "descricao": dados[2],
            "preco": float(dados[3]),
            "em_estoque": int(dados[4]),
        }

        # Adiciona o dicionário estruturado à lista catálogo
        catalogo_livros.append(livro)

# Exibe o resultado na tela para verificação
import pprint

pprint.pprint(catalogo_livros)



import json


# Etapa 2 — Gerando o Arquivo JSON ('w' - write)
# Abre o arquivo catalogo.json no modo de escrita ("w") garantindo a codificação UTF-8
with open("catalogo.json", "w", encoding="utf-8") as arquivo_json:
    # Exporta a lista de dicionários formatada e legível
    json.dump(catalogo_livros, arquivo_json, indent=4, ensure_ascii=False)

print("Arquivo 'catalogo.json' gerado com sucesso!")


#import json

# 1. Criando mais 5 livros diferentes diretamente no código como dicionários
novos_livros = [
    {
        "id": 31,
        "nome": "Código Limpo",
        "descricao": "Habilidades práticas do Agile Software",
        "preco": 85.90,
        "em_estoque": 120
    },
    {
        "id": 32,
        "nome": "O Programador Pragmático",
        "descricao": "Sua jornada para a maestria em programação",
        "preco": 92.50,
        "em_estoque": 150
    },
    {
        "id": 33,
        "nome": "Padrões de Projetos",
        "descricao": "Soluções reutilizáveis de software orientado a objetos",
        "preco": 120.00,
        "em_estoque": 80
    },
    {
        "id": 34,
        "nome": "Introdução aos Algoritmos",
        "descricao": "A bíblia dos algoritmos e estruturas de dados",
        "preco": 189.90,
        "em_estoque": 6
    },
    {
        "id": 35,
        "nome": "Refatoração",
        "descricao": "Aperfeiçoando o design de códigos existentes",
        "preco": 99.00,
        "em_estoque": 7
    }
]

# 2. Adicionando os novos dicionários à lista principal (catalogo_livros)
catalogo_livros.extend(novos_livros)

# 3. Atualizando o arquivo original 'catalogo.json' com a lista completa
with open("catalogo.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(catalogo_livros, arquivo_json, indent=4, ensure_ascii=False)

print(f"Arquivo 'catalogo.json' atualizado com sucesso! Total de livros no catálogo: {len(catalogo_livros)}.")

