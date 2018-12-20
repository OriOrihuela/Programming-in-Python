
def shellSort(arr): 
  
    # Start with a big gap, then reduce the gap 
    n = len(arr) 
    gap = n // 2
  
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0: 
  
        for i in range(gap,n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = arr[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and arr[j - gap] > temp: 
                arr[j] = arr[j - gap] 
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            arr[j] = temp 
        gap //= 2
    return arr

if __name__ == "__main__":
    

    # TEST CASES #

    assert shellSort([13,76,54,34,23,67,89]) == [13,23,34,54,67,76,89]
    assert shellSort([10,2,4,7,99]) == [2,4,7,10,99]
    assert shellSort(['a', 'u', 'i', 'e', 'o']) == sorted(['a', 'u', 'i', 'e', 'o'])
    assert shellSort(['spam', 'ham', 'elmo']) == sorted(['spam', 'ham', 'elmo'])
    assert shellSort(['a', 'b', 'A', 'd', 'c', 'P']) == sorted(['a', 'b', 'A', 'd', 'c', 'P'])
    assert shellSort([1.4, 5, 3, 3.5, 2, 4.1]) == sorted([1.4, 5, 3, 3.5, 2, 4.1])
