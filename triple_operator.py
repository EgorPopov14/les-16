import random
numbers=[]
for i in range(10):
    numbers.append(random.randint(a=0, b=100))
print(numbers)
print('Число 13 есть в списке')if 13 in numbers else print("Числа 13 нету в списке")
a=None
a='есть несчстливое китайское число'if 4 in numbers else'все норм'
print('Результат выражения:\n', a)
b=None
b='вы выйграли лям'if 10 in numbers else'вы проиграли'
print(b)