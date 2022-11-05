"""
Give an algorithm that takes a string S consisting of opening and closing
parentheses, say )()(())()()))())))(, and finds the length of the longest balanced
parentheses in S, which is 12 in the example above. (Hint: The solution is not
necessarily a contiguous run of parenthesis from S.)
"""


def longest_balanced_parentheses_subsequence(string):
    indices = list()
    right_indices = list()
    n = len(string)

    for idx in range(n-1, -1, -1):
        if string[idx] == ')':
            right_indices.append(idx)
        else:
            if len(right_indices):
                indices.append(idx)
                indices.append(right_indices.pop())

    picked = ''.join([string[idx] for idx in sorted(indices)])

    return picked, indices


string = '(()()(())()()))())))(((((((()'
longest, picked_indices = longest_balanced_parentheses_subsequence(string)

print(longest)
print(len(longest))
print(picked_indices)
print('\n')

print('\t'.join([str(x) for x in range(len(string))]))
print('\t'.join(string))