import random
import numpy as np
from tqdm import tqdm

from DoesItPercolate import Percolate


class PercolateStats:
    def __init__(self, n, trials):
        self.trials = trials
        self.stats = list()

        for _ in tqdm(range(trials)):
            obj = Percolate(n)

            done = False
            while not done:
                grid_num = random.randint(0, n*n - 1)
                obj.activate(grid_num)
                done = obj.does_it_percolate()

            self.stats.append(float(obj.number_of_active_sites()) / (n * n))

        print(f"mean                    = {self.mean()}")
        print(f"std                     = {self.std_dev()}")
        print(f"95% Confidence Interval = [{self.confidence_low()}, {self.confidence_high()}]")
        return

    def mean(self):
        return np.mean(self.stats)

    def std_dev(self):
        return np.std(self.stats)

    def confidence_low(self):
        return self.mean() - (1.96 * self.std_dev() / np.sqrt(self.trials))

    def confidence_high(self):
        return self.mean() + (1.96 * self.std_dev() / np.sqrt(self.trials))


def main():
    PercolateStats(100, 100)
    return


if __name__ == "__main__":
    main()
