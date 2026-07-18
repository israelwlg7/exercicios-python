class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def Ligar(self):
        print("O carro está ligando...")

    def Desligar(self):
        print("O carro está desligando...")

    def ExibirInformaçõesDesteCarro(self):
        print(self.marca, self.modelo, self.ano)

carro1 = Carro("Toyota", "Corolla", 2020)
carro1.Ligar()
carro1.Desligar()
carro1.ExibirInformaçõesDesteCarro()