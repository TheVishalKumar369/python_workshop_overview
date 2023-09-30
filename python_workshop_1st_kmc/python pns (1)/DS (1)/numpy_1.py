

import numpy as np

## dimesnsions should be same....for the addition and subtractiopjn between any rtwo arrays....

# a = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])

# b = np.array([
#     [2,4,3],
#     [5,3,2],
#     [4,5,6]
# ])

# c = np.array([1,2,3])

# new_c = np.array([[1,2,32,2],[1,2,3,4],[55,55,523,5],[5,656,454,5]])


# add = np.row_stack((a,c))
# ad = np.row_stack((c,a))
# add2 = np.column_stack((a,c))
# add3 = np.column_stack((c,a))

# print(add)
# print(add2)
# print(ad)
# print(add3)

# print(a+b)
# print(b[1,1])  # ---------> [1,1] where 1 represents the list index:1 in array and another 1 indicates the index of element in that array, similar to aij(i=1 and j =1) 9in matrix 

# print(a@b)
# print(matmul(a,b))
# print(a*b)


#list slicing
# l1 = [[1,2,32,3],[1,2,34,3],[45,5,235,54]]
# print(l1[1][1])  # --> [1],[1] 1 and 1 indicates the position of element in the array.....
# print(l1[1])


# new = np.array([[1,2,3],[3,3,3],[3,1,2]])

# new_reshape =new.reshape(3,1)
# # print(new)
# # print(new_reshape)
# print(new.T)






random_mat = np.random.randint(1,100,(25,32))
print(random_mat)

for element in random_mat:
    ele = np.random_mat(random_mat[element])
    if ele == 0:
        print("0 is found")
    else: 
        print(random_mat(random_mat[element])
    

# random_zero_mat = np.zeros((2,3,4))
# print(random_zero_mat)