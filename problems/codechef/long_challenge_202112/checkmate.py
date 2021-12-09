import sys
input = sys.stdin.readline


def is_in_check(xk, yk, x1, y1):
    if xk == x1 and yk == y1:
        return False
    else:
        if xk == x1 or yk == y1:
            return True
        else:
            return False


def move_possible(xk, yk, x1, y1, x2, y2):
    move_found = False
    for x_diff in [-1, 0, 1]:
        for y_diff in [-1, 0, 1]:
            if x_diff != 0 or y_diff != 0:
                x_new = xk + x_diff
                y_new = yk + y_diff

                if 1 <= x_new <= 8 and 1 <= y_new <= 8:
                    if not (is_in_check(x_new, y_new, x1, y1) or is_in_check(x_new, y_new, x2, y2)):
                        move_found = True

    return move_found


def get_next_rook_positions(x, y, x_other,  y_other):
    positions = list()
    if x == x_other:
        # vertical moves
        min_height = 1 if y < y_other else y_other + 1
        max_height = 8 if y > y_other else y_other - 1
        for idx in range(min_height, max_height + 1):
            positions.append([x, idx])
        # horizontal moves
        for idx in range(1, 9):
            positions.append([idx, y])
    elif y == y_other:
        # vertical moves
        for idx in range(1, 9):
            positions.append([x, idx])
        # horizontal moves
        min_width = 1 if x < x_other else x_other + 1
        max_width = 8 if x > x_other else x_other - 1
        for idx in range(min_width, max_width + 1):
            positions.append([idx, y])
    else:
        for idx in range(1, 9):
            positions.append([idx, y])
        for idx in range(1, 9):
            positions.append([x, idx])
    return positions


def can_check_mate(xk, yk, x1, y1, x2, y2):
    # Check next position for each rook
    # Check if the move produces a check and king has no other move
    # print(x1, y1)
    for x1_new, y1_new in get_next_rook_positions(x1, y1, x2, y2):
        # print(x1_new, y1_new)
        if x1_new != x2 or y1_new != y2:
            if (is_in_check(xk, yk, x1_new, y1_new) or is_in_check(xk, yk, x2, y2)) and not move_possible(xk, yk, x1_new, y1_new, x2, y2):
                return True

    # print(x2, y2)
    for x2_new, y2_new in get_next_rook_positions(x2, y2, x1, y1):
        # print(x2_new, y2_new)
        if x2_new != x2 or y2_new != y2:
            if (is_in_check(xk, yk, x1, y1) or is_in_check(xk, yk, x2_new, y2_new)) and not move_possible(xk, yk, x1, y1, x2_new, y2_new):
                return True

    return False


if __name__ == '__main__':
    for _ in range(int(input())):
        x_k, y_k = list(map(int, input().strip().split(' ')))
        x_1, y_1 = list(map(int, input().strip().split(' ')))
        x_2, y_2 = list(map(int, input().strip().split(' ')))

        if can_check_mate(x_k, y_k, x_1, y_1, x_2, y_2):
            print("YES")
        else:
            print("NO")
