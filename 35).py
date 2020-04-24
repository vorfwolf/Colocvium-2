#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#35. Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по спаданню.
k = [] #пустий масив
while True:  # створюємо умову для зациклення, в разі невірного вводу користувачем
    try:
        n = int(input('Введіть кількість елементів масиву"максимальна кількість-30": '))  # запитуємо користувача, кількість елементів, яку він хоче задати
        if (n < 1 or n > 30):  # кількість елементів може бути від 1 до 30
            print('Кількість елементів масиву має бути не більше 30 і не менше 1')  # в разі невірного вводу, виведемо
            continue
        break
    except ValueError:
        print('Ви можете ввести лише цілі числа від 0 до 30')  # помилка, у разі невірного вводу, виведемо
for i in range(n):
  while True:
    try:
      k.append(int(input('Елемент масиву: ')))  # елементи масиву
      break
    except ValueError:
      print('Введіть лише ціле число')  # помилка, у разі невірного вводу, виведемо
print(k)

a = sorted(k, reverse=True) #порівнюємо масив до сортування і після сортування
if k == a:
  print('Масив упорядкований по спаданню')
else:
  print('Масив не упорядкований по спаданню')
