"""
Создайте функцию process_list(a), которая принимает на вход список a, 
заполненный значениями от 0 до 1000. Функция должна вернуть True, 
если сумма элементов имеющих четные индексы больше чем сумма элементов имеющих не четные индексы.
""" #

def process_list(a):
    s1 = []
    s2 = []
    i = 0
    for el in a:
        if i % 2 == 0:
            s1.append(el)
        else:
            s2.append(el)
        i += 1
    return True if (sum(s1) > sum(s2)) else False

print(process_list([1234, 6734, 9531, 4523, 1354, 111, 999, 546]))