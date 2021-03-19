# test
# Author: Andy Walker

import pandas as pd
#matplotlib and numpy
import matplotlib.pyplot as plt
import numpy as np


irisData = pd.read_csv('bezdekIris.data', header = None)  
irisData.columns = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Class']
pd.set_option('display.max_rows', 150)

with open('practiceIrisData.txt', "wt") as f:
     f.write(str(irisData))

irisSetosa = irisData[:50]
irisVersicolor = irisData[50:100]
irisVirginica = irisData[100:150]

def sepalLength():
     
#print (irisSetosa)
#print (irisVersicolor)
#print (irisVirginica)

#a = irisData["Class"]
#print (a)
     x = irisSetosa["Sepal Length"].values.tolist() #https://datatofish.com/convert-pandas-dataframe-to-list/
     y = irisVersicolor["Sepal Length"].values.tolist()
     z = irisVirginica["Sepal Length"].values.tolist()
#print (irisSetosaSepalLength)
#print (x, y, z)
#print (a)
#irisData.plot.hist(stacked = True, density = True, histtype = "bar", x = "Class", y = "Sepal Length", color = "r")
     plt.hist([x, y, z], stacked = True, color = ["r", "g", "b"]) #https://showmecode.info/python/matplotlib/histogram/create-stacked-histogram/
#irisData.plot.hist(x = "Sepal Length", y = "Class", stacked = True, color = ["r", "g", "b"])
     plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
#plt.xticks([1, 2, 3, 4])
     plt.ylabel("Number of Iris")
     plt.xlabel("Sepal Length")
     plt.plot()
     plt.show()
sepalLength()
#irisSetosa.plot.hist(stacked = True, density = True, histtype = "bar", x = "Class", y = "Sepal Length")
#irisVersicolor.plot.hist(stacked = True, density = True, histtype = "bar", x = "Class", y = "Sepal Length")
#irisVirginica.plot.hist(stacked = True, density = True, histtype = "bar", x = "Class", y = "Sepal Length")







# DO THE FOLLOWING AS FUNCTIONS
#https://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot   
# https://www.shanelynn.ie/bar-plots-in-python-using-pandas-dataframes/#styling-your-pandas-barcharts
# https://matplotlib.org/3.1.1/gallery/statistics/histogram_multihist.html
#colors = ["Red", "Green", "Blue"]
#plt.hist([irisSetosa["Class"],irisVersicolor,irisVirginica], stacked=True, density=True)
#irisData.plot.bar(stacked = True, density = True, histtype = "bar", x = "Class", y = "Sepal Length", color = colors)

#irisSetosa.plot.hist(stacked = True, density = True, histtype = "bar", x = "Class", y = "Sepal Length", color = colors)
#irisVersicolor.plot.hist(stacked = True, density = True, histtype = "bar", x = "Class", y = "Sepal Length", color = colors, bottom = irisVersicolor)
#irisVirginica.plot.hist(stacked = True, density = True, histtype = "bar", x = "Class", y = "Sepal Length", color = colors, bottom = irisVersicolor + irisVirginica)
#irisSetosa.plot.bar(x = "Class", y = "Sepal Length")
#irisVersicolor.plot.bar(x = "Class", y = "Sepal Length", bottom = irisVersicolor)
#irisVirginica.plot.bar(x = "Class", y = "Sepal Length", bottom = irisVersicolor + irisVirginica)








