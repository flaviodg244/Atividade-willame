class Venda:
    def __init__(self, data_venda, valor, quantidade_vendida, forma_pagamento):
        self.data_venda = data_venda
        self.valor = valor
        self.quantidade_vendida = quantidade_vendida
        self.forma_pagamento = forma_pagamento
    
    def calcular_valor_total(self):
        return self.valor * self.quantidade_vendida
    
    def calcular_troco(self, valor_pago):
        return valor_pago - self.calcular_valor_total()
