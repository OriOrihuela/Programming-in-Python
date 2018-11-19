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

    print(greatest([4,23,1]))
    #>>>23


    print(greatest([4,23,1,50]))
    #>>>50


    print(greatest([67,99,1,5,200]))
    #>>>200


    print (greatest([1,2,3,6,0,8]))
    # >>>8


    print (greatest([]))
    #>>>0