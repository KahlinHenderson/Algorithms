# Given an array of integers and a value find three disctinct integers whose sum is 
# equal to the given value and return them.
def find3Numbers(A, arr_size, sum):
    for i in range(0, arr_size - 1):
        s = Set()
        curr_sum = sum - A[i]
        for j in range(i + 1, arr_size):
            if curr_sum - A[j] in s:
                print(curr_sum - A[j], A[i], "and", A[j])
                return
            s.add(A[j])
    print("No triplet found")
        
        
        
        
