# pands-project2021
## Andrew Walker (G00398788@gmit.ie)

### README file for the 20-21: 52167 -- Programming and Scripting Module

#### Lecturer -- Andrew Beatty (andrew.beatty@gmit.ie)

## 1. Summary 

This file is the submission README file for the 2021 Project concerned with Fisher's *Iris* data set. This file contains an introduction to the project and the data set, scope, methodology, examples of interesting analsyes that others have pursued, code, references, and comments. 

The output from the project is a program called analysis.py that:

- outputs a summary of each variable from the data set to a single text file,
- outputs a text file showing the original data in a more easily-readable format than in the original file,
- saves a total of fives histogram - one for each variable - to a separate .png file and displays each histogram on the user's screen,
- saves a total of twelves scatterplots - one for each pair of numeric variables - to a separate .png file and displays each scatterplot on the user's screen,
- saves a pair plot showing a visual representation of the numeric variables and displays the pair plot on the user's screen.

## 2. Introduction to the Data Set

Fisher's *Iris* data set is a multivariate data set first published by R A Fisher in his 1936 paper *The use of multiple measurements in taxonomic problems*<sup>[1])</sup>. The data set contains of a total of 150 instances consisting of 50 samples from each of three species of Iris (*Iris setosa*, *Iris virginica* and *Iris versicolor*). The data set contains four numeric attributes measured in Fisher's study and one predictive attribute for each instance:

- sepal length in centimetres (cm)
- sepal width in centimetres (cm)
- petal width in centimetres (cm)
- class:

    - *Iris setosa*
    - *Iris virginica*
    - *Iris versicolor*

The analysis.py file developed for this project analyses the data set and outputs graphical representations of the data. 

## 3. Methodology

### Introduction
The project requires research in relation to the data set, downloading of the data set, and writing the program code, along with additional tasks such as referencing. The program itself is required to perform several different functions including outputting a summary of each variable, saving histograms of each variable, and outputting a scatter plot for each variable. Therefore, the project is broken down into several smaller stages, as detailed below. 

### Research and Examples of Previous Analyses 

1. https://github.com/RitRa/Project2018-iris
https://www.sisense.com/blog/data-visualizations-in-python-and-r/
https://github.com/vwalsh86/Iris-Data-Set-Project

### Downloading the Data Set

The data set used is taken from the UCI Machine Learning Repository<sup>[2]</sup>, as referenced in the instruction document for the project. The data consists of three files:

- iris.names
- bezdekIris.data
- iris.data
    
The former file is a description of the data set; the latter two files contain the data. The data is in Comma Separated Values (CSV) format. A CSV file is a plain text file that contains a list of data separated by commas. The first five lines of data are shown below as an example:

![alt text](https://github.com/AndyWalker81/PANDS/blob/main/firstFiveRows.PNG "Iris Data")

<sub>Figure 1</sub> 

The UCI repository notes that the iris.data file contains errors in two instances in which the data does not match with Fisher's original publication. These errors do not occur in the data contained within the bezdekIris.data file. Therefore, the bezdekIris.data file is used in this project. 

### Required Outputs

Based on the project task and research into how previous analyses were conducted, it was determined that the output would be:

- A summary output of the data set (summaryIrisData.txt).
    - Uncertainty as to what exactly was required. Therefore......1) summary of mean etc. 2) more easily readable table

- Five histograms showing the freqency that each of the following variables occured:
    - Class (irisClass.png)
    - Sepal Length (sepalLength.png)
    - Sepal Width (sepalWidth.png)
    - Petal Length (petalLength.png)
    - Petal Width (petalWidth.png)

- Twelve scatter plots showing each numeric variable against each other numeric variable
    - Sepal Length against
        - Sepal Width (scatter1.png)
        - Petal Length (scatter2.png)
        - Petal Width (scatter3.png)

    - Sepal Width against
        - Sepal Length (scatter4.png)
        - Petal Length (scatter5.png)
        - Petal Width (scatter6.png)

    - Petal Length against
        - Sepal Length (scatter7.png)
        - Sepal Width (scatter8.png)
        - Petal Width (scatter9.png)

    - Petal Width against
        - Sepal Length (scatter10.png)
        - Sepal Width (scatter11.png)
        - Petal Length (scatter12.png)

- A Pair Plot (matrix.png)
    - Reviews of previous analyses show a pair plot (or scatter matrix) to be a useful method of showing the visual data. A pair plot consists of several pair-wise scatter plots of variables presented in a matrix format, allowing for an instant visualisation of data<sup>[3]</sup>. The resultant pair plot from the program can be seen in Figure 6.

