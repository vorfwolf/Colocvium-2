#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#36. Знайти суму додатніх елементів лінійного масиву цілих чисел.
#Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.
import numpy as np #імпортуємо numpy

q = np.zeros(10, dtype = int) #створюємо масив з нулями
for i in range(10):
    while True:
        try:
            q[i] = int(input(f'q[{i}] = ')) #елементи масиву
            break
        except ValueError:
            print('Введіть лише ціле число') #помилка, у разі невірного вводу, виведемо
print(q)

k = [] #пустий список
for i in q: #проходимося по нашому масиві
    if i > 0: #якщо елемент додатній, то добавляємо його в список k
        k.append(i)
print(k)
print(sum(k)) #знаходимо і виводимо суму додатніх елементів масиву