
# Se requiere que el número de columnas de la matrizA
# sea igual al número de filas de la matrizB. en ésta
# función se da por supuesto que sí son iguales. Por tanto,
# los casos test están acorde a ello. 


def multiplicar_2_matrices(matrizA, matrizB):
    matrizC = []
    fila = 0
    fila_A = len(matrizA)
    while fila < fila_A:
        columna = 0 
        columna_B = len(matrizB[0])
        while columna < columna_B:
            resultado = 0
            columna_actual = 0
            columna_A = len(matrizA[0]) ### Columnas de la matriz A 
            while columna_actual < columna_A:
                resultado += (matrizA[fila][columna_actual] * matrizB[columna_actual][columna]) ### EL ERROR SALE AQUÍ
                columna_actual += 1
            matrizC.append(resultado)
            columna += 1
        fila += 1
    return matrizC


if __name__ == "__main__":

    ### CASOS TEST ###

    matriz1 = [[1,6,7],
                [5,8,9],
                [6,7,9]]
    
    #   multiplicar por   #

    matriz2 = [[1,6,7,5,3],
                [6,3,7,2,1],
                [7,3,1,6,7]]
    
    print(multiplicar_2_matrices(matriz1, matriz2))



    matriz3 = [[1,6],
                [5,8],
                [6,7]]
    
    #   multiplicar por   #

    matriz4 = [[1,6,7,5,3,6,2],
                [6,3,7,2,1,7,9]]
    
    print (multiplicar_2_matrices(matriz3,matriz4))



    matriz5 = [[1,6,7,5,6],
                [5,8,9,7,2],
                [6,7,9,1,1]]
    
    #   multiplicar por   #

    matriz6 = [[1,6,7],
                [6,3,7],
                [7,3,1]
                [1,1,1]
                [7,5,7]]
    
    print (multiplicar_2_matrices(matriz5,matriz6))