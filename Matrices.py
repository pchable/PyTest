import numpy as np

def multiplication_matrices():

    mat_a = np.array([[1, 2, 0], [4, 3, -1]])
    mat_b = np.array([[5, 1], [2, 3], [3, 4]])
    mat_c = mat_a.dot(mat_b)

    print("Matrice A")
    print(mat_a)

    print("Matrice B")
    print(mat_b)

    print("Matrice Produit")
    print(mat_c)

