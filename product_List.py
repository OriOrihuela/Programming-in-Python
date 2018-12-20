# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(lista):
    resultado = 1
    indice = 0
    if len(lista) == 1:
        return lista[0] * 1
    
    if lista == []:
        return 1

    while indice < len(lista):
        resultado = resultado * lista[indice]
        indice += 1
    return resultado



if __name__ == "__main__":

    assert product_list([9]) == 9
    assert product_list([1,2,3,4]) == 24
    assert product_list([]) == 1
