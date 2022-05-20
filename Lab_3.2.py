#Дано дійсне A та ціле число N (> 0). Вивести 1 – A + A2 – A3 + ... + (–1)**N*A**N.
#Виконав: Супрун Богдан.
A = float(input("Ввести число: "))
N = int(input("Ввести число: "))
B = [(-1)**i*A**i for i in range(N)]
print(B)
i = 0
Sum = 0
while i < len(B):
    Sum = Sum + B[i]
    i = i + 1
print("Sum = ", Sum)