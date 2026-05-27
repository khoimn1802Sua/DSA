def linear_search_matrix(M, x):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == x:
                return (i, j)
    return (-1, -1)