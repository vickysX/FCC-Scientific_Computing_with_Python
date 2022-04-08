import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = list()
        for color in balls:
            for i in range(0, balls[color]):
                self.contents.append(color)

    def draw(self, balls_to_draw):
        if balls_to_draw >= len(self.contents):
            return self.contents
        balls_removed = list()
        for i in range(0, balls_to_draw):
            ind = random.randrange(0, len(self.contents))
            balls_removed.append(self.contents[ind])
            self.contents.pop(ind)
        return balls_removed

    def __repr__(self):
        the_hat = dict()
        for ball in self.contents:
            the_hat[ball] = the_hat.get(ball, 0) + 1
        return the_hat

    def __str__(self):
        return str(self.__repr__())

hat1 = Hat(yellow=3, blue=2, green=6)
print(hat1.contents)
print(hat1)
print(hat1.draw(4))
print(hat1.contents)
print(hat1)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    prob_num = 0
    for i in range(0, num_experiments):
        experimental_hat = copy.copy(hat)
        balls_removed = experimental_hat.draw(num_balls_drawn)
        actual_balls = dict()
        for ball in balls_removed:
            actual_balls[ball] = actual_balls.get(ball, 0) + 1
        for key in expected_balls:
            if key not in actual_balls.keys() or actual_balls[key] != expected_balls[key]:
                break;
            else:
                prob_num += 1
    print(prob_num)
    probability = prob_num / num_experiments
    return probability

hat = Hat(black=6, red=4, green=3)
prob = experiment(hat=hat, 
        expected_balls={"red": 2, "green": 1},
        num_balls_drawn=5,
        num_experiments=2000)
print(prob)