It is considered that there is some ambiguity as to what was expected to be 'saved' or 'outputed', based on the wording of the Project instructions. Therefore, it is decided to save both histograms and scatter plots to files, and to show both histograms and scatter plots on the user's screen. 
   
### Programming the Code

Writing the program code is broken down into smaller stages, with the aim to complete an individual task before moving onto the next. At a high-level, the coding is broken down into the following three stages:

1. Import data set, save data set, output summary
2. Output histograms
3. Output scatter plots

Each stage is completed to a working level before moving to the next. However, writing the code is an iterative process whereby if it is considered that later improvements can be made to the working code, then the code is then amended or re-written. Examples of this might be if it is considered that the importing of a library might improve or make the code more efficient, or simply if it is considered that the output charts could be made more attractive if the code was re-written. It is recogised that this approach might involve the re-writing of the same pieces of code, but as a newcomer to Python it is considered that this approach would allow ongoing development and improvement to the program as knowledge grew. 

## 4. The Program Code

### Full Code

The full code is displayed below (additional comments are included in the associated .py file). A breakdown of each section of code (along with links to references) is provided in the following sections.

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set_theme() 

irisData = pd.read_csv('bezdekIris.data', header = None)  
irisData.columns = ['Sepal Length (cm)','Sepal Width (cm)','Petal Length (cm)','Petal Width (cm)','Class']
pd.set_option('display.max_rows', 150)

with open('irisData.txt', "wt") as f:
     f.write(str(irisData))

summaryIrisData = irisData.describe()
with open('summaryIrisData.txt', "wt") as f:
     f.write(str(summaryIrisData))     

irisSetosa = irisData[:50]
irisVersicolor = irisData[50:100]
irisVirginica = irisData[100:150]

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

irisDataArray = irisData.to_numpy()
irisColumnsArray = ('Sepal Length (cm)', 'Sepal Width (cm)','Petal Length (cm)','Petal Width (cm)','Class')

irisDataArrayNew = np.delete(irisDataArray, -1, axis = 1) 
irisColumnsArrayNew = np.delete(irisColumnsArray, -1) 

def scatters():
    
    def setosaSepalLength():

        a = 0 
        b = 0

        irisDataArrayNewTwo = np.delete(irisDataArrayNew, a, axis = 1)
        irisColumnsArrayNewTwo = np.delete(irisColumnsArrayNew, a)  
                 
        while b < (len(irisColumnsArrayNew) - 1):  
            x = irisDataArray[0:50:,a] 
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
                plt.savefig("scatter1.png") 
            elif b == 1: 
                plt.savefig("scatter2.png")
            else: 
                plt.savefig("scatter3.png")
                
            plt.show()

            b = (b+1) 
          
    def setosaSepalWidth():
    
        a = 1 
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

sns.pairplot(irisData, hue = "Class", diag_kind="hist")  
plt.suptitle("Scatter Matrix for Fisher's Iris Data Set") 
plt.savefig("matrix.png")
plt.show()
```

### Breakdown of Code

The following sections detail the code used in the analysis.py program. 

### 1. Import Libraries

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set_theme() 
```

1. Pandas 

Pandas is is a high-level data manipulation tool built on the Numpy package. Its key data structure is called the DataFrame. DataFrames allow the storing and manipulation of tabular data in rows of observations and columns of variables<sup>[4]</sup>.

2. Matplotlib (pyplot)

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python<sup>[5]</sup>. ```matplotlib.pyplot``` is a collection of functions which make some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc<sup>[6]</sup>.

3. NumPy

NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices. <sup>[7]</sup>. 

4. Seaborn 

Seaborn is a Python data visualisation library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. <sup>[8]</sup>.

### 2. Import Data from Fisher's *Iris* data set

The first stage of the program is to import the data from the downloaded files and arrange the data:

```python
irisData = pd.read_csv('bezdekIris.data', header = None)  
irisData.columns = ['Sepal Length (cm)','Sepal Width (cm)','Petal Length (cm)','Petal Width (cm)','Class']
pd.set_option('display.max_rows', 150)
```

1. The code first uses Pandas to create a DataFrame (irisData) by importing the bezdekIris.data file using ```pd.read_csv```. ```header = None``` is used otherwise pandas takes the first row as the header<sup>[9, 10]</sup>.
2. The five column headings are defined.
3. The number of rows to display (150) is defined. Without the ```python pd.set_option('display.max_rows', 150)``` code the results would be truncated showing only the first five and last five lines of data<sup>[11]</sup>.

It is noted that the DataFrame will contain an Index running from 0 to 149.

#### 3. Save Data to .txt File

Next, the data is saved as irisData.txt<sup>[12]</sup>. 

