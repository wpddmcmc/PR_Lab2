import random
import numpy as np
import matplotlib.pyplot as plt

test_data=[[1,-2.3],[1,-0.3],[1.67,3.7],[0.67,-0.3],[1.3,-0.3],
[0,-0.67],[1.67,0],[1.3,1.3],[1.3,0.67],[0.67,0.67]]


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
result1=[]
result2=[]
result3=[]

for test in test_data:
    print(test[0])
    if test[0]<0.5:
        result1.append(2)
    elif test[0]>0.5:
        result1.append(1)
for test in test_data:
    temp=test[1]-(-0.59*test[0]+3.4)
    if temp<0:
        result2.append(3)
    elif temp>0:
        result2.append(1)
for test in test_data:
    temp=test[1]-(3.7*test[0]-5.6)
    if temp<0:
        result3.append(3)
    elif temp>0:
        result3.append(2)

print('SVM1:',result1)
print('SVM2:',result2)
print('SVM3:',result3)
font1 = {
'weight' : 'normal',
'size' : 8,
}
test1,=plt.fill([0.5,0.5,2.17],[3.105,-3.75,2.418],facecolor='gray',alpha=0.5)
ex1, = plt.plot(1,-2.3,'ro')
ex2, = plt.plot(1,-0.3,'bo')
for test in test_data:
    point, = plt.plot(test[0],test[1],'g*')

ex1.set_label('Example $t_1$')
ex2.set_label('Example $t_2$')
line1.set_label('SVM1:$x_1=0.5$')
line2.set_label('SVM2:$x_2=-0.59x_1+3.4$')
line3.set_label('SVM3:$x_2=3.7x_1-5.6$')
test1.set_label('Region cannot be classified')
point.set_label('Test data')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.legend(loc='upper left',prop=font1)
plt.title("The Location of test data and SVMs")
plt.show()