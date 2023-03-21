# *****(3)Напишите программу, которая принимает на вход две строки и определяет,
# являются ли они анаграммами. Знаки препинания, пробелы и регистр при этом игнорируются.
# Пример ввода:
# Цари, вино и сало.
# Лисица и ворона.
# Пример вывода:
# YES

def String_Sep(string):
    list = []
    for i in string:
        list.append(i)
    return list

S1 = input("Введите первое слово: ")
S2 = input("Введите второе слово: ")

list1 = String_Sep(S1)
list2 = String_Sep(S2)

if " " in list1:
    list1.remove(" ")
if "," in list1:
    list1.remove(",")

if " " in list2:
    list2.remove(" ")
if "," in list2:
    list2.remove(",")

res = True

for i in list1:
    if i not in list2:
        res = False
        break

if res:
    print("Yes")
else:
    print("No")