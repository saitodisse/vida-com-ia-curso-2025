import math

def distancia_euclidiana(vetor1, vetor2):
  """
  Calcula a distância euclidiana entre dois vetores.

  Args:
    vetor1: Uma lista ou tupla representando o primeiro vetor.
    vetor2: Uma lista ou tupla representando o segundo vetor.

  Returns:
    A distância euclidiana entre os dois vetores.
  """

  if len(vetor1) != len(vetor2):
    raise ValueError("Os vetores devem ter a mesma dimensão.")
  else:
    print("Os vetores têm a mesma dimensão. OK")

  soma_quadrados = 0
  for i in range(len(vetor1)):
    print(f"{vetor2[i]} - {vetor1[i]} = {vetor2[i] - vetor1[i]}")
    soma_quadrados += (vetor2[i] - vetor1[i]) ** 2
    print(f"Quadrado da diferença: {(vetor2[i] - vetor1[i]) ** 2}")
    print("")

  raiz_quadrada = math.sqrt(soma_quadrados)
  print(f"Raiz quadrada: {raiz_quadrada}")

  return raiz_quadrada

# pede para o usuario digitar os vetores
vetor1 = list(map(float, input("Digite os valores do primeiro vetor separados por espaço: ").split()))
vetor2 = list(map(float, input("Digite os valores do segundo vetor separados por espaço: ").split()))

# 1. verificar se os vetores tem a mesma dimensão
resultado = distancia_euclidiana(vetor1, vetor2)
print(f"A distância euclidiana entre {vetor1} e {vetor2} é: {resultado:.2f}")

