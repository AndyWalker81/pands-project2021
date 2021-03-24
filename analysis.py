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
  
# create functions for scatter plots

#https://ourcodingclub.github.io/tutorials/pandas-python-intro/
def scatters():
     setosaSepalLength = irisSetosa["Sepal Length"]
     setosaSepalWidth = irisSetosa["Sepal Width"]
     setosaPetalLength = irisSetosa["Petal Length"]
     setosaPetalWidth = irisSetosa["Petal Width"]

     versicolorSepalLength = irisVersicolor["Sepal Length"]
     versicolorSepalWidth = irisVersicolor["Sepal Width"]
     versicolorPetalLength = irisVersicolor["Petal Length"]
     versicolorPetalWidth = irisVersicolor["Petal Width"]

     virginicaSepalLength = irisVirginica["Sepal Length"]
     virginicaSepalWidth = irisVirginica["Sepal Width"]
     virginicaPetalLength = irisVirginica["Petal Length"]
     virginicaPetalWidth = irisVirginica["Petal Width"]
     
     def SL():
          def sepalLengthSepalWidth():
               plt.scatter(setosaSepalLength, setosaSepalWidth, c = "r")
               plt.scatter(versicolorSepalLength, versicolorSepalWidth, c = "g")
               plt.scatter(virginicaSepalLength, virginicaSepalWidth, c = "b")
               plt.show()

          sepalLengthSepalWidth()

          def sepalLengthPetalLength():
               plt.scatter(setosaSepalLength, setosaPetalLength, c = "r")
               plt.scatter(versicolorSepalLength, versicolorPetalLength, c = "g")
               plt.scatter(virginicaSepalLength, virginicaPetalLength, c = "b")
               plt.show()

          sepalLengthPetalLength()

          def sepalLengthPetalWidth():
               plt.scatter(setosaSepalLength, setosaPetalWidth, c = "r")
               plt.scatter(versicolorSepalLength, versicolorPetalWidth, c = "g")
               plt.scatter(virginicaSepalLength, virginicaPetalWidth, c = "b")
               plt.show()

          sepalLengthPetalWidth()

     SL()

     def SW():
     
          def sepalWidthSepalLength():

               plt.scatter(setosaSepalWidth, setosaSepalLength, c = "r")
               plt.scatter(versicolorSepalWidth, versicolorSepalLength, c = "g")
               plt.scatter(virginicaSepalWidth, virginicaSepalLength, c = "b")
               plt.show()

          sepalWidthSepalLength()

          def sepalWidthPetalLength():

               plt.scatter(setosaSepalWidth, setosaPetalLength, c = "r")
               plt.scatter(versicolorSepalWidth, versicolorPetalLength, c = "g")
               plt.scatter(virginicaSepalWidth, virginicaPetalLength, c = "b")
               plt.show()

          sepalWidthPetalLength()

          def sepalWidthPetalWidth():

               plt.scatter(setosaSepalWidth, setosaPetalWidth, c = "r")
               plt.scatter(versicolorSepalWidth, versicolorPetalWidth, c = "g")
               plt.scatter(virginicaSepalWidth, virginicaPetalWidth, c = "b")
               plt.show()

          sepalWidthPetalWidth()   

     SW()

     def PL():

          def petalLengthSepalLength():
               plt.scatter(setosaPetalLength, setosaSepalLength, c = "r")
               plt.scatter(versicolorPetalLength, versicolorSepalLength, c = "g")
               plt.scatter(virginicaPetalLength, virginicaSepalLength, c = "b")
               plt.show()

          petalLengthSepalLength()
               
          def petalLengthSepalWidth():
               plt.scatter(setosaPetalLength, setosaSepalWidth, c = "r")
               plt.scatter(versicolorPetalLength, versicolorSepalWidth, c = "g")
               plt.scatter(virginicaPetalLength, virginicaSepalWidth, c = "b")
               plt.show()

          petalLengthSepalWidth()

          def petalLengthPetalWidth():
               plt.scatter(setosaPetalLength, setosaPetalWidth, c = "r")
               plt.scatter(versicolorPetalLength, versicolorPetalWidth, c = "g")
               plt.scatter(virginicaPetalLength, virginicaPetalWidth, c = "b")
               plt.show()

          petalLengthPetalWidth()

     PL()

     def PW():

          def petalWidthSepalLength():
               plt.scatter(setosaPetalWidth, setosaSepalLength, c = "r")
               plt.scatter(versicolorPetalWidth, versicolorSepalLength, c = "g")
               plt.scatter(virginicaPetalWidth, virginicaSepalLength, c = "b")
               plt.show()
          
          petalWidthSepalLength()

          def petalWidthSepalWidth():
               plt.scatter(setosaPetalWidth, setosaSepalWidth, c = "r")
               plt.scatter(versicolorPetalWidth, versicolorSepalWidth, c = "g")
               plt.scatter(virginicaPetalWidth, virginicaSepalWidth, c = "b")
               plt.show()

          petalWidthSepalWidth()  

          def petalWidthPetalLength():
               plt.scatter(setosaPetalWidth, setosaPetalLength, c = "r")
               plt.scatter(versicolorPetalWidth, versicolorPetalLength, c = "g")
               plt.scatter(virginicaPetalWidth, virginicaPetalLength, c = "b")
               plt.show()

          petalWidthPetalLength()  
     
     PW()
          
scatters()




