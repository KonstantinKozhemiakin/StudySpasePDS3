my_name = 'Kozhemiakin Kostiantyn'
def printname(my_name = my_name):
    your_name = input('Enter your surname and name or click Enter to print my name')
    if your_name == "":
        print(my_name)
    else:
        print(your_name)
printname()
