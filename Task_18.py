# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка содержит число X

list = []
#list = [8, 34, 234, 1, 667, 3, 87]
N = int(input("Введите N: "))
X = int(input("Введите X (число которое нужно найти): "))

for i in range(1, N+1):
    list.append(i)
print(f"Список чисел: {list}")

if X in list:
    print(f"Число {X} есть внутри списка")
elif X not in list:
    i = 1
    while X not in list:
        if X+i in list:
            print(f"Ближайшее число к {X} - {X + i}")
            break
        elif X-i in list:
            print(f"Ближайшее число к {X} - {X-i}")
            break
        i += 1