```python
with open('irisData.txt', "wt") as f:
     f.write(str(irisData))
```

This is in a more easily-readable format than the original downloaded data set (shown in Figure 2):

 ![alt text](https://github.com/AndyWalker81/PANDS/blob/main/irisData_txt.PNG "Iris Data")

<sub>Figure 2</sub> 

#### 4. Output a Summary of Each Variable

A summary of the statistical data is saved as summaryIrisData.txt<sup>[13]</sup>. 

```python
summaryIrisData = irisData.describe()
with open('summaryIrisData.txt', "wt") as f:
     f.write(str(summaryIrisData))
```

 ![alt text](https://github.com/AndyWalker81/PANDS/blob/main/irisSummaryData_txt.PNG "Iris Summary Data")

<sub>Figure 3</sub> 

#### 5.Assign Each Class of Iris to a Variable  

The data sets consists of three class of *Iris*, each with 50 samples of data; a list is defined for each class.  

```python
irisSetosa = irisData[:50]
irisVersicolor = irisData[50:100]
irisVirginica = irisData[100:150]
```

Each variable contains a list of 50 rows of data related to a specific species of *Iris*. This is done to allow the histograms to be developed with a different species for each bar of the chart. 

#### 6. Create a Function for Histograms

```python
def histograms():
...
histograms()
```

Within this function are five further functions; one for each variable of the data set<sup>[14]</sup>. 

#### 7. Create a Function to Output Histograms for Each Variable of the Data Set

Five further functions are created within the histogram function:

1. irisClass()
2. sepalLength()
3. sepalWidth()
4. petalLength()
5. petalWidth()

Each function works in the same manner:

1. The column headings were previously defined in Step 1. 
2. A further three lists are defined from the lists created in Step 5. 
    - x, y, and z
    - The first function creates lists based on data in the Class column. 
    - The remaining four functions create lists based on data in the remaining four columns.
3. Using matplotlib, a stacked histogram is created using the three lists (x, y, z)<sup>[15]</sup>
4. The histogram is given a title, a legend, x and y labels.
5. The histogram is saved as a .png file and outputed to the user's screen.

The following code is for the Class column as an example:

```python
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
```

The resultant histogram from the above example is shown below:

 ![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/irisClass.png "Frequency of *Iris* Class")

<sub>Figure 4</sub> 

#### 8. Create NumPy Arrays from the Data Set

```python
irisDataArray = irisData.to_numpy()
irisColumnsArray = ('Sepal Length (cm)', 'Sepal Width (cm)','Petal Length (cm)','Petal Width (cm)','Class (cm)')
```

Two NumPy arrays are created from the DataFrame created in Step 2<sup>[16]</sup>; one containing the complete data set (i.e. 150 rows and five columns), and one containing a single row with five columns headings. These arrays are used to create the scatter plots. 


#### 9. Remove the Last Column of Data and Column Heading from the Arrays

```python
irisDataArrayNew = np.delete(irisDataArray, -1, axis = 1) 
irisColumnsArrayNew = np.delete(irisColumnsArray, -1) 
```

The last column is deleted from each of the two arrays created in the previous step<sup>[17]</sup>. I.e. the Class column is removed. This is done because data from the Class column is not used in the scatter plots.

#### 10. Define a Function for the Scatter Plots:

```python
def scatters():
...    
scatters()
```

Within this function are four further functions; one for each numerical variable of the data set.

#### 11. Create a Function to Output Scatter Plots for Each Numeric Variable of the Data Set

Four further functions are created within the scatters function:

1. setosaSepalLength()
2. setosaSepalWidth()
3. setosaPetalLength()
4. setosaPetalWidth()

The first function is defined as setosaSepalLength() and works as follows:

1. Two variables (a and b) are set, both as 0.
2. Using the a variable, the first column of data from the arrays is deleted (Sepal Length). This is so the program does not create a scatter plot calculating the same variable against itself.
3. A while loop is set to run for one less times than the number of columns in the irisDataArryNew array (i.e. it will run three times)<sup>[18]</sup>.
4. The program then takes the first column of data from the first 50 rows (i.e. *Iris setosa*) of the original data set (i.e. Sepal Length because a = 0), and the first column of data from the the data set with the first column removed (i.e. Sepal Width because b = 0). A scatter plot is created and given title. 
5. The program then repeats Step 4 with the second 50 rows (i.e. *Iris versicolor*) of the original data set array.
6. The program then repeats Step 4 with the third 50 rows (i.e. *Iris virginica*) of the original data set array.
7. The plots are given x-axis label based upon the first column heading from original data set array (i.e. Sepal Length because a = 0) and y-axis label based upon the first column heading from data set array with column removed (i.e. Sepal Width because b = 0)
9. The value for b will increase by 1. 
10. While the value for b is lower than 3 then the loop will run another iteration.
11. Using the if, elif, and else statements, dependant on the value of b, the scatter plots will be saved given a different .png filename<sup>[19]</sup>. 
12. The plots are also displayed on screen. 

```python
def setosaSepalLength():

        a = 0 
        b = 0

        irisDataArrayNewTwo = np.delete(irisDataArrayNew, a, axis = 1) 
        irisColumnsArrayNewTwo = np.delete(irisColumnsArrayNew, a)     
            
        while b < (len(irisColumnsArrayNew) - 1):  
            x = irisDataArray[0:50:,a] 
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
                plt.savefig("scatter1.png") 
            elif b == 1: 
                plt.savefig("scatter2.png")
            else: 
                plt.savefig("scatter3.png")
                
            plt.show()

            b = (b+1) 
```

Therefore, the setosaSepalLength() function creates three separate scatter plots, with the Sepal Length as the x-axis on each with and the other numeric variables as the y-axis on each. As the a variable was 0, the first column was not included in the data. This meant that Sepal Length was not plotted against Sepal Length.

Following the setosaSepalLength() function completing, the code then runs a function for the next numeric variable (i.e. Sepal Width). This is similar to the setosaSepalLength() function except that the value for a increases by 1 (i.e. a now equals 1). This means that the second column is deleted from the data set arrays (i.e. Sepal Width). This is so the program does not create a scatter plot calculating the same variable against itself. In addition, the outputted .png files are saved as individual filenames, differing from the previous function.

Following the completion of this function, two further functions are run with the value of a increasing by 1 each time and the .png files being given individual filenames. 

A resultant scatter plot from the above example is shown below:

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/scatter1.png "Distribution of Variables")

<sub>Figure 5</sub> 

This approach is taken as it results in a program that can automatically generate the scatter plots without the variables being explicitly named. A previous iteration of the code took a different approach and the variables were manually inputted into the code. For example:

```python
def sepalLengthSepalWidth():
               plt.scatter(setosaSepalLength, setosaSepalWidth)
               plt.scatter(versicolorSepalLength, versicolorSepalWidth)
               plt.scatter(virginicaSepalLength, virginicaSepalWidth)
               plt.show()
```

Whilst this approach does generate scatter plots with the correct data, each variable for each class of *Iris* must be typed out manually and cross-referenced to ensure that each variable is included against each other. This could lead to errors if a variable was accidently omitted or inputted incorrectly. Furthermore, whilst Fisher's *Iris* data set is relatively small with four numeric variables used, it is recognised that a larger data set might have been used. The code used in the final version of the program would allow further columns of data to be added and would be able to generate further scatter plots with relative ease with relative minor additions to the code. For example, if a new colummn was added and a new column heading was defined, a new function could simply be added with just the value of 'a' being increased by 1 and new filenames for the .png files being defined. However, using the example code from the earlier iteration would mean the manual entry and cross-referencing of variable names with a higher risk of error being made - the more variables used in the data set, the more difficult this would become. 

#### 12. Output a Pairplot 

The last section of code generates and saves a pairplot using Seaborn<sup>[20, 21, 22, 23]</sup>.

```python
sns.pairplot(irisData, hue = "Class", diag_kind="hist")  
plt.suptitle("Scatter Matrix for Fisher's Iris Data Set") 
plt.savefig("matrix.png")
plt.show()
```

The resultant pairplot is shown below:

 ![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/matrix.png "Pair Plot")

<sub>Figure 6</sub> 

## 5. Output Plots

The full compliment of five histograms, twelve scatter plots, and one pair plot are shown below:

### Histograms

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/irisClass.png "Frequency of Class")

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/sepalLength.png "Frequency of Sepal Length")

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/sepalWidth.png "Frequency of Sepal Width")

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/petalLength.png "Frequency of Petal Length")

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/petalWidth.png "Frequency of Petal Width")


