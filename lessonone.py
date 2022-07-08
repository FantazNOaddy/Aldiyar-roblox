import random
print("угадай число от 1 до 100")
secret_number = random.randint(1, 100)
my_number = 0
attempt = 3

while secret_number != my_number:
    my_number = int(input("введите число: "))
    if my_number == secret_number:
        print("вы победили")
    elif my_number >= secret_number:
        print("число меньше")
        attempt -= 1
    else:
        print("число больше")
        attempt -= 1
    if attempt == 0:
        print("вы проиграли")
        break
    