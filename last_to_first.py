# Сдвиг в развитии
# На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел.
# Напишите программу циклического сдвига элементов списка направо, когда последний элемент становится первым,
# а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.

numbers = input().split()
numbers.insert(0, numbers.pop())

print(*numbers)
