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




