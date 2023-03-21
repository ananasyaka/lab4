try:
    a = int(input('Введите число '))
    b=100/a
except ValueError:
    print("Введено не число")
except ZeroDivisionError:
    print("Введен 0")
else:
     print("Результат деления = ",b)