class Produto:
    def __init__(self, nome, descricao, valor, estoque):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.estoque = estoque
    
    def incrementar_estoque(self, quantidade):
        self.estoque += quantidade

    def decrementar_estoque(self, quantidade):
        if self.estoque >= quantidade:
            self.estoque -= quantidade
            return True
        else:
            return False