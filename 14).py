#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#14. Сформуйте лінійний масив дійсних чисел, елементи якого є відстанями,
#пройденими тілом при вільному падінні на землю за 1, 2, ..., 10 с.
import numpy as np #імпортуємо numpy

a = np.array([])
print(np.append(a, [(9.81*1**2)/2, (9.81*2**2)/2, (9.81*3**2)/2, (9.81*4**2)/2, (9.81*5**2)/2, (9.81*6**2)/2,
                    (9.81*7**2)/2, (9.81*8**2)/2, (9.81*9**2)/2, (9.81*10**2)/2]))
#за формулою h=(g*t**2)/2 знаходимо і добавляємо елементи в масив