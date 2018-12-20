

def insertionSort(array):
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
	

	# TEST CASES #

	
	assert insertionSort([13,76,54,34,23,67,89]) == [13,23,34,54,67,76,89]
	assert insertionSort([10,2,4,7,99]) == [2,4,7,10,99]
	assert insertionSort(['a', 'u', 'i', 'e', 'o']) == sorted(['a', 'u', 'i', 'e', 'o'])
	assert insertionSort(['spam', 'ham', 'elmo']) == sorted(['spam', 'ham', 'elmo'])
	assert insertionSort(['a', 'b', 'A', 'd', 'c', 'P']) == sorted(['a', 'b', 'A', 'd', 'c', 'P'])
	assert insertionSort([1.4, 5, 3, 3.5, 2, 4.1]) == sorted([1.4, 5, 3, 3.5, 2, 4.1])
