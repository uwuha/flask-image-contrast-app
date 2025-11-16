import time
import numpy
import math

# интеграл с использованием массивов numpy
def integral_np(x,f):
 return ((f[0:-1]+f[1:])*(x[1:]-x[0:-1])*0.5).sum()
# интеграл стандартным способом
def integral(x,f):
 s = 0.0
 for i in range(min(len(x),len(f))-1):
 s = s+(f[i+1]+f[i])*(x[i+1]-x[i])*0.5
 return s
N = 10000
# задаем функцию по которой ведется расчет
x = numpy.array([i*math.pi/N for i in range(N)])
f = numpy.sin(x)
# выводим значение интеграла и время расчета
t = time.time()
print(integral_np(x,f))
dt = time.time() - t
print(f"Время работы равно: {dt} ")
# выводим значение интеграла и время расчета
# расчет интеграла обычным способом
t = time.time()
print(integral(x,f))
dt = time.time() - t
print(f"Время работы равно: {dt} ")