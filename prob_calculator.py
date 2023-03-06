import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **kwargs):
        self.contents = []

        for key in kwargs.keys():
            self.contents = self.contents + [key]*kwargs[key]

    def draw(self, N):
        if N > len(self.contents):
            return self.contents
        else:
            sample = random.sample(self.contents, k=N)
            for sampled in sample:
                self.contents.remove(sampled)
            return sample


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    M = 0
    hats = [copy.deepcopy(hat) for i in range(0, num_experiments)]
    experiments = []

    for i in range(0, num_experiments):
        experiments.append(hats[i].draw(num_balls_drawn))

    last_key = list(expected_balls.keys())[-1]

    for exp in experiments:
        for key in expected_balls:
               if key != last_key:
                    if exp.count(key) < expected_balls[key]:
                        break
                    elif key == last_key and exp.count(key) >=expected_balls[key]:
                        M += 1

    probability = M/num_experiments
    return probability
