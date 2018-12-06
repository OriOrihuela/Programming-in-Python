def Insertion(array):
	posInicial = 0
	aux = 0

	while posInicial < len(array):
		posMin = posInicial
		posActual = posInicial

		while posActual < len(array):

			if array[posActual] < array[posMin]:
				posMin = posActual

			posActual = posActual+1
		if posMin != posInicial:
			aux = array[posMin]
			array[posMin] = array [posInicial]
			array[posInicial] = aux

		posInicial += 1

	return array

if __name__ == '__main__':
	
	array1 = [9,4,8,1,10,15,32,19,7]

	assert Insertion(array1)

	array2 = [6,10,11,15,27,2,1,5,28]

	assert Insertion(array2)