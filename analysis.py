# analysis.py
# Submission for the 20-21: 52167 -- Programming and Scripting Module
# Lecturer -- Andrew Beatty (andrew.beatty@gmit.ie)
# A program to investigate Fisher's iris data set and output the results to files. 
# Author: Andrew Walker (G00398788@gmit.ie)

# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read dataset and put into dataframe
irisData = pd.read_csv('bezdekIris.data', header = None)  
irisData.columns = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Class']
pd.set_option('display.max_rows', 150)

# save dataset to text file
with open('irisData.txt', "wt") as f:
     f.write(str(irisData))

# save statistical summary
summaryIrisData = irisData.describe()
with open('summaryIrisData.txt', "wt") as f:
     f.write(str(summaryIrisData))     

# assign each class of Iris to a variable
irisSetosa = irisData[:50]
irisVersicolor = irisData[50:100]
irisVirginica = irisData[100:150]

# create a function for the histograms
# within this function are five further functions for each variable which save each histogram to a .png file
def histograms():
     
     def sepalLength():
          x = irisSetosa["Sepal Length"]#https://datatofish.com/convert-pandas-dataframe-to-list/
          y = irisVersicolor["Sepal Length"]
          z = irisVirginica["Sepal Length"]

          plt.hist([x, y, z], stacked = True, color = ["r", "g", "b"]) #https://showmecode.info/python/matplotlib/histogram/create-stacked-histogram/
          plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
          plt.xlabel("Sepal Length")
          plt.ylabel("Frequency")
          plt.savefig("sepalLength.png")
          plt.show()
     
     def sepalWidth():
          x = irisSetosa["Sepal Width"]
          y = irisVersicolor["Sepal Width"]
          z = irisVirginica["Sepal Width"]
     
          plt.hist([x, y, z], stacked = True, color = ["r", "g", "b"]) 
          plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
          plt.xlabel("Sepal Width")
          plt.ylabel("Frequency")
          plt.savefig("sepalWidth.png")
          plt.show()

     def petalLength():
          x = irisSetosa["Petal Length"]
          y = irisVersicolor["Petal Length"]
          z = irisVirginica["Petal Length"]
     
          plt.hist([x, y, z], stacked = True, color = ["r", "g", "b"]) 
          plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
          plt.xlabel("Petal Length")
          plt.ylabel("Frequency")
          plt.savefig("petalLength.png")
          plt.show()

     def petalWidth():
          x = irisSetosa["Petal Width"]
          y = irisVersicolor["Petal Width"]
          z = irisVirginica["Petal Width"]
     
          plt.hist([x, y, z], stacked = True, color = ["r", "g", "b"]) 
          plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
          plt.xlabel("Petal Width")
          plt.ylabel("Frequency")
          plt.savefig("petalWidth.png")
          plt.show()

     def irisClass():
          x = irisSetosa["Class"]
          y = irisVersicolor["Class"]
          z = irisVirginica["Class"]
     
          plt.hist([x, y, z], stacked = True, color = ["r", "g", "b"]) 
          plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
          plt.xlabel("Class")
          plt.ylabel("Frequency")
          plt.savefig("irisClass.png")
          plt.show()

     irisClass()
     sepalLength()
     sepalWidth()
     petalLength()
     petalWidth()
     
histograms()
  





