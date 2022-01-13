from utils.GenUtils import read_lines
from BoggleBoard import BoggleBoard
from BoggleSolver import BoggleSolver


def main(dict_fn, board_fn):
    dictionary = read_lines(dict_fn)
    solver = BoggleSolver(dictionary)
    board = BoggleBoard(board_fn)

    score = 0
    for word in solver.get_all_valid_words(board):
        curr_score = solver.score_of(word)
        print(f"{word}\t{curr_score}")
        score += curr_score

    print(f"Total score: {score}")

    return


if __name__ == '__main__':
    dict_file = '/Users/sravan/Projects/ds_algo/problems/princeton_assignments/boggle/data/dictionary-common.txt'
    board_file = '/Users/sravan/Projects/ds_algo/problems/princeton_assignments/boggle/data/board-points100.txt'

    main(dict_file, board_file)

