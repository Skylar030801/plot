'''
import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()


import matplotlib.pyplot as plt
a=[1.3, 3.4, 2.3, 9.8]
b=[3.5, 4.9, 1.3, 2.2]
c=[9.7, 1.5, 4.3, 0.9, 11.2]
data1=[a,b,c]
plt.boxplot(data1)
plt.xlabel("Colleges")
plt.ylabel("Scores")
plt.title("Boxplot for colleges")
plt.show()



from matplotlib import pyplot as plt
students = ['BOYS', 'GIRLS']
data = [12,8]
fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = students)
plt.show()
'''

import matplotlib.pyplot as plt
from scipy import stats

plt.title("SOUP SALES IN RELATION TO TEMPERATURE")
plt.xlabel("TEMPERATURE (DEGREES CELCIUS)")

x = [14.2,16.5,11.8,15.3,18.8,22.5,19.5]
y = [220,330,190,340,410,445,415]
slope, intercept, r, p, std_err = stats.linregress(x,y)

def myfunc(a):
    return slope * a + intercept

mymodel = list(map(myfunc, x))
plt.scatter(x,y)
plt.plot(x, mymodel)
plt.show()

plt.scatter(x, y)
plt.show()


