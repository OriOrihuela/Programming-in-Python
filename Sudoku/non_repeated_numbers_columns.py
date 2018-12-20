
def numeroNoRepetidoColumna(sudoku):
    i = 0
    while i < len(sudoku):
        numerosColumna = []
        for lista in sudoku:
            if len(lista) != len(sudoku):
                return False
            numerosColumna.append(lista[i])
        i = i + 1
    for numero in numerosColumna:
        if numerosColumna.count(numero) > 1:
            return False  
    return True



if __name__ == '__main__':


### CASOS TEST para comprobar si los números son únicos en la misma columna.


    correct = [[1,2,3],
               [2,3,1],
               [3,1,2]]


    if numeroNoRepetidoColumna(correct):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect = [[1,2,3,4],
                 [2,3,1,3],
                 [3,1,2,3],
                 [4,4,4,2]]


    if numeroNoRepetidoColumna(incorrect):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect2 = [[1,2,3,4],
                [2,3,1,2],
                [4,1,2,3],
                [2,3,1,4]]


    if numeroNoRepetidoColumna(incorrect2):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect3 = [[1,2,3,4,5],
                [2,3,1,5,6],
                [4,5,2,1,3],
                [3,4,5,2,1],
                [5,6,4,3,2]]


    if numeroNoRepetidoColumna(incorrect3):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect4 = [['a','b','c'],
                ['b','c','a'],
                ['c','a','b']]


    if numeroNoRepetidoColumna(incorrect4):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect5 = [ [1, 1.5],
                [1.5, 1]]


    if numeroNoRepetidoColumna(incorrect5):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")

        
    irregular = [[1,2,3],
                [2,3,1]]


    if numeroNoRepetidoColumna(irregular):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    irregular2 = [[1,2,3],
                [2,3,1],
                [3,1]]


    if numeroNoRepetidoColumna(irregular2):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")
