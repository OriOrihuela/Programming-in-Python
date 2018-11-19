int numeros = {1,2,3,4,5,6,7,8,9}
int posIzquierda, posDerecha, posCentral
int numeroBuscado

def busquedaBinaria(lista, numeroBuscado)
    posIzquierda = numeros[0]
    posDerecha = len(numeros) - 1
    while posIzquierda <= posDerecha:
        posCentral = (posIzquierda+posDerecha) / 2
        if numeros[posCentral] == numeroBuscado:
            return posCentral
        elif numeros[posCentral] > numeroBuscado:
            posDerecha = posCentral - 1
        else:
            posIzquierda = posCentral + 1
    return - 1
print def busquedaBinaria(numeros, 8)