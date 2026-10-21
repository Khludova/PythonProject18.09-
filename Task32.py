N = float(input("Число полных часов и число полных минут: "))
hours = int(N // 30)
minutes = int((N % 30) // 0.5)
print("Прошло часов и минут:", hours, minutes)