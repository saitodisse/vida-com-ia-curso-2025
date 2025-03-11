import numpy as np

# Representar as matrizes A e B usando NumPy
A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([[7, 8], [9, 10]])

# Imprimir as matrizes para verificar
print("Matriz A:")
print(A)
print("\nMatriz B:")
print(B)

# Verificar se as matrizes podem ser multiplicadas
if A.shape[1] != B.shape[0]:
    print("As matrizes não podem ser multiplicadas.")
else:
    print("As matrizes podem ser multiplicadas pois o número de colunas de A é igual ao número de linhas de B. O resultado será uma matriz com o número de linhas de A e o número de colunas de B.")

# Usando o operador builtin do Python @
C = A @ B
print("\nResultado da multiplicação usando o operador @:")
print(C)


# Usando o Numpy
D = np.dot(A, B)
print("\nResultado da multiplicação usando o Numpy:")
print(D)



