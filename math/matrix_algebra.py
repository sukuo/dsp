import numpy as np
import scipy as sci

A = sci.array([[1,2,3], [2,7,4]])
B = sci.array([[1,-1],[0,1]])
C = sci.array([[5,-1], [9,1], [6,0]])
D = sci.array([[3,-2,-1], [1,2,3]])
u = sci.matrix([6,2,-3,5])
v = sci.matrix([3,5,-1,4])
w = sci.matrix([1,8,0,5]).T

print("Ex 1.1:", A.shape)
print("Ex 1.2:", B.shape)
print("Ex 1.3:", C.shape)
print("Ex 1.4:", D.shape)
print("Ex 1.5:", u.shape)
print("Ex 1.6:", w.shape)
print('\n')

UplusV = u+v
print("Ex 2.1:", UplusV)
UminusV = u-v
print("Ex 2.2:", UminusV)
scaled6 = u*6
print("Ex 2.3:", scaled6)
u = sci.array([6,2,-3,5])
v = sci.array([3,5,-1,4])
UdotV = u.dot(v)
print("Ex 2.4:", UdotV)
normU = np.linalg.norm(u)
print("Ex 2.5:", normU)
print('\n')

print("Ex 3.1: not defined")
C_Tr = C.T
#print(C_Tr)
Ex3_2 = A - C_Tr
print("Ex 3.2:", '\n', Ex3_2)
D3 = []
for x in D:
    for i in x:
        D3.append(i*3)
D3 = np.reshape(D3, (2,3))
#print(D3)
Ex3_3 = C.T + D3
print("Ex 3.3:", '\n',Ex3_3)
Ex3_4 = B.dot(A)
print("Ex 3.4:", '\n',Ex3_4)
print("Ex 3.5: not defined")
print("Ex 3.6: not defined")
Ex3_7 = C.dot(B)
print("Ex 3.7:", '\n',Ex3_7)
Ex3_8 = B**4
print("Ex 3.8:", '\n',Ex3_8)
Ex3_9 = A.dot(A.T)
print("Ex 3.9:", '\n',Ex3_9)
Ex3_10 = D.T.dot(D)
print("Ex 3.10:", '\n',Ex3_10)

#***Answers***

#Ex 1.1: (2, 3)
#Ex 1.2: (2, 2)
#Ex 1.3: (3, 2)
#Ex 1.4: (2, 3)
#Ex 1.5: (1, 4)
#Ex 1.6: (4, 1)


#Ex 2.1: [[ 9  7 -4  9]]
#Ex 2.2: [[ 3 -3 -2  1]]
#Ex 2.3: [[ 36  12 -18  30]]
#Ex 2.4: 51
#Ex 2.5: 8.60232526704


#Ex 3.1: not defined
#Ex 3.2: 
# [[-4 -7 -3]
# [ 3  6  4]]
#Ex 3.3: 
# [[14  3  3]
# [ 2  7  9]]
#Ex 3.4: 
# [[-1 -5 -1]
# [ 2  7  4]]
#Ex 3.5: not defined
#Ex 3.6: not defined
#Ex 3.7: 
# [[ 5 -6]
# [ 9 -8]
# [ 6 -6]]
#Ex 3.8: 
# [[1 1]
# [0 1]]
#Ex 3.9: 
# [[14 28]
# [28 69]]
#Ex 3.10: 
# [[10 -4  0]
# [-4  8  8]
# [ 0  8 10]]


