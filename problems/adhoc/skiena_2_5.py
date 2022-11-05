import matplotlib.pyplot as plt
from tqdm import tqdm


def g(n):
    count = 0
    for k in range(1, n+1):
        x = k
        while x < n:
            count += 1

            x = 2 * x
    return count


n_s = list()
counts = list()
max_n = 10**4

for i in tqdm(range(1, max_n + 1)):
    n_s.append(i)
    counts.append(g(i))

import random

for x in sorted(random.sample(list(range(1, max_n)), 10)):
    print(n_s[x - 1], counts[x - 1])

fig, ax = plt.subplots(1, 1, figsize=(5, 5))
_ = ax.plot(n_s, n_s)
_ = ax.plot(n_s, counts)
_ = ax.legend(['y=x', 'f(n)'])
_ = plt.show()
