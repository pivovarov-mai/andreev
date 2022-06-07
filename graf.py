import numpy as np
import matplotlib.pyplot as plt

def main():
    X = [i for i in np.arange(-2, 5, 0.1)]
    Y = []
    Z = []
    for i in X:
        Y.append(2**i-i**2-0.5)
        Z.append(0)
    plt.plot(X, Y, label = 'Функция')
    plt.plot(X, Z, label = 'Ось Х')
    plt.legend()
    plt.grid()
    plt.savefig('function.png')
    print('Посмотрите график функции сохраненный в файл function и перейдите в программу main')

if __name__ == '__main__':
    main()