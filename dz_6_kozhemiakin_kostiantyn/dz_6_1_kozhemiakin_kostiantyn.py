import random

# на вхід функії приймаємо міншмум і максимум діапазона загаданного числа і кількість спроб
def guess_int(min_int=0, max_int=100, attempts=6):
    # генеруємо рандомне число (загадане)
    guessed_num = random.randint(min_int, max_int)
    # проходимось циклом по кількості спроб
    for i in range(1, attempts + 1):
        # просимо ввести число
        guess = int(input('Enter your number\n'))
        # якщо введене число дорівнює загаданому - виходимо з циклу, видаємо сповіщення "ви вгадали"
        # видаємо кількість спроб
        if guess == guessed_num:
            print(f"You are right!\nThe number is: {guessed_num}\nNumber of attempts: {i}")
            break
        # якщо число менше - видаємо сповіщення "число менше"
        if guess < guessed_num:
            print("Your number is less than i guessed.")
        # інакше видаємо сповіщення "число більше"
        else:
            print("Your number is grather then i guessed.")
        # якщо кількість спроб вичерпана - видаємо сповіщення і закінчуємо програму
        if i == attempts:
            print("Sorry, you've run out of attempts.\nGame over.")
            break


guess_int()
