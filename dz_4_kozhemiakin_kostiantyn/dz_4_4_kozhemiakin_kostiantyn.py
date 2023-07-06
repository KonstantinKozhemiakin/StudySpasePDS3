def sum_digits(digit):
    if isinstance(digit, int) == True:
        return (sum([int(i) for i in str(digit)]))
    else:
        return 0


print(sum_digits(123))
