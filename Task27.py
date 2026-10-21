t = input("Введите три числа:")
# Считываем три числа из одной строки
K_str, N_str, R_str = t.split()

# Размножаем строку с числом K ровно N раз
big_number_str = K_str * int(N_str)

# Переводим получившееся огромное число в int и умножаем на R
result = int(big_number_str) * int(R_str)

# Выводим итоговый результат
print(result)