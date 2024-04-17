import numpy as np

matriz = np.array([[1, 2], [2, 1]])

# Calcular los valores propios y los vectores propios
valores_propios, vectores_propios = np.linalg.eig(matriz)

# Imprimir los valores propios y vectores propios
print("Valores propios:")
print(valores_propios)
print("\nVectores propios:")
print(vectores_propios)
