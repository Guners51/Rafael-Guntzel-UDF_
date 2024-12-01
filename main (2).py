import os

# Define o código PlantUML para o Diagrama de Casos de Uso
use_case_uml = """
@startuml
actor Cliente
actor Vendedor
actor Gerente

Cliente --> (Consultar Produtos)
Vendedor --> (Registrar Pedido)
Gerente --> (Gerenciar Produtos)
Gerente --> (Gerar Relatórios)
@enduml
"""

# Define o código PlantUML para o Diagrama de Classes
class_diagram_uml = """
@startuml
class Produto {
    - id: int
    - nome: string
    - preco: float
    + atualizarPreco()
}

class Pedido {
    - id: int
    - data: date
    - cliente: Cliente
    + calcularTotal()
}

class Cliente {
    - id: int
    - nome: string
    - endereco: string
    + realizarPedido()
}

class Gerente {
    - id: int
    - nome: string
    + gerarRelatorios()
}

Produto "1" --> "*" Pedido
Pedido "*" --> "1" Cliente
@enduml
"""

# Função para salvar o código PlantUML em arquivos
def save_uml_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

# Salva os arquivos UML
save_uml_file("use_case_diagram.puml", use_case_uml)
save_uml_file("class_diagram.puml", class_diagram_uml)

# Exemplos de uso das classes
class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

    def atualizarPreco(self, novo_preco):
        self.preco = novo_preco
        print(f"Preço atualizado de {self.nome} para R${self.preco:.2f}")

class Pedido:
    def __init__(self, id, data, cliente, produtos):
        self.id = id
        self.data = data
        self.cliente = cliente
        self.produtos = produtos

    def calcularTotal(self):
        total = sum([produto.preco for produto in self.produtos])
        print(f"Total do Pedido #{self.id}: R${total:.2f}")
        return total

class Cliente:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def realizarPedido(self, pedido):
        print(f"{self.nome} realizou o pedido #{pedido.id}.")

class Gerente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def gerarRelatorios(self):
        print(f"{self.nome} gerou um relatório de vendas.")

# Exemplo de instâncias
produto1 = Produto(1, "Camiseta", 49.90)
produto2 = Produto(2, "Calça", 99.90)

# Atualizando preço de um produto
produto1.atualizarPreco(45.00)

cliente = Cliente(1, "Carlos Silva", "Rua A, 123")
pedido = Pedido(101, "2024-12-01", cliente, [produto1, produto2])

# Cliente realizando pedido
cliente.realizarPedido(pedido)

# Calculando o total do pedido
pedido.calcularTotal()

# Gerando relatório
gerente = Gerente(1, "João Pereira")
gerente.gerarRelatorios()

# Instruções para gerar os diagramas
print("\nOs arquivos PlantUML foram gerados: 'use_case_diagram.puml' e 'class_diagram.puml'.")
print("Use o PlantUML para converter esses arquivos em imagens.")
