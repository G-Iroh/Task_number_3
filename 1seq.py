""" Задание:
Пользователь вводит количество элементов будущего списка
После этого по очереди по одной вводит любые цифры
Сохранить цифры в список
Отсортировать список по возрастанию и вывести на экран"""


quantity = input("Введите количество элементов: ")
conclusion = []

for i in range(int(quantity)):
    quantity_count = int(input(f"Введите {i+1} элемент: "))
    conclusion.append(quantity_count)

conclusion.sort()
print(conclusion)
