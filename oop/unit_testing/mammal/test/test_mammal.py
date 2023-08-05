from unittest import TestCase, main
from project.mammal import Mammal

class MammalTest(TestCase):
    def test_class_initialization(self):
        lion = Mammal("Jojo", "Lion", "Roar")
        self.assertEqual(lion.name, "Jojo")
        self.assertEqual(lion.type, "Lion")
        self.assertEqual(lion.sound, "Roar")
        self.assertEqual(lion._Mammal__kingdom, "animals")

    def test_make_sound(self):
        lion = Mammal("Jojo", "Lion", "Roar")
        result = lion.make_sound()
        expected = "Jojo makes Roar"
        self.assertEqual(expected, result)

    def test_get__kingdom(self):
        lion = Mammal("Jojo", "Lion", "Roar")
        result = lion.get_kingdom()
        expected = "animals"
        self.assertEqual(expected, result)

    def test_get_info(self):
        lion = Mammal("Jojo", "Lion", "Roar")
        result = lion.info()
        expected = f"Jojo is of type Lion"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
