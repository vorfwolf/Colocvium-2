#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#2. Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
#екран значення коріння і квадратів кожного з елементів масиву.
import numpy as np #імпортуємо numpy
X = np.array([4,9,16,8,5]) #масив
print(X)
print(*X**2) #значення квадрату елементів масиву
print(*X**(1/2)) #значення корення елементів масиву
