# *****(4)Напишите функцию, которая принимает словарь с параметрами и возвращает строку запроса,
# сформированную из отсортированных в лексикографическом порядке параметров.
# Пример:
# Код print(query({'course': 'python', 'lesson': 2, 'challenge': 17})) должен возвращать строку:
# challenge=17&course=python&lesson=2

def query(dict):
    string = "&".join(sorted(f"{k}={v}" for k, v in dict.items()))
    return string

print(query({'course': 'python', 'lesson': 2, 'challenge': 17}))

