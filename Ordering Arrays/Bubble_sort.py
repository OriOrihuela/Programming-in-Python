


def bubbleSort(lista):
    recorrer_array = True
    pos = 0
    aux = 0
    while recorrer_array == True:
        recorrer_array = False
        while pos < len(lista) - 1:
            if lista[pos] > lista[pos + 1]:
                aux = lista[pos]
                lista[pos] = lista[pos + 1]
                lista[pos + 1] = aux

                recorrer_array = True
            pos += 1
        pos = 0
    return lista

if __name__ == "__main__":
    
    
    # TEST CASES # 

    
    assert bubbleSort([13,76,54,34,23,67,89]) == [13,23,34,54,67,76,89]
    assert bubbleSort([10,2,4,7,99]) == [2,4,7,10,99]
    assert bubbleSort(['a', 'u', 'i', 'e', 'o']) == sorted(['a', 'u', 'i', 'e', 'o'])
    assert bubbleSort(['spam', 'ham', 'elmo']) == sorted(['spam', 'ham', 'elmo'])
    assert bubbleSort(['a', 'b', 'A', 'd', 'c', 'P']) == sorted(['a', 'b', 'A', 'd', 'c', 'P'])
    assert bubbleSort([1.4, 5, 3, 3.5, 2, 4.1]) == sorted([1.4, 5, 3, 3.5, 2, 4.1])



    
