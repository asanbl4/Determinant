def determinant(matrix_size, matrix):
    ans = 1
    for i in range(matrix_size):
        # If the diagonal_element = 0, seek for the next non-zero element at the same position
        if not matrix[i][i]:
            for j in range(i + 1, matrix_size):
                if matrix[j][i] != 0:
                    # If such element is found then swap those rows
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
                if j == matrix_size - 1:
                    return 0

        # Row operations
        for j in range(i + 1, matrix_size):
            if matrix[j][i]:
                fraction = -matrix[j][i] / matrix[i][i]
                # Multiply the main row by the fraction and add the secondary one
                matrix[j] = [fraction * matrix[i][k] + matrix[j][k] for k in range(len(matrix[j]))]

        ans *= matrix[i][i]

    # # Echelon form matrix
    # for i in matrix:
    #     print(i)

    return round(ans, 4)


if __name__ == '__main__':
    """Test:
    matrix_size = 4
    test = ([[4, 2, 1, 0], [-2, 3, 7, 12], [9, 8, 4, 1], [12, 3, 4, 5]])
    """
    matrix_size = int(input('Enter the size of a matrix: '))
    test = []
    print('Enter the matrix')
    for _ in range(matrix_size):
        test.append([float(i) for i in input().split()])
    print(f'∆ = {determinant(matrix_size, test)}')
