class ItemDoPedido:
    def __init__(self, produto: str, quantidade: int, preço_unitario: float):
        self.produto = produto
        self.quantidade = quantidade
        self.preço_unitario = preço_unitario
        
    def calcular_subtotal(self) -> float:
        return self.quantidade * self.preço_unitario
    
class Pedido:
    def __init__(self, id_cliente: int):
        self.id_cliente = id_cliente
        self._itens = []
        print(f"\nPedido criado para o cliente {self.id_cliente}.")
            
    def adicionar_item(self, produto: str, quantidade: int, preço_unitario: float):
        novo_item = ItemDoPedido(produto, quantidade, preço_unitario)
        self._itens.append(novo_item)
        print(f" - Item '{produto}' adicionado ao pedido. ")
        
    def calcular_total(self):
        total = sum(item.calcular_subtotal() for item in self._itens)
        print(f"Total do Pedido: R${total: .2f}")
        
pedido_123 = Pedido(957)
    
pedido_123.adicionar_item("Notebook Gamer", 1, 5000.000)
pedido_123.adicionar_item("Mouse sem fio", 2, 150.00)
pedido_123.adicionar_item("Fone de ouvido (sem fio)", 1, 50.00)
pedido_123.adicionar_item("Teclado gamer rgb", 2, 450.00)
pedido_123.adicionar_item("Mouse ped", 4, 14.99)
pedido_123.calcular_total()
    