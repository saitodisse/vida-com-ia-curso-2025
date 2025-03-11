import math

import numpy as np

def distancia_euclidiana_com_numpy(vetor1, vetor2):
  """
  Calcula a distância euclidiana entre dois vetores usando numpy.

  Args:
    vetor1: Uma lista ou tupla representando o primeiro vetor.
    vetor2: Uma lista ou tupla representando o segundo vetor.

  Returns:
    A distância euclidiana entre os dois vetores.
  """
  # Converte as listas para arrays numpy
  vetor1_np = np.array(vetor1)
  vetor2_np = np.array(vetor2)
  
  return np.linalg.norm(vetor1_np - vetor2_np)

# pede para o usuario digitar os vetores
vetor1 = list(map(float, input("Digite os valores do primeiro vetor separados por espaço: ").split()))
vetor2 = list(map(float, input("Digite os valores do segundo vetor separados por espaço: ").split()))

# calcula a distância euclidiana entre os dois vetores
resultado = distancia_euclidiana_com_numpy(vetor1, vetor2)
print(f">> np.linalg.norm({vetor1} - {vetor2}) = {resultado:.2f}")
  
