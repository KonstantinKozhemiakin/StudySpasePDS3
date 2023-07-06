def recursion_desc():
    def rec(number):
        print(number)
        if number == 0:
            return None
        rec(number - 1)

    num = input('Enter integer\n')
    if num.isdigit():
        rec(int(num))


recursion_desc()
