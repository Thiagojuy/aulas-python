class Produto:
    def __init__(self, nome: str, preco: float, quantidade_estoque: int):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    def adicionar_estoque(self, quantidade: int):
        if quantidade > 0:
            self.__quantidade_estoque += quantidade
        else:
            print("Erro: Quantidade inválida")

    def realizar_venda(self, quantidade: int):
        if quantidade <= 0:
            print("Erro: Quantidade inválida")
        elif quantidade <= self.__quantidade_estoque:
            self.__quantidade_estoque -= quantity
            self.__quantidade_estoque -= quantidade

        else:
            print("Venda negada: Estoque insuficiente")

    # Ajustando o método realizar_venda sem duplicidade:
    def realizar_venda(self, quantidade: int):
        if quantidade > 0 and quantidade <= self.__quantidade_estoque:
            self.__quantidade_estoque -= quantidade
        elif quantidade > self.__quantidade_estoque:
            print("Venda negada: Estoque insuficiente")
        else:
            print("Erro: Quantidade inválida")

    def aplicar_desconto(self, percentual: float):
        if 0 < percentual <= 80:
            self.__preco -= self.__preco * (percentual / 100)
        else:
            print("Erro: Desconto inválido")

    def exibir_resumo(self):
        print(f"Produto: {self.__nome} | Preço: R${self.__preco:.2f} | Estoque: {self.__quantidade_estoque}")


meu_produto = Produto("Smartphone X", 2000.0, 10)


meu_produto.__quantidade_estoque = -50
meu_produto.__preco = -100


meu_produto.realizar_venda(9999)


print("\n--- Resumo do Produto ---")
meu_produto.exibir_resumo()

print("\n--- Dicionário Real do Objeto (__dict__) ---")
print(meu_produto.__dict__)
