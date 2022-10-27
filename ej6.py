def determinantedematriz(matriz, n):
    resultado = (n.linalg.det(matriz))
    return (int(round(resultado)))

#intentamos hacer una función que realice el determinante de una matriz    
import numpy as np
a = np.array([[65,33,65,33,65],[65,33,65,33,65],[65,33,65,33,65],[65,33,65,33,65],[65,33,65,33,65]])
d = np.linalg.det(a)
print(d)