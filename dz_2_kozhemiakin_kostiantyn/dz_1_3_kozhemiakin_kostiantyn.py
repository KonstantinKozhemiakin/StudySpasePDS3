test_list = [1, 8, 5, 4, 12]


def avg_list(my_list=[]):
    sum_list = 0
    for num in my_list:
        try:
            sum_list += num
        except:
            return None
    return sum_list/len(my_list)


print(avg_list(test_list))
