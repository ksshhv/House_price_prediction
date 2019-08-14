import matplotlib.pyplot as plt
import csv
import numpy as np
x=[]
y=[]
with open('G:/ML/touse.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
      y.append(int(row[0]))
      x.append(int(row[1]))
x.sort()
y.sort()
q1=-400000
m=[]
n=[]
r=9999999999999999999999999999
#eqn of line
print("Analyzing your data...")
def k(i):
    q=q0*x[i]+q1
    return q
while(q1<100000):
    q0=0
    while(q0<500):
        j=0
        i=0
        # cost fn j
        while(i<len(x)):
            j+=(y[i]-k(i))*(y[i]-k(i))
            i+=1
        l=(j//len(x))
        if(l<r):
            r=l
            m.append(r)
            n.append([q0,q1])
        q0+=1
    q1+=10000
minj = m.index(min(m))
print("Data analyzed successfully !!!")
def predictedprice(x2):
    y2=n[minj][0]*x2+n[minj][1]
    return y2
print("Enter the total area of your house in sq. ft :",end=" ")
area=int(input())
print("Expected price is : "+str(predictedprice(area)))
print("Generating Graphical Representation")
# plotting points as a scatter plot 
plt.scatter(x, y, label= "stars", color= "green",  
            marker= "*", s=30) 
# x-axis label
plt.xlabel('Area in sq. ft', color='#1C2833')
# frequency label 
plt.ylabel('Price in $', color='#1C2833')
# plot title 
plt.title('My scatter plot with prediction line') 
x1 = np.linspace(500,5000,100)
y1 = n[minj][0]*x1+n[minj][1]
plt.plot(x1, y1, '-r', label='prediction')  
plt.grid()
plt.scatter(area, predictedprice(area), label= "your house", color= "blue",
            marker= "o", s=60)
#show legend
plt.legend()
plt.show()
