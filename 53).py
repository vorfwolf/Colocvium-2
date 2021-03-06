#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#53. В масиві X (1: n) кожен елемент рівний 0, 1 або 5. Переставити елементи
#масиву так, щоб спочатку розташовувалися всі нулі, потім все одиниці, а потім всі
#п'ятірки. Додаткового масиву не заводити.
import numpy as np #імпортуємо numpy

n = int(input('Введіть довжину масиву: '))
q = np.random.choice([0, 1, 5], n) #масив з 0, 1, 2
print(q)
#сортуємо наш масив за допомогою алгоритму бульбашкового сортування
for i in range(n):  # зовнішній цикл для проходження по масиву
    flag = False  # прапор для оптимізації сортування
    for j in range(0, n - i - 1):  # внутрішній цикл
        if q[j] > q[j + 1]:  # якщо наступний елемент масиву менший за попередній
            q[j], q[j + 1] = q[j + 1], q[j]  # то міняємо їх місцями
            flag = True  # змінюємо прапор на правду
    if flag == False:  # знінюємо прапор на хибу
        break

print('Відсортований масив: ', q)
