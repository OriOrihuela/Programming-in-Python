def numerosEnRango(sudoku):
    for elemento in sudoku:
        for numero in elemento:
            if isinstance(numero, str) or numero not in range(1, len(sudoku) + 1):
                return False
    return True    

### CASOS TEST para comprobar si los números van de 1..N

if __name__ == "__main__":


    correct = [[1,2,3],
            [2,3,1],
            [3,1,2]]


    if numerosEnRango(correct):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect = [[1,2,3,4],
                [2,3,1,3],
                [3,1,2,3],
                [4,4,4,2]]


    if numerosEnRango(incorrect):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect2 = [[1,2,3,4],
                [2,3,1,2],
                [4,1,2,3],
                [2,3,1,4]]


    if numerosEnRango(incorrect2):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect3 = [[1,2,3,4,5],
                [2,3,1,5,6],
                [4,5,2,1,3],
                [3,4,5,2,1],
                [5,6,4,3,2]]


    if numerosEnRango(incorrect3):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect4 = [['a','b','c'],
                ['b','c','a'],
                ['c','a','b']]


    if numerosEnRango(incorrect4):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect5 = [ [1, 1.5],
                [1.5, 1]]


    if numerosEnRango(incorrect5):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")

        
    irregular = [[1,2,3],
                [2,3,1]]


    if numerosEnRango(irregular):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    irregular2 = [[1,2,3],
                [2,3,1],
                [3,1]]


    if numerosEnRango(irregular2):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")

