#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#9. З 8 до 20 години температура повітря вимірювалася щогодини. Відомо,
#що протягом цього часу температура знижувалася. Визначте, о котрій годині було
#вперше зафіксовано від'ємну температуру.
import numpy as np #імпортуємо numpy

a = np.zeros(13, dtype=int) #створюємо масив з нулями
a[-1] = 1000
for i in range(13):
    while True: #створюємо умову для зациклення, в разі невірного вводу користувачем
        try:
            a[i] = int(input(f'Температура повітря за {i+8}:00: '))
            if a[i] >= a[i-1]:
                print('Введіть значення нижче за попереднє, адже температура за умовою задачі з кожною годиною зменшується')
            else:
                break
        except ValueError:
            print('Введіть лише ціле число')
print(a)

for i in range(len(a)): #проходимося по нашому масиві
    if a[i] < 0: #якщо елемент масиву  менший за нуль, то виводимо
        print(f"О {i+8}:00 було вперше зафіксовано від'ємну температуру")
        break
    else: #в іншому випадку виводимо
        print("Від'ємної температури немає")

