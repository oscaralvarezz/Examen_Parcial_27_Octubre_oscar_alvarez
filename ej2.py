#desde otro repositorio cuyo nombre es  (examen_oscar) y cuyo link es:
#https://github.com/oscaralvarezz/examen_oscar.git

#metemos entonces el ya realizado algoritmo.

def mergesort(lista):
    "Método para ordenar denominado mergesort"
    if (len(lista) <= 1):
        return lista
    else:
        medio = len(lista) // 2
        izquierda = []
        for i in range(0,medio):
            izquierda.append(lista[i])
        derecha = []
        for i in range(medio,len(lista)):
            derecha.append(lista[i])
        izquierda = mergesort(izquierda)
        derecha = mergesort(derecha)
        if (izquierda[medio-1] <= derecha[0]):
            izquierda += derecha
            return izquierda
        resultado = merge(izquierda,derecha)
        return resultado

def merge(izquierda,derecha):
    "Función que mezcla las listas"
    lista_mezclada = []
    while (len(izquierda) > 0) and (len(derecha) > 0):
        if(izquierda[0]<derecha[0]):
            lista_mezclada.append(izquierda.pop(0))
        else:
            lista_mezclada.append(derecha.pop(0))
    if (len(izquierda)>0):
        lista_mezclada += izquierda
    if (len(derecha)>0):
        lista_mezclada += derecha
    return lista_mezclada

lista = [18, 50, 210, 80, 145, 333, 70, 30]
print(mergesort(lista))


#por otro lado, metemos también el algoritmo de centinela, realizado también previamente en el mismo 
#repositorio de práctica de examen, realizado anteriormente.

def centinela(lista, buscado):
    "Método de busqueda (secuencial)"
    posicion = -1
    for i in range(0,len(lista)):
        if (lista[i]== buscado):
            posicion = i
            break
    return posicion

print(centinela(lista, 145))
if 145 not in lista:
    print(-1)

    