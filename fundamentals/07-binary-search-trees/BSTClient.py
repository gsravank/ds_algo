from BinarySearchTree import BinarySearchTree
from utils.DSUtils import print_tree
import random
from tqdm import tqdm
import pandas as pd


def main():
    initial_heights = list()
    end_heights = list()

    all_items = list(range(10000))
    population = random.sample(all_items, 3000)
    sec_population = [x for x in all_items if x not in population]
    exceptions = list()

    for _ in tqdm(range(100)):
        try:
            items = random.sample(population, 2048)
            random.shuffle(items)
            bst = BinarySearchTree()
            for item in items:
                bst.insert_rec(item)
            initial_height = bst.assign_heights()

            sec_idx = 0
            for _ in range(10000):
                if random.random() <= 0.5:
                    item = sec_population[sec_idx]
                    bst.insert_rec(item)
                    sec_idx += 1
                    items.append(item)
                else:
                    bst.delete(random.sample(items, 1)[0])

            initial_heights.append(initial_height)
            end_heights.append(bst.assign_heights())
        except Exception as e:
            exceptions.append(e.__str__())
            pass

    df = pd.DataFrame({'initial': initial_heights, 'final': end_heights})
    print(df.describe([0.01, 0.05, 0.1, 0.2, 0.25, 0.5, 0.75, 0.8, 0.9, 0.95, 0.99]))
    print(len(exceptions))

    return


if __name__ == "__main__":
    main()