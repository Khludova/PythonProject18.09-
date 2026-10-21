N_str, C_str, K_str = input("Напиши кол-во страниц, столбцов и номеров:").split()
N = int(N_str)
C = int(C_str)
K = int(K_str)
page_capacity = N * C
idx = K - 1
page = (idx // page_capacity) + 1
column = ((idx % page_capacity) // N) + 1
row = ((idx % page_capacity) % N) + 1
print("страница", int(page), "столбец", int(column), "строка", int(row))