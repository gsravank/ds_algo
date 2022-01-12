def horizontal_zeros_between(row, col_left, col_right, nz_matrix, matrix):
    if nz_matrix[row][col_right] == nz_matrix[row][col_left]:
        return matrix[row][col_left] == '0'
    else:
        return True


def vertical_zeros_between(col, row_top, row_bottom, nz_matrix, matrix):
    if nz_matrix[row_bottom][col] == nz_matrix[row_top][col]:
        return matrix[row_top][col] == '0'
    else:
        return True


def compute_num_square_frames(matrix, n):
    nz_ltor = list()
    nz_ttob = [[0 for _ in range(n)] for _ in range(n)]
    for row in range(n):
        ltor_list = list()
        nzs = 0
        for val in matrix[row]:
            if val == '0':
                nzs += 1
            ltor_list.append(nzs)
        nz_ltor.append(ltor_list)
    for j in range(n):
        nzs = 0
        for i in range(n):
            if matrix[i][j] == '0':
                nzs += 1
            nz_ttob[i][j] = nzs

    # for row in nz_ltor:
    #     print(row)

    # for row in nz_ttob:
    #     print(row)

    num_square_frames = 0
    for size_of_square in range(1, n + 1):
        for i_top in range(n - size_of_square + 1):
            for j_left in range(n - size_of_square + 1):
                i_bottom = i_top + size_of_square - 1
                j_right = j_left + size_of_square - 1
                # Four checks
                if not horizontal_zeros_between(i_bottom, j_left, j_right, nz_ltor, matrix) and not horizontal_zeros_between(i_top, j_left, j_right, nz_ltor, matrix) and not vertical_zeros_between(j_right, i_top, i_bottom, nz_ttob, matrix) and not vertical_zeros_between(j_left, i_top, i_bottom, nz_ttob, matrix):
                    # print(i_top, j_left, i_bottom, j_right)
                    num_square_frames += 1

    return num_square_frames


for _ in range(int(input())):
    N = int(input())
    mat = list()
    for _ in range(N):
        mat.append(input().strip())
    
    print(compute_num_square_frames(mat, N))
    