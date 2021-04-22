# analysis.py
# Submission for the 20-21: 52167 -- Programming and Scripting Module
# Lecturer -- Andrew Beatty (andrew.beatty@gmit.ie)
# A program to investigate Fisher's Iris data set and output the results to files. 
# Author: Andrew Walker (G00398788@gmit.ie)

# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set_theme() 

# read dataset and put into dataframe
irisData = pd.read_csv('bezdekIris.data', header = None)  
irisData.columns = ['Sepal Length (cm)','Sepal Width (cm)','Petal Length (cm)','Petal Width (cm)','Class']
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

     def irisClass():
         x = irisSetosa["Class"]
         y = irisVersicolor["Class"]
         z = irisVirginica["Class"]

         plt.hist([x, y, z], stacked = True) 
         plt.title("Frequency of Iris Class")
         plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
         plt.xlabel("Class")
         plt.ylabel("Frequency")
         plt.savefig("irisClass.png")
         plt.show()
     
     def sepalLength():
          x = irisSetosa["Sepal Length (cm)"]
          y = irisVersicolor["Sepal Length (cm)"]
          z = irisVirginica["Sepal Length (cm)"]

          plt.hist([x, y, z], stacked = True)
          plt.title("Frequency of Sepal Length")
          plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
          plt.xlabel("Sepal Length (cm)")
          plt.ylabel("Frequency")
          plt.savefig("sepalLength.png")
          plt.show()
     
     def sepalWidth():
          x = irisSetosa["Sepal Width (cm)"]
          y = irisVersicolor["Sepal Width (cm)"]
          z = irisVirginica["Sepal Width (cm)"]
     
          plt.hist([x, y, z], stacked = True) 
          plt.title("Frequency of Sepal Width")
          plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
          plt.xlabel("Sepal Width (cm)")
          plt.ylabel("Frequency")
          plt.savefig("sepalWidth.png")
          plt.show()

     def petalLength():
          x = irisSetosa["Petal Length (cm)"]
          y = irisVersicolor["Petal Length (cm)"]
          z = irisVirginica["Petal Length (cm)"]
     
          plt.hist([x, y, z], stacked = True) 
          plt.title("Frequency of Petal Length")
          plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
          plt.xlabel("Petal Length (cm)")
          plt.ylabel("Frequency")
          plt.savefig("petalLength.png")
          plt.show()

     def petalWidth():
          x = irisSetosa["Petal Width (cm)"]
          y = irisVersicolor["Petal Width (cm)"]
          z = irisVirginica["Petal Width (cm)"]
     
          plt.hist([x, y, z], stacked = True) 
          plt.title("Frequency of Petal Width")
          plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
          plt.xlabel("Petal Width (cm)")
          plt.ylabel("Frequency")
          plt.savefig("petalWidth.png")
          plt.show()

     irisClass()
     sepalLength()
     sepalWidth()
     petalLength()
     petalWidth()
     
histograms()

# create numpy arrays from dataset
irisDataArray = irisData.to_numpy()
irisColumnsArray = ('Sepal Length (cm)', 'Sepal Width (cm)','Petal Length (cm)','Petal Width (cm)','Class')

# remove last column of data and column heading (Class)
irisDataArrayNew = np.delete(irisDataArray, -1, axis = 1) # deletes last column of data (Class) 
irisColumnsArrayNew = np.delete(irisColumnsArray, -1) # deletes last column heading (Class)

