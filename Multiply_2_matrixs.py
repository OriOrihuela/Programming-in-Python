
# Se requiere que el número de columnas de la matrizA
# sea igual al número de filas de la matrizB. en ésta
# función se da por supuesto que sí son iguales. Por tanto,
# los casos test están acorde a ello. 



def getMatrixProduct(matrizA, matrizB):
        
        if len(matrizA[0]) != len(matrizB):
            return - 1 

        posfila_A = 0
        result = []
        fila_result = []
        
        while posfila_A < len(matrizA):

            poscolumna_B = 0

            while poscolumna_B < len(matrizB[0]):
                
                r = 0
                indiceActual = 0

                while indiceActual < len(matrizA[0]):
                    r += matrizA[posfila_A][indiceActual] * matrizB[indiceActual][poscolumna_B]
                    indiceActual += 1
                
                fila_result.append(r)
                poscolumna_B += 1
            
            result.append(fila_result)
            fila_result = []
            posfila_A += 1
            
        return result





if __name__ == "__main__":

    ### CASOS TEST ###

    matriz1 = [[1,6,7],
                [5,8,9],
                [6,7,9]]
    
    #   multiplicar por   #

    matriz2 = [[1,6,7,5,3],
                [6,3,7,2,1],
                [7,3,1,6,7]]
    
    print(getMatrixProduct(matriz1, matriz2))



    matriz3 = [[1,6],
                [5,8],
                [6,7]]
    
    #   multiplicar por   #

    matriz4 = [[1,6,7,5,3,6,2],
                [6,3,7,2,1,7,9]]
    
    assert (getMatrixProduct(matriz3,matriz4))



    matriz5 = [[1,6,7,5,6],
                [5,8,9,7,2],
                [6,7,9,1,1]]
    
    #   multiplicar por   #

    matriz6 = [[1,6,7],
                [6,3,7],
                [7,3,1],
                [1,1,1],
                [7,5,7]]
    
    assert getMatrixProduct(matriz5,matriz6)