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

#def sepalLength():
     x = irisSetosa["Sepal Length"].values.tolist() #https://datatofish.com/convert-pandas-dataframe-to-list/
     y = irisVersicolor["Sepal Length"].values.tolist()
     z = irisVirginica["Sepal Length"].values.tolist()

     plt.hist([x, y, z], stacked = True, color = ["r", "g", "b"]) #https://showmecode.info/python/matplotlib/histogram/create-stacked-histogram/
     plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
     #plt.xticks([1, 2, 3, 4])
     plt.ylabel("Number of Iris")
     plt.xlabel("Sepal Length")
     plt.plot()
     #plt.show()
sepalLength()

def sepalWidth():
     a = irisSetosa["Sepal Width"].values.tolist() #https://datatofish.com/convert-pandas-dataframe-to-list/
     b = irisVersicolor["Sepal Width"].values.tolist()
     c = irisVirginica["Sepal Width"].values.tolist()

     plt.hist([a, b, c], stacked = True, color = ["r", "g", "b"]) #https://showmecode.info/python/matplotlib/histogram/create-stacked-histogram/
     plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
     #plt.xticks([1, 2, 3, 4])
     plt.ylabel("Number of Iris")
     plt.xlabel("Sepal Width")
     plt.plot()
     #plt.show()
sepalWidth()

plt.show()

#fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)







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








