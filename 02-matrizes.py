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


# tentando multiplicar matrizes com tamanhos inválidos
A = np.array([[1, 2, 20], [3, 4, 50], [5, 6, 60]])
B = np.array([[7, 8], [9, 10]])

try:
    C = A @ B
    print("\nResultado da multiplicação:")
    print(C)
except ValueError as e:
    print(f"Erro: {e}")

print("\n\n")
#  ----------------------

# verificar a minha versão do cuda: PS> nvcc --version
# instalar o pytorch daqui: https://pytorch.org/get-started/locally/
# PS> pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

import torch
print("torch.cuda.is_available()? {}".format(torch.cuda.is_available()))
print("torch.version.cuda? {}".format(torch.version.cuda))
print("torch.__version__? {}".format(torch.__version__))

# Converter as matrizes para tensores do Pytorch
A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([[7, 8], [9, 10]])

A_tensor = torch.tensor(A)
B_tensor = torch.tensor(B)

# Usando o operador @
C_tensor = A_tensor @ B_tensor
print("\nResultado da multiplicação usando o operador @:")
print(C_tensor)

# Usando a função do Pytorch
D_tensor = torch.matmul(A_tensor, B_tensor)
print("\nResultado da multiplicação usando a função do Pytorch:")
print(D_tensor)







