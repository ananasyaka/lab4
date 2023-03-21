a = input('Введите дату ДД.ММ.ГГ ')
a = a.split('.')
if int(a[0]) * int(a[1]) == int(a[2]):
    print("Дата магическая")
else: print("Дата не магическая")