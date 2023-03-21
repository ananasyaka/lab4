try:
    a = int(input('Введите число '))
except ValueError:
    print("Введено не число")
else:
    if a % 3 == 0:
     print("Число делится на 3")
    else:
     print("Число не делится на 3")


