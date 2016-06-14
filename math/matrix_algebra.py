# Matrix Algebra

import numpy as np
import scipy as sci

A = sci.array([[1,2,3], [2,7,4]])
B = sci.array([[1,-1],[0,1]])
C = sci.array([[5,-1], [9,1], [6,0]])
D = sci.array([[3,-2,-1], [1,2,3]])
u = sci.matrix([6,2,-3,5])
v = sci.matrix([3,5,-1,4])
w = sci.matrix([1,8,0,5])



print("Ex 1.1:", A.shape)
print('\n')
print("Ex 1.2:", B.shape)
print('\n')
print("Ex 1.3:", C.shape)
print('\n')
print("Ex 1.4:", D.shape)
print('\n')
print("Ex 1.5:", u.shape)
print('\n')
print("Ex 1.6:", w.T.shape)
print('\n')

UplusV = u+v
print("Ex 2.1:", UplusV)
print('\n')
UminusV = u-v
print("Ex 2.2:", UminusV)
print('\n')
scaled6 = u*6
print("Ex 2.3:", scaled6)
print('\n')
u = sci.array([6,2,-3,5])
v = sci.array([3,5,-1,4])
UdotV = u.dot(v)
print("Ex 2.4:", UdotV)
print('\n')
normU = np.linalg.norm(u)
print("Ex 2.5:", normU)
print('\n')

print("Ex 3.1: not defined")
print('\n')
C_Tr = C.T
#print(C_Tr)
Ex3_2 = A - C_Tr
print("Ex 3.2:", '\n', Ex3_2)
print('\n')
D3 = []
for x in D:
    for i in x:
        D3.append(i*3)
D3 = np.reshape(D3, (2,3))
#print(D3)
Ex3_3 = C.T + D3
print("Ex 3.3:", '\n',Ex3_3)
print('\n')
Ex3_4 = B.dot(A)
print("Ex 3.4:", '\n',Ex3_4)
print('\n')
A_Trans = A.T
#print(A_Trans)
#Ex3_5 = B.dot(A_Trans)
#print("Ex 3.5", '\n',Ex3_5)
print("Ex 3.5: not defined")

