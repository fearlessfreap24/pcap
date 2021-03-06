def get_row(num):
    row = input(f"enter your row #{num}, 9 digits only: ")
    while len(row) != 9 or not row.isdigit() :
        row = input(f"enter your row #{num}, 9 digits only: ")
    return row

def check_numbers(numbers):
    one_to_nine = '123456789'
    for i in numbers:
        if i not in one_to_nine or numbers.count(i) != 1:
            return False
    return True

def check_row(numbers):
    for i in numbers:
        if not check_numbers(i):
            return False
    return True

def check_column(numbers):
    for i in range(len(numbers)):
        column = numbers[0][i] + numbers[1][i] + numbers[2][i] + numbers[3][i] + numbers[4][i] \
             + numbers[5][i] + numbers[6][i] + numbers[7][i] + numbers[8][i]
        if not check_numbers(column):
            return False
    return True


def check_subsquare(numbers):
    for i in range(0, len(numbers), 3):
        for j in range(0, len(numbers), 3):
            subsquare = numbers[i][j] + numbers[i][j+1] + numbers[i][j+2] + numbers[i+1][j] + numbers[i+1][j+1] \
                 + numbers[i+1][j+2] + numbers[i+2][j] + numbers[i+2][j+1] + numbers[i+2][j+2]
            if not check_numbers(subsquare):
                return False
    return True


def is_sudoku(numbers):
    if check_row(numbers) and check_column(numbers) and check_subsquare(numbers):
        return "Yes"
    else: return "No"

# good_numbers = ['295743861',
#             '431865927',
#             '876192543',
#             '387459216',
#             '612387495',
#             '549216738',
#             '763524189',
#             '928671354',
#             '154938672']

# bad_numbers = ['195743862',
#                 '431865927',
#                 '876192543',
#                 '387459216',
#                 '612387495',
#                 '549216738',
#                 '763524189',
#                 '928671354',
#                 '254938671']

# print(is_sudoku(good_numbers))
# print(is_sudoku(bad_numbers))

numbers = [get_row(i+1) for i in range(9)]
print(is_sudoku(numbers))