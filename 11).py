#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#11. Дані про температуру води на Чорноморському узбережжі за декаду
#вересня зберігаються в масиві. Визначити, скільки за цей час було днів, придатних для купання.
import numpy as np #імпортуємо numpy

q = np.zeros(10, dtype = int) #створюємо масив з нулями
for i in range(10):
    while True: #створюємо умову для зациклення, в разі невірного вводу користувачем
        try:
            q[i] = int(input(f'{i+1} температура води на Чорноморському узбережжі за декаду\
вересня: ')) #елементи масиву
            break
        except ValueError:
            print('Введіть лише ціле число')
print(q)

k = 0 #кількість днів, придатних для купання
for i in range(len(q)): #проходимося по нашому масиві
    if q[i] > 25: #якщо елемент більший за 25, то добавляємо +1
        k += 1
print(f'Днів, придатних для купання: {k} ')
