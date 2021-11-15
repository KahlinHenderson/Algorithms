# Given an n x n matrix that represents an image rotate the image 90 degrees clockwise.
def rotate(matrix):
    for i in range(0, len(matrix)):
        for j in range(i, len(matrix[0])):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for i in range(0, len(matrix)):
        matrix[i] = reversed(matrix[i])
            
