import numpy as np
import matplotlib.pyplot as plt
from math import *
print("Hello world")
# константа обозначается заглавной буквой
N = 100
x = np.array([i for i in range(N)]) # массив из N элементов
x = x*pi/(N-1) # вектор умножаем на скаляр
# создаем сетку от 0 до pi включительно с количеством элементов N
x1 = np.linspace(0,pi,N) # используем для того же функцию
# В узлах сетки рассчитываем значения функций sin и cos
y = np.sin(x)
y1 = np.cos(x1)
ax = plt.gca() # ссылка на текущий объект axes
plt.plot(x,y) # создаем обычный график sin
plt.plot(x1,y1) # создаем обычный график cos
ax.set_xlabel("angle, rad")
ax.set_ylabel("sin, cos function")
plt.show()
x2 = x1 - x1.max()/2
y2 = x2*x2
plt.plot(x2,y2)
plt.show()
y=y1
x_rol = np.zeros(N)
# копируем срез со сдвигом
# данная операция нужна, если сетка неравномерная
x_rol[0:N-1] = x[1:N]
xdif = x_rol-x
xdif[-1]=0.0 #?? как еще можно решить эту проблему
integral_rectangle = (y*xdif).sum()
y_rol = np.zeros(N)
# для метода трапеций копируем в массив со сдвигом
# в данном случае это необязательно
# ведь можно реализовать сумму от 1 до N-1
# и добавить первый и последний элемент, так как
# промежуточные суммы все равно совпадают
# попробуйте это показать математически
y_rol[0:N-1] = y[1:N]
y[-1] = 0.0 #?? как еще можно решить эту проблему
y_sum = ((y+y_rol)*0.5*xdif).sum()
integral_trapeze = y_sum
print(f"integral by rectangle {integral_rectangle}")
print(f"integral by trapeze {integral_trapeze}")
# пример работы с модулем time для учета времени работы
import time
t = time.time()
y = []
N = 10000
z = []
# добавление значений функции в список
for i in range(N):
 y = y+[sin(i*pi*2/N)]
 z.append(y[i])
print(y)
print(z)
dt = time.time()-t
print(f'Time {dt}')
import numpy as np
import matplotlib.pyplot as plt
from math import *
print("Hello world")
# константа обозначается заглавной буквой
N = 100
x = np.array([i for i in range(N)]) # массив из N элементов
x = x*pi/(N-1) # вектор умножаем на скаляр
# создаем сетку от 0 до pi включительно с количеством элементов N
x1 = np.linspace(0,pi,N) # используем для того же функцию
# В узлах сетки рассчитываем значения функций sin и cos
y = np.sin(x)
y1 = np.cos(x1)
ax = plt.gca() # ссылка на текущий объект axes
plt.plot(x,y) # создаем обычный график sin
plt.plot(x1,y1) # создаем обычный график cos
ax.set_xlabel("angle, rad")
ax.set_ylabel("sin, cos function")
plt.show()
x2 = x1 - x1.max()/2
y2 = x2*x2
plt.plot(x2,y2)
plt.show()
y=y1
x_rol = np.zeros(N)
# копируем срез со сдвигом
# данная операция нужна, если сетка неравномерная
x_rol[0:N-1] = x[1:N]
xdif = x_rol-x
xdif[-1]=0.0 #?? как еще можно решить эту проблему
integral_rectangle = (y*xdif).sum()
y_rol = np.zeros(N)
# для метода трапеций копируем в массив со сдвигом
# в данном случае это необязательно
# ведь можно реализовать сумму от 1 до N-1
# и добавить первый и последний элемент, так как
# промежуточные суммы все равно совпадают
# попробуйте это показать математически
y_rol[0:N-1] = y[1:N]
y[-1] = 0.0 # ?? как еще можно решить эту проблему
y_sum = ((y+y_rol)*0.5*xdif).sum()
integral_trapeze = y_sum
print(f"integral by rectangle {integral_rectangle}")
print(f"integral by trapeze {integral_trapeze}")
# пример работы с модулем time для учета времени работы
import time
t = time.time()
y =[]
N = 10000
z = []
# добавление значений функции в список
for i in range(N):
 y = y+[sin(i*pi*2/N)]
 z.append(y[i])
print(y)
print(z)
dt = time.time()-t
print(f'Time {dt}')