from es_cuadrada import esCuadrada
from numeros_en_rango import numerosEnRango
from numero_no_repetido_fila import numeroNoRepetidoFila
from numero_no_repetido_columnas import numeroNoRepetidoColumna

def checkSudoku(sudoku):
    if sudoku == esCuadrada and numerosEnRango and numeroNoRepetidoFila and numeroNoRepetidoColumna:
        return True
    else:
        return False

if __name__ == "__main__":

### CASOS TEST para comprobar si los números son únicos en la misma columna.


    correct = [[1,2,3],
               [2,3,1],
               [3,1,2]]


    if checkSudoku(correct):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect = [[1,2,3,4],
                 [2,3,1,3],
                 [3,1,2,3],
                 [4,4,4,2]]


    if checkSudoku(incorrect):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect2 = [[1,2,3,4],
                [2,3,1,2],
                [4,1,2,3],
                [2,3,1,4]]


    if checkSudoku(incorrect2):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect3 = [[1,2,3,4,5],
                [2,3,1,5,6],
                [4,5,2,1,3],
                [3,4,5,2,1],
                [5,6,4,3,2]]


    if checkSudoku(incorrect3):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect4 = [['a','b','c'],
                ['b','c','a'],
                ['c','a','b']]


    if checkSudoku(incorrect4):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    incorrect5 = [ [1, 1.5],
                [1.5, 1]]


    if checkSudoku(incorrect5):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")

        
    irregular = [[1,2,3],
                [2,3,1]]


    if checkSudoku(irregular):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")


    irregular2 = [[1,2,3],
                [2,3,1],
                [3,1]]


    if checkSudoku(irregular2):
        print("Este caso test es correcto")
    else :
        print("Este caso test es incorrecto")