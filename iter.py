import math

a = [[-11,-9,0,0,0],
     [5,-15,-2,0,0],
     [0,-8,11,-3,0],
     [0,0,6,-15,4],
     [0,0,0,3,6]]

b = [-122,-48,-14,-50,42]

def print_arr( string, namevec, a ):
    if (type(a) == int) or (type(a) == float):
        print(a)
    else:
        print( string )
        for k in range(len(a)):   
            print("{}[{}] = {:8.4f}".format(namevec, k, a[k]))
            

def isCorrectArray(a):
    n = len(a)
    
    for row in range(0, n):
        if( len(a[row]) != n ):
            print('Не соответствует размерность')
            return False
        
    for row in range(1, n - 1):
        if(abs(a[row][row]) < abs(a[row][row - 1]) + abs(a[row][row + 1])):
            print('Не выполнены условия достаточности')
            return False

    if (abs(a[0][0]) < abs(a[0][1]))or(abs(a[n - 1][n - 1]) < abs(a[n - 1][n - 2])):
        print('Не выполнены условия достаточности')
        return False
        
    
    for row in range(0, len(a)):
        if( a[row][row] == 0 ):
            print('Нулевые элементы на главной диагонали')
            return False
    return True

def solution(a, b):
    if( not isCorrectArray(a) ):
        print('Ошибка в исходных данных')
        return -1 

    n = len(a)
    x = [0 for k in range(0, n)]
    print('Размерность матрицы: ',n,'x',n)
    
    v = [0 for k in range(0, n)]
    u = [0 for k in range(0, n)]

    v[0] = a[0][1] / (-a[0][0]) 
    u[0] = ( - b[0]) / (-a[0][0]) 
    for i in range(1, n - 1): 
        v[i] = a[i][i+1] / ( -a[i][i] - a[i][i-1]*v[i-1] )
        u[i] = ( a[i][i-1]*u[i-1] - b[i] ) / ( -a[i][i] - a[i][i-1]*v[i-1] )
    v[n-1] = 0
    u[n-1] = (a[n-1][n-2]*u[n-2] - b[n-1]) / (-a[n-1][n-1] - a[n-1][n-2]*v[n-2])
    
    print_arr('Прогоночные коэффициенты v: ','v', v)
    print_arr('Прогоночные коэффициенты u: ','u', u)
    
    x[n-1] = u[n-1]
    for i in range(n-1, 0, -1):
        x[i-1] = v[i-1] * x[i] + u[i-1]
        
    return x    
                
x = solution(a, b)
print_arr('Решение: ','x', x)