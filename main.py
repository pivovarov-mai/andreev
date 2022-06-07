import matplotlib.pyplot as plt
import numpy as np

Err = []
Err2 = []


eps = 0.001
function_f = lambda x: 2**x-x**2-0.5
function_phi = lambda x: (2**x-0.5)**(1/2)
derivative = lambda x: np.log(2)*2**x-2*x
second_derivative = lambda x: np.log(2)**2*2**x-2


def Iterative_Method(x_min, eps, Err):
    last_result = 0
    iteration = 0
    while (abs(last_result - x_min) > eps):
        Err.append(x_min)
        iteration += 1
        last_result = x_min
        x_min = function_phi(x_min)
    print("\nКоличество итераций методом итераций:", iteration)
    Erry = [x_min for i in range(iteration)]
    X0 = [i for i in range(iteration)]
    plt.plot(X0, Erry, label = 'Корень уравнения')
    plt.plot(X0, Err, label = 'корни метода простыых итерацияй')
    plt.legend()
    plt.grid()
    plt.savefig('calculation_error.png')
    return x_min


def Newton_Method(x_min, x_max, eps, Err2):
    last_result = 0
    iteration = 0
    if ((function_f(x_min) * second_derivative(x_min)) > 0):
        while (abs(last_result - x_min) > eps):
            Err2.append(x_min)
            iteration += 1
            last_result = x_min
            x_min = x_min - function_f(x_min) / derivative(x_min)
        print("\nКоличество итераций методом Ньютона:", iteration)
        X0 = [i for i in range(iteration)]
        plt.plot(X0, Err2, label = 'Корни метода Ньютона')
        plt.legend()
        return x_min
    else:
        while (abs(last_result - x_max) > eps):
            Err2.append(x_max)
            iteration += 1
            last_result = x_max
            x_max = x_max - function_f(x_max) / derivative(x_max)
        print("\nКоличество итераций методом Ньютона:", iteration)
        X0 = [i for i in range(iteration)]
        plt.plot(X0, Err2, label = 'Корни метода Ньютона')
        plt.legend()
        return x_max


x_min = float(input("Введите начальное значение интервала x_min: "))
x_max = float(input("Введите конечное значение интервала x_max: "))

if (function_f(x_min) * function_f(x_max) > 0):
    print("На данном интервале корней у функции нет!")

else:
    print("Методом Ньютона с точностью до 0.001 =", "%.3f" % Newton_Method(x_min, x_max, 0.001, Err2))
    print("Mетодом итераций с точностью до 0.001 =", "%.3f" % Iterative_Method(x_min, 0.001, Err))
