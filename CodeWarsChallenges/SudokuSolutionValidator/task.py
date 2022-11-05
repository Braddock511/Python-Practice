import numpy as np
def valid_solution(board):
    matrix = np.array(board)
    number = 1
    number_2 = 3
    number_3 = 2
    number_4 = 2
    n=3
    m=3
    t=0
    w=0
    k=0
    kk=0
    array = []
    while number<10:
        matrixs = matrix[t:n,w:m]
        m+=3
        w+=3
        if w>6:
            w=0
            t+=3
        if m>9:
            m=3
            n+=3
        for y in matrixs:
            if number<number_2:
                for p in y:
                    array.append(p)
        for l in array:
            if array.count(l)!=1:
                return False
        array.clear()
        number_2+=1
        number+=1
    number = 1
    while number<10:
        row_matrix=matrix[k]
        k+=1
        
        for g in row_matrix:
            if number<number_3:
                array.append(g)
        for ll in array:
            if array.count(ll)!=1:
                return False
        array.clear()
        number_3+=1
        number+=1
    number = 1
    while number<10:
        column_matrix=matrix[0:,kk]
        kk+=1
        for gg in column_matrix:
            if number<number_4:
                array.append(gg)

        for lll in array:
            if array.count(lll)!=1:
                return False
        array.clear()
        number_4+=1
        number+=1
    return True

def test(fun, x):
    return fun == x

print(test(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                            [6, 7, 2, 1, 9, 5, 3, 4, 8],
                            [1, 9, 8, 3, 4, 2, 5, 6, 7],
                            [8, 5, 9, 7, 6, 1, 4, 2, 3],
                            [4, 2, 6, 8, 5, 3, 7, 9, 1],
                            [7, 1, 3, 9, 2, 4, 8, 5, 6],
                            [9, 6, 1, 5, 3, 7, 2, 8, 4],
                            [2, 8, 7, 4, 1, 9, 6, 3, 5],
                            [3, 4, 5, 2, 8, 6, 1, 7, 9]]), True))

print(test(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                            [6, 7, 2, 1, 9, 0, 3, 4, 9],
                            [1, 0, 0, 3, 4, 2, 5, 6, 0],
                            [8, 5, 9, 7, 6, 1, 0, 2, 0],
                            [4, 2, 6, 8, 5, 3, 7, 9, 1],
                            [7, 1, 3, 9, 2, 4, 8, 5, 6],
                            [9, 0, 1, 5, 3, 7, 2, 1, 4],
                            [2, 8, 7, 4, 1, 9, 6, 3, 5],
                            [3, 0, 0, 4, 8, 1, 1, 7, 9]]), False))

print(test(valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]), True))

print(test(valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]), False))

print(test(valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 0, 3, 7, 5]
                        ,[7, 0, 6, 3, 8, 0, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 0, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 0, 8, 4, 6]
                        ,[9, 8, 0, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 0, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 0, 6, 4, 2, 1, 3, 5]]), False))

print(test(valid_solution([[1, 2, 3, 4, 5, 6, 7, 8, 9]
                            ,[2, 3, 4, 5, 6, 7, 8, 9, 1]
                            ,[3, 4, 5, 6, 7, 8, 9, 1, 2]
                            ,[4, 5, 6, 7, 8, 9, 1, 2, 3]
                            ,[5, 6, 7, 8, 9, 1, 2, 3, 4]
                            ,[6, 7, 8, 9, 1, 2, 3, 4, 5]
                            ,[7, 8, 9, 1, 2, 3, 4, 5, 6]
                            ,[8, 9, 1, 2, 3, 4, 5, 6, 7]
                            ,[9, 1, 2, 3, 4, 5, 6, 7, 8]]), False))