# pands-project2021
## Andrew Walker (G00398788@gmit.ie)

### README file for the 20-21: 52167 -- Programming and Scripting Module

#### Lecturer -- Andrew Beatty (andrew.beatty@gmit.ie)

## 1. Summary 

This file is the submission README file for the 2021 Project concerned with Fisher's *Iris* data set. This file contains an introduction to the project and the data set, scope, methodology, examples of interesting analsyes that others have pursued, code, references, and comments. 

The output from the project is a program called analysis.py that:

- outputs a summary of each variable from the data set to a single text file,
- saves a histogram of each variable to a png file,
- outputs a scatter plot of each pair of variables.

In addition, the program generates a text file showing the original data in a more easily-readable format.

## 2. Introduction to the Data Set

Fisher's *Iris* data set is a multivariate data set first published by R A Fisher in his 1936 paper *The use of multiple measurements in taxonomic problems*<sup>[1]</sup>. The data set contains of a total of 150 instances consisting of 50 samples from each of three species of Iris (*Iris setosa*, *Iris virginica* and *Iris versicolor*). The data set contains four numeric attributes measured in Fisher's study and one predictive attribute for each instance:

- sepal length in centimetres (cm)
- sepal width in centimetres (cm)
- petal width in centimetres (cm)
- class:

    - *Iris setosa*
    - *Iris virginica*
    - *Iris versicolor*

The analysis.py file developed for this project analyses the data set and outputs graphical representations of the data. 

##### References

1. Fisher, R. A., (1936) The use of multiple measurements in taxonomic problems, *Annals of Eugenics* [Online] Available at: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x (Accessed 20th March 2021)
2. UCI (n.d.) *Iris Data Set*, [Online] Available at: http://archive.ics.uci.edu/ml/datasets/Iris (Accessed 20th March 2021)

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

- A summary output of the data set.
    - Uncertainty as to what exactly was required. Therefore......1) summary of mean etc. 2) more easily readable table

- Five histograms showing the freqency that each of the following variables occured:
    - Class 
    - Sepal Length
    - Sepal Width
    - Petal Length
    - Petal Width

- Twelve scatter plots showing each numeric variable against each other numeric variable
    - Sepal Length against
        - Sepal Width
        - Petal Length 
        - Petal Width

    - Sepal Width against
        - Sepal Length
        - Petal Length
        - Petal Width

    - Petal Length against
        - Sepal Length
        - Sepal Width
        - Petal Width

    - Petal Width against
        - Sepal Length
        - Sepal Width
        - Petal Length

