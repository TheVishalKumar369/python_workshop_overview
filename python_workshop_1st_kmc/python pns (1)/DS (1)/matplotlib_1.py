# *************************MATPLOTLIB****************


import matplotlib.pyplot as plt

 a =[1,2,3,4,5]

a_array = num.array(a)
print(a_array)
print(type(a_array))

l1 = ["hello",1,2,3,[1,2,"morning",76]]
b_array = num.array(l1)
print(b_array)

# MATRIX FORM 

mat = [[1,2,3],[4,5,6,],[7,8,9]]
mat1 = num.array(mat)
print(mat1)  
print(mat1.shape)
print(mat1.size)

file = pd.read_csv('ds.csv')
students = file["name"]
marks = file["marks"]
# plt.scatter(students,marks)
# plt.bar(students,marks)
plt.pie(students,marks)
plt.show()

