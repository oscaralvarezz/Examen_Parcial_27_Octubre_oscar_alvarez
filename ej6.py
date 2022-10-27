#intentamos hacer una función que realice el determinante de una matriz sin importar.   
matriz = [[2,6,8,11,3], [3,5,1,0,1], [3,4,8,8,8], [9,5,1,2,64],[9,3,18,11,1]]

def factor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i] + m[i+1:])]
def hacer_determinante(matriz):
    if len(matriz)==2:
        valor = matriz[0][0] * matriz [1][1] - matriz [1][0]
    suma = 0
    for columna_actual in range(len(matriz)):

        signo = (-1) ** (columna_actual)
        sub_det = hacer_determinante(factor(matriz, 0, columna_actual))
        suma += (signo * matriz[0][columna_actual] * sub_det)
    return suma

print("El determinante es:", hacer_determinante(matriz))
