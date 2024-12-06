from produto import Produto
from datetime import datetime
from teste_produto import produto1, produto2
from venda import Venda

venda = Venda(datetime.now(), 50.0, 5.0, "Desconto")
valor_total = venda.calcular_valor_total()
troco = venda.calcular_troco(300)

print("Produto 1:", produto1.descricao, "Estoque:", produto1.estoque)
print("Produto 2:", produto2.descricao, "Estoque:", produto2.estoque)
print("Valor total:", valor_total)
print("Troco:", troco)

