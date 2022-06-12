import copy
import random


# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents: list = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(f"{key}")

    def draw(self, how_many: int):
        if how_many > self.contents.__len__():
            result = self.contents
            self.contents = []
            return result

        balls = []
        for i in range(how_many):
            balls.append(self.contents.pop(random.randint(0, ((self.contents.__len__()) - 1))))
        return balls


def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int):
    total_acomplished: int = 0

    for i in range(num_experiments):
        hat_to_experiment = copy.deepcopy(hat)
        compished_experiment: bool = True
        ball_get: dict = {}
        for ball in hat_to_experiment.draw(num_balls_drawn):
            try:
                ball_get[ball] += 1
            except KeyError:
                ball_get[ball] = 1
        condition = contains(get_keys(ball_get), get_keys(expected_balls))
        if condition:
            for key, value in expected_balls.items():
                if ball_get[f"{key}"] >= value:
                    continue
                else:
                    compished_experiment = False
                    break
        else:
            compished_experiment = False
        if compished_experiment:
            total_acomplished += 1

    print(total_acomplished / num_experiments)
    return total_acomplished / num_experiments


def get_keys(dictionary: dict):
    result: list = []
    for key, value in dictionary.items():
        result.append(key)
    return result


def contains(set_container, set_being_containing):
    for element in set_being_containing:
        if not(element in set_container):
            return False
    return True
