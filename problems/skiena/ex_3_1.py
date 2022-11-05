"""
A common problem for compilers and text editors is determining whether
the parentheses in a string are balanced and properly nested. For example, the
string ((())())() contains properly nested pairs of parentheses, while the strings
)()( and ()) do not. Give an algorithm that returns true if a string contains
properly nested and balanced parentheses, and false if otherwise. For full credit,
identify the position of the first offending parenthesis if the string is not properly
nested and balanced.
"""


def validate_parenthesis_string(string):
    count = 0

    for char in string:
        if char == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            return False

    return count == 0

string = '((())())()'
string = ')()('
string = '(())'
string = '((((()((((()))))))))'
print(validate_parenthesis_string(string))
