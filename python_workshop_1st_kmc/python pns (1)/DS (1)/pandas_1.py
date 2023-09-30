# *******************************PANDAS***********************

import pandas as pd 
        
student_marks = pd.read_csv('ds.csv')

print(student_marks.to_string()) 
print(type(student_marks.to_string()))

# for i in enumerate(0,1)):
#     print(student_marks[i])

print(student_marks)
print(type(student_marks))

print(student_marks['name'])