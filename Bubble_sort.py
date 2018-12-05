
'''import matplotlib.pyplot as plt
from random import shuffle

def createRandomList(length):
    lista = [number for number in range(length)]
    # shuffle no devuelve nada: cambia la lista in place
    # porque las listas son objetos mutables
    shuffle(lista)
    assert len(lista) == length
    print(lista)'''

def bubblesort(lista):
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


    '''lista = createRandomList(15)'''

    
    assert bubblesort([13,76,54,34,23,67,89]) == [13,23,34,54,67,76,89]
    assert bubblesort([10,2,4,7,99]) == [2,4,7,10,99]



    
