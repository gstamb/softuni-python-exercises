from animal import Animal
from mammal import Mammal
from reptile import Reptile
from gorilla import Gorilla
from bear import Bear
from lizard import Lizard
from snake import Snake


if __name__ == "__main__":
    mammal = Mammal("Stella")
    print(mammal.__class__.__bases__[0].__name__)
    print(mammal.name)
    lizard = Lizard("John")
    print(lizard.__class__.__bases__[0].__name__)
    print(lizard.name)
