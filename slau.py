def input_A(kol_strok,myA):
    myA = [list(map(float, (input(f"строка {i+1}: ").split()))) 
        for i in range(kol_strok)]
    return (myA)

def input_B(myB):
    myB = map(float, input("Введите матрицу правых частей, пробелы между числами: ").split())
    myB = list(myB)
    return (myB)

def Output(A, B, selected):
    for row in range(len(B)):
        print("(", end='')
        for col in range(len(A[row])):
             print("\t{1:1.3f}{0}".format(" " if (selected is None
or selected != (row, col)) else "*", A[row][col]), end='')
        print("\t) * (\tX{0}) = (\t{1:1.3f})".format(row + 1, B[row]))
    print('')

def RowSwap(A, B, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]

def RowDivide(A, B, row, divider):
    A[row] = [a / divider for a in A[row]]
    B[row] /= divider

def RowSum(A, B, row, source_row, coefficient):
    A[row] = [(a + k * coefficient) for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * coefficient

def Gauss(A, B):
    column = 0
    while column < len(B):
        RowDivide(A, B, column, A[column][column])
        Output(A, B, (column,column))
        for i in range(len(A) - 1 - column):
            RowSum(A, B, i+1+column, column, -A[i + 1 + column][column])
        Output(A, B, (column,column))
        column += 1
    X = [0 for b in B]
    for i in range(len(B)-1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))
    for i in range(len(X)):
        print(f'x{i+1} = {round(X[i], 2)}')

def main():
    myA = []
    myB = []
    kol_strok = int(input('Введите количество строк матрицы коэффициентов:'))
    myA = input_A(kol_strok,myA)
    myB = input_B(myB)
    Gauss(myA, myB)

main()