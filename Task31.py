X = int(input("Введите первое число (X): "))
Y = int(input("Введите второе число (Y): "))
result_mod = (X % Y) * (Y % X)
print(int(result_mod == 0))