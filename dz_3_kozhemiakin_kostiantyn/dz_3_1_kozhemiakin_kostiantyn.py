def fibonacci():
    f1 = 0
    f2 = 1
    sum_f = 0
    while True:
        print(f2)
        sum_f = f1+f2
        f1 = f2
        f2 = sum_f


print(fibonacci())
