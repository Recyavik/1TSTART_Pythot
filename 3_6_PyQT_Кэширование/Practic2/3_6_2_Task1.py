# На прошлом уроке мы с вами применяли методы оптимизации, т.е. кэширования рекурсивных функций
# Мемоизация кода с помощью словарей для рекурсивной функции оказалась самой эффективной.
# Давайте разбираться в этом почему

# Рекурсивная функция – это функция, которая вызывает сама себя,
# и при каждом очередном вызове использует данные,
# созданные во время предыдущего вызова. В программировании есть ряд задач,
# которые проще (но не всегда эффективнее) решаются с помощью рекурсии.
# Написание рекурсивных функций часто ставит начинающих программистов в тупик.
# Чтобы разобраться в принципе работы рекурсивных функций,
# нужно понять (в самых общих чертах) концепцию стека вызовов.
# Стек – это структура данных LIFO (last in, first out):
# информация последовательно добавляется в «стопку» ,
# каждый новый объект помещается поверх предыдущего,
# а извлекаются объекты в обратном порядке, – начиная с верхнего.
# Работу стека отлично иллюстрирует добавление данных в список с помощью append
# и извлечение информации посредством pop:

stack = []
for i in range(1, 11):
    stack.append(f'{i}-й элемент')
    print(f'+ {i}-й элемент добавлен')
    for i in stack:
        print(i, end=" ")
print('\n')

for i in range(len(stack)):
    print('В стеке: ', end=" ")
    for i in stack:
        print(i, end=" ")
    print(f'\n{stack.pop()} удален из стека')

