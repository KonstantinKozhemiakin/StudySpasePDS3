sum = 0
for i in range(10):
    num = input('Enter an integer')
    if num.isdigit():
        sum += int(num)
print(f"Sum is: {sum}")
