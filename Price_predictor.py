import matplotlib.pyplot as plt
import csv
import numpy as np

x = []
y = []

with open('G:/ML/touse.csv', 'rt') as f:
    data = csv.reader(f)
    for row in data:
        y.append(int(row[0]))
        x.append(int(row[1]))

x.sort()
y.sort()

best_cost = float('inf')
best_q0 = 0
best_q1 = 0

print("Analyzing your data...")

def k(i, q0, q1):
    return q0 * x[i] + q1

q1 = -400000
while q1 < 100000:
    q0 = 0
    while q0 < 500:
        total_cost = 0
        for i in range(len(x)):
            prediction = k(i, q0, q1)
            error = y[i] - prediction
            total_cost += error * error
        avg_cost = total_cost // len(x)
        if avg_cost < best_cost:
            best_cost = avg_cost
            best_q0 = q0
            best_q1 = q1
        q0 += 1
    q1 += 10000

print("Data analyzed successfully !!!")

def predictedprice(x2):
    return best_q0 * x2 + best_q1

print("Enter the total area of your house in sq. ft :", end=" ")
area = int(input())
print("Expected price is : " + str(predictedprice(area)))
print("Generating Graphical Representation")

# Plotting points as a scatter plot
plt.scatter(x, y, label="Actual Data", color="green", marker="*", s=30)
plt.xlabel('Area in sq. ft', color='#1C2833')
plt.ylabel('Price in $', color='#1C2833')
plt.title('My scatter plot with prediction line')

# Line of best fit
x1 = np.linspace(500, 5000, 100)
y1 = best_q0 * x1 + best_q1
plt.plot(x1, y1, '-r', label='Prediction')

plt.grid()
plt.scatter(area, predictedprice(area), label="Your House", color="blue", marker="o", s=60)
plt.legend()
plt.show()
