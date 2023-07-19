class GuineaPig:
    def __init__(self, food, hay, cover, weight):
        self.food = float(food) * 1000
        self.hay = float(hay) * 1000
        self.cover = float(cover) * 1000
        self.weight = float(weight) * 1000

    def eat(self, day):
        self.food -= 300
        if day % 2 == 0:
            hay = .05 * self.food
            self.hay -= hay
        if day % 3 == 0:
            cover = self.weight / 3
            self.cover -= cover

        enough_food = self.check_quantity()
        return enough_food

    def check_quantity(self):
        if self.food <= 0 or self.hay <= 0 or self.cover <= 0:
            return False
        else:
            return True

    def __repr__(self):
        rep = f"Food quantity: {self.food} - Hay quantity: {self.hay} -" \
              f" Cover quantity {self.cover} - Weight: {self.weight}"
        return rep


inputs = [input() for x in range(4)]
puppy = GuineaPig(inputs[0], inputs[1], inputs[2], inputs[3])
for i in range(1, 31):
    if puppy.eat(i):
        continue
    else:
        print("Merry must go to the pet store!")
        break
else:
    print(
        f"Everything is fine! Puppy is happy! Food: "
        f"{puppy.food / 1000:.2f}, Hay: {puppy.hay / 1000:.2f}, Cover: {puppy.cover / 1000:.2f}.")
