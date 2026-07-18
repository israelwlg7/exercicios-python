class Veiculo:
    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
    def apresentar(self):
        print(f"{self._marca} {self._modelo} {self._ano}")
class Carro(Veiculo):
    def apresentar(self):
        print("isso e um carro")
        super().apresentar()
    def abrir_porta(self):
        print("abrindo a porta do carro")
class Moto(Veiculo):
    def apresentar(self):
        print("isso e uma moto")
        super().apresentar()
    def empinar(self):
        print("empinando a moto")
carro1 = Carro("Kwid", "Zen", 2025)
moto1 = Moto("Honda", "CB500X", 2024)
carro1.apresentar()
carro1.abrir_porta()
print()
moto1.empinar()
moto1.apresentar() 