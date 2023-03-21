"cddfj"
a = input('Введите номер билета ')
l1 = 0
l2 = 0
if len(a) % 2 == 0:
    p = int(len(a)/2)
    k = int(len(a)) + 1
    for i in a[0:p]:
        l1 = l1 + int(i)
    for i in a[p:k]:
        l2 = l2 + int(i)
    if l1 == l2:
        print("Билет счастливый")
    else:
        print("Билет не счастливый")
else:
    print("Кол-во чисел нечетное")


