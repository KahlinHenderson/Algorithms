# Given an array of integers and a target value find the disctinct integers in the
# array whose sum is equal to the target value and return their indices.
def findPair(A, Sum):
    dict = {}
    for i,e in enumerate(A):
        if Sum-e in dict:
            print("Pair found at", i, "and", dict[Sum-e])
            return
        dict[e] = i
    print("Pair not found")
    
