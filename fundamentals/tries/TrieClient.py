from RWayTrie import RWayTrie
from Trie import Trie
import random

def main():
    # obj = RWayTrie()
    obj = Trie()

    alphabet = 'abc'
    str_len = 5
    words = list()
    for _ in range(20):
        curr_word = ''.join(random.choices(alphabet, k=random.randint(1, str_len)))
        if obj.contains(curr_word):
            print(f"{curr_word} is already in the trie")
        else:
            print(f"Inserting {curr_word}")
        obj.put(curr_word, 1)
        words.append(curr_word)
    print(len(set(words)))

    num_twos = 0
    for word in words:
        if random.random() <= 0.5:
            obj.put(word, 2)
            num_twos += 1

    for word in words:
        print(f"{word} {obj.contains(word)} {obj.get(word)}")

    print(f'\nNum twos: {num_twos}')
    return


if __name__ == "__main__":
    main()