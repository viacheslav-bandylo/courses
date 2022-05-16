# Камень, ножницы, бумага
# Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов".
# Для этого они решили сыграть в камень, ножницы и бумагу. Помогите ребятам бросить честный
# жребий и определить, кто будет делать очередной модуль нового курса.

variants = [['камень', 'камень', 'ничья'], ['камень', 'ножницы', 'Тимур'], ['камень', 'бумага', 'Руслан'],
            ['ножницы', 'ножницы', 'ничья'], ['ножницы', 'бумага', 'Тимур'], ['ножницы', 'камень', 'Руслан'],
            ['бумага', 'бумага', 'ничья'], ['бумага', 'камень', 'Тимур'], ['бумага', 'ножницы', 'Руслан']]
game = [input() for _ in range(2)]

for var in variants:
    if game == var[:2]:
        print(var[2])