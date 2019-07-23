import csv
import numpy as np
import matplotlib.pyplot as plt

listeL = []
listeDate = np.array([])
listeLight = np.array([])
listeError = np.array([])
with open('light-curve.csv', 'r', encoding='UTF-8', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        listeL.append([row])


for numligne in range(len(listeL)):
    listeDate = np.append(listeDate,float(listeL[numligne][0][0]))
for numligne in range(len(listeL)):
    listeLight = np.append(listeLight,float(listeL[numligne][0][1]))
for numligne in range(len(listeL)):
    listeError = np.append(listeError,float(listeL[numligne][0][2]))


x = np.array(np.array([np.array_split(listeDate, 13)]).mean(axis=1))
y = np.array(np.array([np.array_split(listeLight, 13)]).mean(axis=1))
z = np.array(np.array([np.array_split(listeError, 13)]).mean(axis=1))

x = x[0]
y = y[0]
z = z[0]

fig, ax = plt.subplots()

line1, = ax.plot(x, y)
line1.set_dashes([2, 2, 10, 2])

line2, = ax.plot(x, y-z)
line3, = ax.plot(x, y+z)

plt.show()