from Trie import Trie
import time
from BoggleBoard import BoggleBoard
from utils.GenUtils import read_lines


class BoggleSolver:
    def __init__(self, dictionary):
        self.trie = Trie(dictionary)
        self.root = self.trie.root
        return

    def get_all_valid_words(self, board):
        valid_words = list()
        
        # Setup state of board
        m = board.rows()
        n = board.cols()
        state = [[0 for _ in range(n)] for _ in range(m)]
        
        # Iterate over each starting character and explore the board
        # Add valid words to the set
        for i in range(m):
            for j in range(n):
                chars_collected = list()
                curr_node = self.root
                self.explore_and_collect(i, j, state, board, curr_node, valid_words, chars_collected, 0)
        
        valid_words = [x.replace("Q", "QU") for x in sorted(list(set(valid_words)))]
        return valid_words

    def explore_and_collect(self, i, j, state, board, curr_node, valid_words, chars_collected, num_chars):
        curr_char = board.get_letter(i, j)
        if curr_char in curr_node.next:
            state[i][j] = 1
            chars_collected.append(curr_char)
            num_chars += 1

            if curr_node.next[curr_char].val == 1 and num_chars >= 3:
                valid_words.append(''.join(chars_collected))

            # All possible steps that you can take from here
            for i_diff in range(1, -2, -1):
                for j_diff in range(1, -2, -1):
                    if i_diff == 0 and j_diff == 0:
                        continue

                    new_i = i + i_diff
                    new_j = j + j_diff

                    if 0 <= new_i < board.rows() and 0 <= new_j < board.cols():
                        if state[new_i][new_j] == 0:
                            self.explore_and_collect(new_i, new_j, state, board, curr_node.next[curr_char], valid_words,
                                                     chars_collected, num_chars)

            # Backtracking
            state[i][j] = 0
            chars_collected.pop()

        return
    
    def score_of(self, word):
        if self.trie.is_present(word):
            m = len(word)
            if 3 <= m <= 4:
                return 1
            elif m == 5:
                return 2
            elif m == 6:
                return 3
            elif m == 7:
                return 5
            elif m >= 8:
                return 11
        return 0


def main(dict_fn, board_fn):
    dictionary = read_lines(dict_fn)
    solver = BoggleSolver(dictionary)
    board = BoggleBoard(board_fn)

    print(board.to_string())
    print('\n')

    t1 = time.time()
    solver.get_all_valid_words(board)
    t2 = time.time()
    print(f"Time taken (sec): {t2 - t1}\n")

    score = 0
    for word in solver.get_all_valid_words(board):
        curr_score = solver.score_of(word)
        print(f"{word} {curr_score}")
        score += curr_score

    print(f"Total score: {score}")

    return


if __name__ == '__main__':
    dict_file = '/Users/sravan/Projects/ds_algo/problems/princeton_assignments/boggle/data/dictionary-algs4.txt'
    board_file = '/Users/sravan/Projects/ds_algo/problems/princeton_assignments/boggle/data/board-q.txt'

    main(dict_file, board_file)

