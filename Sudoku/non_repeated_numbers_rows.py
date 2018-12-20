

def numeroNoRepetidoFila(sudoku):
    for lista in sudoku:
        posicion = 0
        while posicion < len(lista): 
            if isinstance(lista[posicion], int) and lista[posicion] not in lista[posicion + 1:]:
                posicion = posicion + 1
            else:
                return False
    return True
  


if __name__ == '__main__':


### CASOS TEST para comprobar si los números son únicos en la misma fila.


    correct = [[1,2,3],
               [2,3,1],
               [3,1,2]]


    if numeroNoRepetidoFila(correct):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect = [[1,2,3,4],
                 [2,3,1,3],
                 [3,1,2,3],
                 [4,4,4,2]]


    if numeroNoRepetidoFila(incorrect):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect2 = [[1,2,3,4],
                [2,3,1,2],
                [4,1,2,3],
                [2,3,1,4]]


    if numeroNoRepetidoFila(incorrect2):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect3 = [[1,2,3,4,5],
                [2,3,1,5,6],
                [4,5,2,1,3],
                [3,4,5,2,1],
                [5,6,4,3,2]]


    if numeroNoRepetidoFila(incorrect3):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect4 = [['a','b','c'],
                ['b','c','a'],
                ['c','a','b']]


    if numeroNoRepetidoFila(incorrect4):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect5 = [ [1, 1.5],
                [1.5, 1]]


    if numeroNoRepetidoFila(incorrect5):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")

        
    irregular = [[1,2,3],
                [2,3,1]]


    if numeroNoRepetidoFila(irregular):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    irregular2 = [[1,2,3],
                [2,3,1],
                [3,1]]


    if numeroNoRepetidoFila(irregular2):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")
