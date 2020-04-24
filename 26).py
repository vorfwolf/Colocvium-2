#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#26. Напишіть програму аналізу значень температури хворого за добу:
#визначте мінімальне і максимальне значення, середнє арифметичне. Заміри
#температури виробляються шість раз на добу і результати вводяться з клавіатури у
#масив T.
import numpy as np #імпортуємо numpy

i = 1
T = np.zeros(6, dtype=float) #створюємо масив з нулями
for i in range(6):
    while True: #створюємо умову для зациклення, в разі невірного вводу користувачем
        try:
            T[i] = float(input(f'Введіть [{i+1}] температуру хворого: '))  # елементи масиву
            break
        except ValueError:
            print('Введіть лише число')

print(T)

print('Максимальна температура: ', max(T))
print('Мінімальна температура: ', min(T))
print('Середня температура: ', np.mean(T))