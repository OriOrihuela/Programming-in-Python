def numerosEnRango(matriz):
    for elemento in matriz:
        for numero in elemento:
            if isinstance(numero, str) or numero not in range(2):
                return False
    return True    

### CASOS TEST para comprobar si los números van de 0..1

if __name__ == "__main__":


    correct = [[1,2,3],
            [2,3,1],
            [3,1,2]]
    assert numerosEnRango(correct) == True
    
    
    correct2 = [[1,2,3,4],
                [2,3,1,2],
                [4,1,2,3],
                [2,3,1,4]]
    assert numerosEnRango(correct2) == True

    
    incorrect = [[1,2,3,4],
                [2,3,1,3],
                [3,1,2,3],
                [4,4,4,2]]
    assert numerosEnRango(incorrect) == False


    incorrect2 = [[1,2,3,4,5],
                [2,3,1,5,6],
                [4,5,2,1,3],
                [3,4,5,2,1],
                [5,6,4,3,2]]
    assert numerosEnRango(incorrect2) == False

    
    incorrect3 = [['a','b','c'],
                ['b','c','a'],
                ['c','a','b']]
    assert numerosEnRango(incorrect3) == False


    incorrect4 = [ [1, 1.5],
                [1.5, 1]]
    assert numerosEnRango(incorrect4) == False

        
    incorrect5 = [[1,2,3],
                [2,3,1]]
    assert numerosEnRango(incorrect5) == False


    incorrect6 = [[1,2,3],
                [2,3,1],
                [3,1]]
    assert numerosEnRango(incorrect6) == False
