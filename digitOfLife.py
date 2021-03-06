def sum_of_digits(digits):
    sum = 0
    for i in digits:
        sum += int(i)
    return str(sum)


def digit_of_life(bdate):
    sum = sum_of_digits(bdate)
    while len(sum) != 1:
        sum = sum_of_digits(sum)
        
    return sum
    
user_bdate = input("Enter a birthday using only digits i.e. 19740819: ")
print(digit_of_life(user_bdate))

# bdate = '19991229'.split("")
# print(bdate)