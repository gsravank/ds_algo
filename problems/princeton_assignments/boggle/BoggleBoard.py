from utils.GenUtils import read_lines


class BoggleBoard:
    def __init__(self, filename):
        lines = read_lines(filename)
        m, n = [int(x) for x in lines[0].strip().split(' ')]

        assert m > 0 and n > 0

        self.board = []
        for idx in range(1, m + 1):
            line = lines[idx]
            line = line.replace("Qu", "Q").replace("QU", "Q")
            self.board.append([x for x in line.strip().split(' ') if len(x)])

        return

    def rows(self):
        return len(self.board)

    def cols(self):
        return len(self.board[0])

    def get_letter(self, i, j):
        return self.board[i][j]

    def to_string(self):
        return '\n'.join(['\t'.join(line).replace("Q", "Q") for line in self.board])


if __name__ == "__main__":
    board_file = '/Users/sravan/Projects/ds_algo/problems/princeton_assignments/boggle/data/board-q.txt'
    board = BoggleBoard(board_file)

    print('\n'.join(read_lines(board_file)))
    print('\n')
    print(board.to_string())
