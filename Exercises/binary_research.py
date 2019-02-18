
'''Binary Research of a number within an array'''

def binaryResearch(array, numeroBuscado):
    
    posIzquierda = 0
    posDerecha = len(array) - 1
    posCentral = int((posIzquierda + posDerecha) / 2)
    
    while posIzquierda <= posDerecha and array[posCentral] != numeroBuscado:
        
        if numeroBuscado > array[posCentral]:
            posIzquierda = posCentral + 1
        else:
            posDerecha = posCentral - 1
        posCentral = int((posIzquierda + posDerecha) / 2)
    if array[posCentral] == numeroBuscado:
        return posCentral
    else:
        return - 1


if __name__ == "__main__":
    
    # TEST CASES# 

    array1 = [1,2,3,4,5,6,7,8,9]
    assert binaryResearch(array1, 8) == 7

    array2 = [2,4,6,8,10,12,14,16,18,20]
    assert binaryResearch(array2, 6) == 2

    array3 = [43,56,12,11,8,97,100,67]
    assert binaryResearch(array3, 97) == 5

    array4 = [45,23,46,78,9,65]
    assert binaryResearch(array4, 5) == -1