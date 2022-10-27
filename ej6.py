#intentamos hacer una función que realice el determinante de una matriz importando numpy.   
def determinante_recursivo(A, total=0):
    indices = list(range(len(A)))
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
    for fc in indices:
        As = copia_matriz(A)
        As = As[1:]
        height = len(As)
 
        for i in range(height): 
            As[i] = As[i][0:fc] + As[i][fc+1:] 
 
        signo = (-1) ** (fc % 2) 
        sub_det = determinante_recursivo(As)
        total += signo * A[0][fc] * sub_det 
        return total

        