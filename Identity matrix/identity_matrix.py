# Dada una lista de lista representando una matriz n*n:
# Define una rutina que devuelve True si la entrada es una matriz indentidad
# y False en otro caso.

# Una matriz identidad es una matriz cuadrada en la que todos los elementos
# en la diagonal principal son 1 y el resto de elementos fuera de la
# diagonal principal son 0. 
# (Una matriz cuadrada es una matriz con el numero de filas
# igual al numero de columnas)

from es_cuadrada_matriz import esCuadrada
from numeros_en_rango_matriz import numerosEnRango

def esMatrizIdentidad(matriz):
    if not esCuadrada(matriz) and numerosEnRango(matriz):
        return False
	posicionUnoCorrecta = 0
	contadorUnos = 0
	contadorFalsos = 0

	for fila in matriz:
		for elemento in fila:
			if elemento == 1:
				posicionUno = fila.index[elemento]
				contadorUnos += 1
			elif elemento != 0:
				contadorFalsos += 1
		if contadorUnos != 1 or contadorFalsos != 0 or posicionUno != posicionUnoCorrecta:
			return False
		contadorUnos = 0 
		posicionUnoCorrecta +=1
	return True



### CASOS TEST ###

if __name__ == "__main__":

    matrix1 = [[1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]]
    
    assert esMatrizIdentidad(matrix1) == True

    matrix2 = [[1,0,0],
            [0,1,0],
            [0,0,0]]

    assert esMatrizIdentidad(matrix2) == False 

    matrix3 = [[2,0,0],
            [0,2,0],
            [0,0,2]]

    assert esMatrizIdentidad(matrix3) == False 

    matrix6 = [[1,0,0,0],  
            [0,1,0,2],  
            [0,0,1,0],  
            [0,0,0,1]]

    assert esMatrizIdentidad(matrix6) == False 

    matrix7 = [[1, -1, 1],
            [0, 1, 0],
            [0, 0, 1]]
   
    assert esMatrizIdentidad(matrix7) == False           


    # casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert):

    matrix4 = [[1,0,0,0],
            [0,1,1,0],
            [0,0,0,1]]

    assert esMatrizIdentidad(matrix4) == False

    matrix5 = [[1,0,0,0,0,0,0,0,0]]

    assert esMatrizIdentidad(matrix5) == False
