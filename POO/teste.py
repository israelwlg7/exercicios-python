from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au Au"
class Gato(Animal):
    def falar(self):
        return "Miau Miau"
cachorro1 = Cachorro("Jeick")
gato1 = Gato("shaw")
print(f"{cachorro1.name} fala: {cachorro1.falar()}")
print(f"{gato1.name} fala: {gato1.falar()}")