- A scatter matrix 
    - Whilst not specifically required as an output for the project, reviews of previous analyses show a scatter matrix to be a useful method of showing the visual data. A scatter matrix consists of several pair-wise scatter plots of variables presented in a matrix format, as shown in Figure 2:

 ![alt text](https://github.com/AndyWalker81/pands-project2021/blob/main/matrix.png "Scatter Matrix")

<sub>Figure 2</sub> 
   
Ref: https://www.originlab.com/doc/Tutorials/ScatterMatrix

### Programming the Code

Writing the program code is broken down into smaller stages, with the aim to complete an individual task before moving onto the next. At a high-level, the coding is broken down into the following three stages:

1. Import data set, save data set, output summary
2. Output histograms
3. Output scatter plots

Each stage is completed to a working level before moving to the next. However, writing the code is an iterative process whereby if it is considered that later improvements can be made to the working code, then the code is then amended or re-written. Examples of this might be if it is considered that the importing of a library might improve or make the code more efficient, or simply if it is considered that the output charts could be made more attractive if the code was re-written. It is recogised that this approach might involve the re-writing of the same pieces of code, but as a newcomer to Python it is considered that this approach would allow ongoing development and improvement to the program as knowledge grew. 


## 4. The Program Code

### Full Code

The full code is displayed below. A breakdown of each section of code is provided in the following sections




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

Pandas is is a high-level data manipulation tool built on the Numpy package. Its key data structure is called the DataFrame. DataFrames allow the storing and manipulation of tabular data in rows of observations and columns of variables<sup>[1]</sup>.

2. Matplotlib (pyplot)

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python<sup>[2]</sup>. ```matplotlib.pyplot``` is a collection of functions which make some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc<sup>[3]</sup>.

3. NumPy

NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices. <sup>[4]</sup>. 

4. Seaborn 

Seaborn is a Python data visualisation library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. <sup>[5]</sup>.

##### References

1. learnpython.org (n.d.) *Pandas Basics* [Online] Available at: https://www.learnpython.org/en/Pandas_Basics (Accessed 20th March 2021)
2. Matplotlib (2021) *Matplotlib: Visualization with Python* [Online] Available at: https://matplotlib.org/ (Accessed 20th March 2021)
3. Matplotlib (2021) *Pyplot tutorial* [Online] Available at: https://matplotlib.org/stable/tutorials/introductory/pyplot.html (Accessed 20th March 2021)
4. W3Schools (n.d.) *NumPy Introduction* [Online] Available at: https://www.w3schools.com/python/numpy_intro.asp (Accessed 20th March 2021)
5. Seaborn (2020) *seaborn: statistical data visualization* [Online] Available at: https://seaborn.pydata.org/ (Accessed 14th April 2021)

### 2. Import Data from Fisher's *Iris* data set

The first stage of the program is to import the data from the downloaded files and arrange the data:

```python
irisData = pd.read_csv('bezdekIris.data', header = None)  
irisData.columns = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Class']
pd.set_option('display.max_rows', 150)
```

1. The code first uses Pandas to create a DataFrame (irisData) by importing the bezdekIris.data file using ```pd.read_csv```. ```header = None``` is used otherwise pandas takes the first row as the header.
2. The five column headings are defined.
3. The number of rows to display (150) is defined. Without the ```python pd.set_option('display.max_rows', 150)``` code the results would be truncated showing only the first five and last five lines of data.

It is noted that the DataFrame will contain an Index running from 0 to 149.

References: 
https://www.learnpython.org/en/Pandas_Basics
https://community.insaid.co/hc/en-us/community/posts/360027461213-pd-read-csv-not-able-to-show-all-rows
https://stackoverflow.com/questions/32940709/missing-first-row-while-reading-from-file-python-pandas


#### 3. Save Data to .txt File

Next, the data is saved as irisData.txt. 

```python
with open('irisData.txt', "wt") as f:
     f.write(str(irisData))
```

This is in a more easily-readable format than the original downloaded data set (shown in Figure 2):

 ![alt text](https://github.com/AndyWalker81/PANDS/blob/main/irisData_txt.PNG "Iris Data")

<sub>Figure 3</sub> 

References: 

#### 4. Output a Summary of Each Variable

A summary of the statistical data is saved as summaryIrisData.txt. 

```python
summaryIrisData = irisData.describe()
with open('summaryIrisData.txt', "wt") as f:
     f.write(str(summaryIrisData))
```

 ![alt text](https://github.com/AndyWalker81/PANDS/blob/main/irisSummaryData_txt.PNG "Iris Summary Data")

<sub>Figure 4</sub> 


References: 
https://www.tutorialspoint.com/python_pandas/python_pandas_descriptive_statistics.htm

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

Within this function are five further functions; one for each variable of the data set. 

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
3. Using matplotlib, a stacked histogram is created using the three lists (x, y, z)
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

ref: https://datatofish.com/convert-pandas-dataframe-to-list/
ref: #https://showmecode.info/python/matplotlib/histogram/create-stacked-histogram/

#### 8. Create NumPy Arrays from the Data Set

```python
irisDataArray = irisData.to_numpy()
irisColumnsArray = ('Sepal Length', 'Sepal Width','Petal Length','Petal Width','Class')
```

Two NumPy arrays are created; one containing the complete data set (i.e. 150 rows and five columns), and one containing a single row with five columns headings. These arrays are used to create the scatter plots. 

ref: 

#### 9. Remove the Last Column of Data and Column Heading from the Arrays

```python
irisDataArrayNew = np.delete(irisDataArray, -1, axis = 1) 
irisColumnsArrayNew = np.delete(irisColumnsArray, -1) 
```

The last column is deleted from each of the two arrays created in the previous step. I.e. the Class column is removed. This is done because data from the Class column is not used in the scatter plots.

ref: https://note.nkmk.me/en/python-numpy-delete/

#### 10. Define a Function for the Scatter Plots:

```python
def scatters():
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
3. A while loop is set to run for one less times than the number of columns in the irisDataArryNew array (i.e. it will run three times).
4. The program then takes the first column of data from the first 50 rows (i.e. *Iris setosa*) of the original data set (i.e. Sepal Length because a = 0), and the first column of data from the the data set with the first column removed (i.e. Sepal Width because b = 0). A scatter plot is created and given title. 
5. The program then repeats Step 4 with the second 50 rows (i.e. *Iris versicolor*) of the original data set array.
6. The program then repeats Step 4 with the third 50 rows (i.e. *Iris virginica*) of the original data set array.
7. The plots are given x-axis label based upon the first column heading from original data set array (i.e. Sepal Length because a = 0) and y-axis label based upon the first column heading from data set array with column removed (i.e. Sepal Width because b = 0)
9. The value for b will increase by 1. 
10. While the value for b is lower than 3 then the loop will run another iteration.
11. Dependant on the value of b, the scatter plots will be saved given a different .png filename. 
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

Therefore, the setosaSepalLength() function creates three separate scatter plots, with the Sepal Length as the x-axis on each with and the other numeric variables as the y-axis on each.

Following the setosaSepalLength() function completing, the code then runs a function for the next numeric variable (i.e. Sepal Width). This is similar to the setosaSepalLength() function except that the value for a = 1. This means that the second column is deleted from the data set arrays (i.e. Sepal Width). This is so the program does not create a scatter plot calculating the same variable against itself. In addition, the outputted .png files are saved as individual filenames, differing from the previous function.

Following the completion of this function, two further functions are run with the value of a increasing by 1 each time and the .png files being given individual filenames.

This approach is taken as it results in a program that can automatically generate the scatter plots without the variables being explicitly named. Whilst this data set is relatively small with four numeric variables used, it is recognised that a larger data set might be used. This code would allow further columns of data to be added and would be able to generate further scatter plots with relative ease. 


ref: https://www.w3schools.com/python/python_conditions.asp





## 5. Examples of Outputs



## 6. Major iterations

Use of loops. This was a data set with unchangeable values. However, if a 'live' data set was being used it would be good to automate (e.g. if new data added).
Seaborn - change colours.

## 7. Learnings and Further Points


## 8. Conclusion