def scatters():
    
    def setosaSepalLength():

        a = 0 
        b = 0

        irisDataArrayNewTwo = np.delete(irisDataArrayNew, a, axis = 1) # deletes first column of data (Sepal Length)
        irisColumnsArrayNewTwo = np.delete(irisColumnsArrayNew, a) # deletes first column heading (Sepal Length)    
        # this is so that the program does not calculate the same variable against itself    
        
        while b < (len(irisColumnsArrayNew) - 1):   # i.e. it runs three times
            x = irisDataArray[0:50:,a] # takes the first column of data from original data set (Sepal Length)
            y = irisDataArrayNewTwo[0:50,b] # takes first column of data from data set with Sepal Length data removed (i.e. Sepal Width)
            plt.title("Distribution of Variables")   
            plt.scatter(x,y)
                    
            x = irisDataArray[50:100,a]
            y = irisDataArrayNewTwo[50:100,b]
            plt.title("Distribution of Variables") 
            plt.scatter(x,y)

            x = irisDataArray[100:150,a]
            y = irisDataArrayNewTwo[100:150,b]
            plt.title("Distribution of Variables") 
            plt.scatter(x,y)
  
            plt.xlabel(irisColumnsArrayNew[a]) 
            plt.ylabel(irisColumnsArrayNewTwo[b]) 
            plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
            
            # save each plot as png
            if b == 0:
                plt.savefig("scatter1.png") 
            elif b == 1: 
                plt.savefig("scatter2.png")
            else: 
                plt.savefig("scatter3.png")
                
            plt.show()

            b = (b+1) # increases value of b by 1 each loop. The x-axis will stay the same for each Class of Iris but the y-axis will change each iteration 
          
    def setosaSepalWidth():
    
        a = 1 # this value increases by 1 in each function so that the next column and heading is deleted 
        b = 0
                
        irisDataArrayNewTwo = np.delete(irisDataArrayNew, a, axis = 1) 
        irisColumnsArrayNewTwo = np.delete(irisColumnsArrayNew, a) 

        while b < (len(irisColumnsArrayNew) - 1):
            x = irisDataArray[0:50,a]
            y = irisDataArrayNewTwo[0:50,b]
            plt.title("Distribution of Variables") 
            plt.scatter(x,y)
                    
            x = irisDataArray[50:100,a]
            y = irisDataArrayNewTwo[50:100,b]
            plt.title("Distribution of Variables") 
            plt.scatter(x,y)

            x = irisDataArray[100:150,a]
            y = irisDataArrayNewTwo[100:150,b]
            plt.title("Distribution of Variables") 
            plt.scatter(x,y)
            
            plt.xlabel(irisColumnsArrayNew[a])
            plt.ylabel(irisColumnsArrayNewTwo[b])      
            plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])  
            
            if b == 0:
                plt.savefig("scatter4.png")
            elif b == 1: 
                plt.savefig("scatter5.png")
            else: 
                plt.savefig("scatter6.png")            
            
            plt.show()

            b = (b+1)

    def setosaPetalLength():
    
        a = 2
        b = 0
                
        irisDataArrayNewTwo = np.delete(irisDataArrayNew, a, axis = 1)
        irisColumnsArrayNewTwo = np.delete(irisColumnsArrayNew, a) 

        while b < (len(irisColumnsArrayNew) - 1):
            x = irisDataArray[0:50,a]
            y = irisDataArrayNewTwo[0:50,b]
            plt.title("Distribution of Variables") 
            plt.scatter(x,y)
                    
            x = irisDataArray[50:100,a]
            y = irisDataArrayNewTwo[50:100,b]
            plt.title("Distribution of Variables") 
            plt.scatter(x,y)

            x = irisDataArray[100:150,a]
            y = irisDataArrayNewTwo[100:150,b]
            plt.title("Distribution of Variables") 
            plt.scatter(x,y)

            plt.xlabel(irisColumnsArrayNew[a])
            plt.ylabel(irisColumnsArrayNewTwo[b])   
            plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])     
            
            if b == 0:
                plt.savefig("scatter7.png")
            elif b == 1: 
                plt.savefig("scatter8.png")
            else: 
                plt.savefig("scatter9.png")
                      
            plt.show()

            b = (b+1)

    def setosaPetalWidth():
    
        a = 3
        b = 0
                
        irisDataArrayNewTwo = np.delete(irisDataArrayNew, a, axis = 1)
        irisColumnsArrayNewTwo = np.delete(irisColumnsArrayNew, a) 

        while b < (len(irisColumnsArrayNew) - 1):
            x = irisDataArray[0:50,a]
            y = irisDataArrayNewTwo[0:50,b]
            plt.title("Distribution of Variables") 
            plt.scatter(x,y)
                    
            x = irisDataArray[50:100,a]
            y = irisDataArrayNewTwo[50:100,b]
            plt.title("Distribution of Variables") 
            plt.scatter(x,y)

            x = irisDataArray[100:150,a]
            y = irisDataArrayNewTwo[100:150,b]
            plt.title("Distribution of Variables") 
            plt.scatter(x,y)

            plt.xlabel(irisColumnsArrayNew[a])
            plt.ylabel(irisColumnsArrayNewTwo[b])  
            plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])     

            if b == 0:
                plt.savefig("scatter10.png")
            elif b == 1: 
                plt.savefig("scatter11.png")
            else: 
                plt.savefig("scatter12.png")            
                      
            plt.show()

            b = (b+1)

    setosaSepalLength()
    setosaSepalWidth()
    setosaPetalLength()
    setosaPetalWidth()

scatters()

# Output a pairplot

sns.pairplot(irisData, hue = "Class", diag_kind="hist")  
plt.suptitle("Scatter Matrix for Fisher's Iris Data Set") 
plt.savefig("matrix.png")
plt.show()

