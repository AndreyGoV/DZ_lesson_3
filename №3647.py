'''Задача №3647. Утренняя пробежка
В первый день спортсмен пробежал 𝑥 километров, а затем он
каждый день увеличивал пробег на 10% от предыдущего значения.
По данному числу 𝑦 определите номер дня, на который пробег
спортсмена составит не менее 𝑦 километров.

Входные данные
Программа получает на вход действительные числа 𝑥 и 𝑦

Выходные данные
Программа должна вывести одно натуральное число.'''

x = 10
y = 20

day = 1
distance = x
while distance < y:
    distance += distance * 0.1
    day += 1
print(day)