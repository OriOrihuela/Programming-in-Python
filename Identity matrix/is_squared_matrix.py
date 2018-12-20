
def esCuadrada(matriz):
    for elemento in matriz:
        if len(elemento) != len(matriz):
            return False
    return True

#Casos Test para comprobar si la matriz es cuadrada

if __name__ == "__main__":


    correct = [[1,2,3],
            [2,3,1],
            [3,1,2]]
    assert esCuadrada(correct) == True


    correct2 = [[1,2,3,4],
                [2,3,1,3],
                [3,1,2,3],
                [4,4,4,2]]
    assert esCuadrada(correct2) == True


    correct3 = [[1,2,3,4],
                [2,3,1,2],
                [4,1,2,3],
                [2,3,1,4]]
    assert esCuadrada(correct3) == True


    correct4 = [[1,2,3,4,5],
                [2,3,1,5,6],
                [4,5,2,1,3],
                [3,4,5,2,1],
                [5,6,4,3,2]]
    assert esCuadrada(correct4) == True

    
    correct5 = [['a','b','c'],
                ['b','c','a'],
                ['c','a','b']]
    assert esCuadrada(correct5) == True


    correct6 = [ [1, 1.5],
                [1.5, 1]]
    assert esCuadrada(correct6) == True

        
    incorrect = [[1,2,3],
                [2,3,1]]
    assert esCuadrada(incorrect) == False


    incorrect2 = [[1,2,3],
                [2,3,1],
                [3,1]]
    assert esCuadrada(incorrect2) == False
