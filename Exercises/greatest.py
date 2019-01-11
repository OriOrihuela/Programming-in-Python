# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(lista):
    if lista == []:
        return 0
    else:
        return max(lista)


if __name__ == "__main__":

    assert greatest([4,23,1]) == 23
    assert greatest([4,23,1,50]) == 50
    assert greatest([67,99,1,5,200]) == 200
    assert greatest([1,2,3,6,0,8]) == 8
    assert greatest([]) == 0
