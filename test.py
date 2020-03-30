import random
import numpy as np
import matplotlib.pyplot as plt

class1=[]
class2=[]
class3=[]

xl = [[-2, 3]] 
yl = [[-(0.29*(-2)-1)/0.59, -(0.29*(3)-1)/0.59]]

for i in range(len(xl)):
    line1,=plt.plot([0.5, 0.5], [-15, 15], color='y')
   

class1 = [[1, 7],[2, 5],[2, 3],[1, 5],[3, 11],[1, 6],[3, 10],[3, 8],[2, 8],[2, 6]]
class2=[[-1, -5],[-1, 1],[0, 1],[0,-3],[-1, 2],[-2, -2],[-1, -3],[-2, -5],[-1, -4],[-2, -4]]
class3= [[3, -9],[2, -7],[2, -1],[1, -3],[3, -6],[1, -6],[3, -5],[2, -2],[3, -2],[2, 0]]
for n in class1:
    dot1, =plt.plot(n[0],n[1],'bx')
for n in class2:
    dot2, =plt.plot(n[0],n[1],'ro')
# for n in class3:
#     dot3, =plt.plot(n[0],n[1],'g*')

dot1.set_label('class 1')
dot2.set_label('class 2')
line1.set_label('hyperplane')
plt.xlabel('x1')
plt.ylabel('x2')
#dot3.set_label('class 3')
plt.legend(loc='upper left')
plt.title("The 1-against-2 classifier $x_1=0.5$")
plt.show()


w1=0.26
w2=0.44
w0=-1.5
xl = [-0, 4] 
yl = [(-w1*xl[0]-w0)/w2,(-w1*xl[1]-w0)/w2]

line1,=plt.plot(xl, yl, color='y')
for n in class1:
    dot1, =plt.plot(n[0],n[1],'bx')
for n in class3:
    dot3, =plt.plot(n[0],n[1],'g*')
dot1.set_label('class 1')
dot2.set_label('class 2')
line1.set_label('hyperplane')
plt.xlabel('x1')
plt.ylabel('x2')
dot3.set_label('class 3')
plt.legend(loc='upper left')
plt.title("The 1-against-3 classifier $x_2=-0.59x_1+3.4$")
plt.show()

w1=2
w2=0.54
w0=3
xl = [-2, 4] 
yl = [(w1*xl[0]-w0)/w2,(w1*xl[1]-w0)/w2]

line1,=plt.plot(xl, yl, color='y')
for n in class2:
    dot2, =plt.plot(n[0],n[1],'ro')
for n in class3:
    dot3, =plt.plot(n[0],n[1],'g*')
dot1.set_label('class 1')
dot2.set_label('class 2')
line1.set_label('hyperplane')
plt.xlabel('x1')
plt.ylabel('x2')
dot3.set_label('class 3')
plt.legend(loc='upper left')
plt.title("The 2-against-3 classifier $x_2=3.7x_1-5.6$")
plt.show()



for n in class1:
    dot1, =plt.plot(n[0],n[1],'bx')
for n in class2:
    dot2, =plt.plot(n[0],n[1],'ro')
for n in class3:
    dot3, =plt.plot(n[0],n[1],'g*')
line1,=plt.plot([0.5, 0.5], [-15, 20], color='deeppink')

w1=0.26
w2=0.44
w0=-1.5
xl = [-2.4, 4] 
yl = [(-w1*xl[0]-w0)/w2,(-w1*xl[1]-w0)/w2]

line2,=plt.plot(xl, yl, color='darkblue')
w1=2
w2=0.54
w0=3
xl = [-2.4, 4] 
yl = [(w1*xl[0]-w0)/w2,(w1*xl[1]-w0)/w2]

line3,=plt.plot(xl, yl, color='mistyrose')


font1 = {
'weight' : 'normal',
'size' : 8,
}
test,=plt.fill([0.5,0.5,2.17],[3.105,-3.75,2.418],facecolor='gray',alpha=0.5)
dot1.set_label('class 1')
dot2.set_label('class 2')
line1.set_label('SVM1:$x_1=0.5$')
line2.set_label('SVM2:$x_2=-0.59x_1+3.4$')
line3.set_label('SVM3:$x_2=3.7x_1-5.6$')
test.set_label('Region cannot be classified')

plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
dot3.set_label('class 3')
plt.legend(loc='upper left',prop=font1)
plt.title("The three SVMs")
plt.show()