### Scatter Plots

#### Sepal Length

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/scatter1.png "Distribution of Variables")

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/scatter2.png "Distribution of Variables")

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/scatter3.png "Distribution of Variables")

#### Sepal Width

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/scatter4.png "Distribution of Variables")

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/scatter5.png "Distribution of Variables")

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/scatter6.png "Distribution of Variables")

#### Petal Length

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/scatter7.png "Distribution of Variables")

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/scatter8.png "Distribution of Variables")

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/scatter9.png "Distribution of Variables")

#### Petal Width

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/scatter10.png "Distribution of Variables")

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/scatter11.png "Distribution of Variables")

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/scatter12.png "Distribution of Variables")

### Pair Plot

![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/matrix.png "Pair Plot")


## 6. Learnings and Further Points


## 7. Conclusion


## 7. References

1. Fisher, R. A., (1936) The use of multiple measurements in taxonomic problems, *Annals of Eugenics* [Online] Available at: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x (Accessed 20th March 2021)
2. UCI (n.d.) *Iris Data Set*, [Online] Available at: http://archive.ics.uci.edu/ml/datasets/Iris (Accessed 20th March 2021)
3. Towards Data Science (2018) *Visualizing Data with Pairs Plots in Python* [Online]. Available at: https://www.originlab.com/doc/Tutorials/ScatterMatrix (Accessed 20th April 2021)
4. learnpython.org (n.d.) *Pandas Basics* [Online] Available at: https://www.learnpython.org/en/Pandas_Basics (Accessed 20th March 2021)
5. Matplotlib (2021) *Matplotlib: Visualization with Python* [Online] Available at: https://matplotlib.org/ (Accessed 20th March 2021)
6. Matplotlib (2021) *Pyplot tutorial* [Online] Available at: https://matplotlib.org/stable/tutorials/introductory/pyplot.html (Accessed 20th March 2021)
7. W3Schools (n.d.) *NumPy Introduction* [Online] Available at: https://www.w3schools.com/python/numpy_intro.asp (Accessed 20th March 2021)
8. Seaborn (2020) *seaborn: statistical data visualization* [Online] Available at: https://seaborn.pydata.org/ (Accessed 14th April 2021)
9. Learn Python (n.d.) *Pandas Basics* [Online]. Available at: https://www.learnpython.org/en/Pandas_Basics (Accessed 20th March 2021)
10. Stack Overflow (n.d.) *Missing first row while reading from file - Python Pandas* [Online]. Available at: https://stackoverflow.com/questions/32940709/missing-first-row-while-reading-from-file-python-pandas (Accessed 20th April 2021)
11. International School of AI & Data Science *pd.read_csv not able to show all rows* [Online]. Available at: https://community.insaid.co/hc/en-us/community/posts/360027461213-pd-read-csv-not-able-to-show-all-rows (Accessed 20th April 2021)
12. W3Schools (n.d) *Python File Write* [Online]. Available at: https://www.w3schools.com/python/python_file_write.asp (Accessed 21st April 2021)
13. TutorialsPoint (2021) *Python Pandas - Descriptive Statistics* [Online]. Available at: https://www.tutorialspoint.com/python_pandas/python_pandas_descriptive_statistics.htm (Accessed 20th April 2021)
14. W3Schools (n.d) *Python Functions* [Online]. Available at: https://www.w3schools.com/python/python_functions.asp (Accessed 21st April 2021)
15. Show Me Code (n.d.) *Create a stacked histogram in Matplotlib* [Online]. Available at: https://showmecode.info/python/matplotlib/histogram/create-stacked-histogram/ (Accessed 21st April 2021)
16. Python Examples (n.d.) *Pandas DataFrame to NumPy Array* [Online]. Available at: https://pythonexamples.org/convert-pandas-dataframe-to-numpy-array/ (Accessed 21st April 2021)
17. note.nkmk.me (2017) *numpy.delete(): Delete rows and columns of ndarray* [Online]. Available at: https://note.nkmk.me/en/python-numpy-delete/ (Accessed 21st April 2021)
18. W3Schools (n.d.) *Python While Loops* [Online]. Available at: https://www.w3schools.com/python/python_while_loops.asp (Accessed 21st April 2021)
19. W3Schools (n.d.) *Python If ... Else* [Online]. Available at: https://www.w3schools.com/python/python_conditions.asp (Accessed 21st April 2021)
20. Seaborn (2020) *seaborn.pairplot* [Online]. Available at: https://seaborn.pydata.org/generated/seaborn.pairplot.html (Accessed 21st April 2021)
21. Python Tutorial (2021) *Seaborn pairplot example* [Online]. Available at: https://pythonbasics.org/seaborn-pairplot/ (Accessed 21st April 2021)
22. Seaborn (2020) *Overview of seaborn plotting functions* [Online]. Available at: https://seaborn.pydata.org/tutorial/function_overview.html (Accessed 21st April 2021)
23. Geeks for Geeks (n.d.) *Change Axis Labels, Set Title and Figure Size to Plots with Seaborn* [Online]. Available at: https://www.geeksforgeeks.org/change-axis-labels-set-title-and-figure-size-to-plots-with-seaborn/l (Accessed 21st April 2021)