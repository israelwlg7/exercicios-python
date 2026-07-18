# Aula 1 - Introdução à Programação Orientada a Objetos (POO)
#Classe é um molde para criar objetos. Ela define as características e comportamentos que os objetos criados a partir dela terão.
#syntax para criar uma classe:



class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def ligar(self):
        print("estou ligando")

    def desligar(self):
        print("estou desligando")

    def ExibirInformaçõesDesteComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

computador1 = Computador("Dell", "16GB", "NVIDIA GeForce RTX 3060")
computador1.ligar()
computador1.desligar()
computador1.ExibirInformaçõesDesteComputador()

# uma classe e uma forma de agrupar dados e comportamentos relacionados a um objeto específico. Ela serve como um modelo para criar objetos, permitindo que você defina atributos (características) e métodos (comportamentos) que os objetos criados a partir da classe terão.