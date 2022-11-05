from collections import defaultdict


def divisors(n):
    result = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            result.add(i)
            result.add(n//i)
    return sorted(list(result))


def check(cum_sum_map, num_pieces, max_array_elem, array_sum, n):
    if num_pieces > n:
        return False
    each_piece = array_sum // num_pieces
    # if max_array_elem > each_piece:
    #     return False
    # print(f"Searching in map for: {[i * each_piece for i in range(1, num_pieces + 1)]}")

    return all([i * each_piece in cum_sum_map for i in range(1, num_pieces + 1)])


def get_min_ops(array, n):
    max_elem = max(array)
    cs_map = defaultdict(int)
    cs_arr = list()
    curr_sum = 0
    for item in array:
        curr_sum += item
        cs_arr.append(curr_sum)
        cs_map[curr_sum] += 1
    arr_sum = curr_sum

    # print(f"Array sum: {arr_sum}")
    # print(f"Array cum sum: {cs_arr}")
    # print(f"Array cum sum map: {cs_map}")

    if arr_sum == 0:
        num_zeros = cs_map[0]  # len([x for x in cs_arr if x == 0])
        num_pieces = num_zeros
        # print(f"Zero total sum. Num zeros = Num pieces = {num_pieces}")
    else:
        sign = -1 if arr_sum < 0 else 1
        sum_divisors = divisors(arr_sum * sign)

        # print(f"Sign: {sign}")
        # print(f"Divisors: {sum_divisors}")

        for sum_each_piece in sum_divisors:
            num_pieces = (arr_sum * sign) // sum_each_piece
            # print(f"Sum each piece: {sum_each_piece}. Max array elem: {max_elem} Num pieces: {num_pieces}")

            if check(cs_map, num_pieces, max_elem, arr_sum, len(array)):
                # print(f"Found answer. Sum each piece: {sum_each_piece}. Num pieces: {num_pieces}")
                break

    return len(array) - num_pieces


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))

    print(get_min_ops(arr, n))
