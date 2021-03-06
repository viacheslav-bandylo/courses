# Координатные четверти
# Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек,
# лежащих в каждой координатной четверти. В первой строке записано количество точек. Каждая
# следующая строка состоит из двух целых чисел — координат точки (сначала абсцисса – x,
# затем ордината – y), разделенных символом пробела.


def quadrant(x, y):
    if x == 0 or y == 0:
        return 4
    elif x > 0:
        if y > 0:
            return 0
        else:
            return 3
    else:
        if y > 0:
            return 1
        else:
            return 2


answer = [0, 0, 0, 0, 0]
names = ["Первая четверть:", "Вторая четверть:", "Третья четверть:", "Четвертая четверть:"]
n = int(input())

for _ in range(n):
    x, y = input().split()
    answer[quadrant(int(x), int(y))] += 1

for i in range(4):
    print(names[i], answer[i])
