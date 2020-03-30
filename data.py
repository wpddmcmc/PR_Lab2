import random
import numpy as np
import matplotlib.pyplot as plt

class1=[]
class2=[]
class3=[]


yl = [[-15, 15], [(-15+6)/4*(-0.5)+3, (15+6)/4*(-0.5)+3]]
xl = [[(-15+6)/4, (15+6)/4], [(-15+6)/4, (15+6)/4]] 
for i in range(len(xl)):
    line1, = plt.plot(xl[i], yl[i], color='k')
    plt.plot([-0.1, 0.5], [-18, 18], color='k')
class1 = [[1, 7],[2, 5],[2, 3],[1, 5],[3, 11],[1, 6],[3, 10],[3, 8],[2, 8],[2, 6]]
class2=[[-1, -5],[-1, 1],[0, 1],[0,-3],[-1, 2],[-2, -2],[-1, -3],[-2, -5],[-1, -4],[-2, -4]]
class3= [[3, -9],[2, -7],[2, -1],[1, -3],[3, -6],[1, -6],[3, -5],[2, -2],[3, -2],[2, 0]]
for n in class1:
    dot1, =plt.plot(n[0],n[1],'bx')
for n in class2:
    dot2, =plt.plot(n[0],n[1],'ro')
for n in class3:
    dot3, =plt.plot(n[0],n[1],'g*')

dot1.set_label('class 1')
dot2.set_label('class 2')
dot3.set_label('class 3')
line1.set_label('example hyperplane')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend(loc='upper left')
plt.title("The linearly separable data")
# for n in range(500):
#     x=random.randint(-2,3)
#     y=random.randint(-10,10)
#     temp1=4*x-6
#     temp2=-0.5*x+3
#     if y>temp1 and y>temp2:
#         if [x,y] not in class1 and len(class1)<10:
#             class1.append([x,y])
#             plt.plot(x,y,'bx')
#     if y>temp1 and y<temp2 and len(class2)<10:
#         if [x,y] not in class3:
#             class2.append([x,y])
#             plt.plot(x,y,'ro')
#     if y<temp1 and y<temp2 and len(class3)<10:
#         if [x,y] not in class3:
#             class3.append([x,y])
#             plt.plot(x,y,'g*')
plt.show()
print("class1:",class1)
print("class2:",class2)
print("class3:",class3)

for n in class2:
    dot2, =plt.plot(n[0],n[1],'ro')
for n in class1:
    dot1, =plt.plot(n[0],n[1],'bx')
dot1.set_label('class 1')
dot2.set_label('class 2')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend(loc='upper left')
plt.title("Class1 and Class2")
plt.show()

for n in class1:
    dot1, =plt.plot(n[0],n[1],'bx')
for n in class3:
    dot3, =plt.plot(n[0],n[1],'g*')
dot1.set_label('class 1')
dot3.set_label('class 3')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend(loc='upper left')
plt.title("Class1 and Class3")
plt.show()

for n in class2:
    dot2, =plt.plot(n[0],n[1],'ro')
dot2.set_label('class 2')
for n in class3:
    dot3, =plt.plot(n[0],n[1],'g*')
dot3.set_label('class 3')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend(loc='upper left')
plt.title("Class2 and Class3")
plt.show()