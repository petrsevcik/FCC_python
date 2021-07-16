import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for color, number in kwargs.items():
            for i in range(number):
                self.contents.append(color)

    def show_contents(self):# to be deleted
        return self.contents

    def draw(self, no_draw):
        list_from_draw = []
        copy_contents = self.contents.copy()
        if no_draw <= len(self.contents):
            for i in range(no_draw):
                random_item = random.choice(self.contents)
                self.contents.remove(random_item)
                list_from_draw.append(random_item)
            return list_from_draw

        if no_draw > len(self.contents):
            times = no_draw // len(self.contents)
            modulo = no_draw % len(self.contents)
            for i in range(times):
                list_from_draw.extend(self.contents)
            for i in range(modulo):
                random_item = random.choice(self.contents)
                self.contents.remove(random_item)
                list_from_draw.append(random_item)
            return list_from_draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    count = []
    for key in expected_balls:
        count.append(expected_balls[key])
    successes = 0

    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls = new_hat.draw(num_balls_drawn)

        no_of_balls = []
        for key in expected_balls:
            no_of_balls.append(balls.count(key))

        if no_of_balls >= count:
            successes += 1

    return successes/num_experiments

#hat = Hat(red=5,blue=2)
#actual = hat.draw(2)
#expected = ['blue', 'red']
#print(actual)

hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=5)
print(probability)