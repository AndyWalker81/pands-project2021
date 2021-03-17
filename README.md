# pands-project2021
## Andrew Walker (G00398788@gmit.ie)

### README file for the 20-21: 52167 -- Programming and Scripting Module

#### Lecturer -- Andrew Beatty (andrew.beatty@gmit.ie)

##### Summary 

This file is the submission README file for the 2021 Project concerned with Fisher's *Iris* data set. This file contains an introduction to the project and the data set, scope, methodology, examples of interesting analsyes that others have pursued, code, references, and comments. 

The output from the project is a file called analysis.py that:
    - outputs a summary of each variable from the data set to a single text file,
    - saves a histogram of each variable to a png file,
    - outputs a scatter plot of each pair of variables.

##### Introduction 

Fisher's *Iris* data set is a multivariate data set first published by R A Fisher in his 1936 paper *The use of multiple measurements in taxonomic problems*<sup>[1]</sup>. The data set used is taken from the UCI Machine Learning Repository<sup>[2]</sup>. The data consists of three files:
    - iris.names
    - bezdekIris.data
    - iris.data
    
The former file is a description of the data set; the latter two files contain the data. The data is in Comma Separated Values (CSV) format. A CSV file is a plain text file that contains a list of data separated by commas. The first five lines of data are shown below:

(https://github.com/AndyWalker81/PANDS/blob/main/firstFiveRows.PNG "Iris Data")

The UCI repository notes that the iris.data file contains errors in two instances in which the data does not match with Fisher's original publication. These errors do not occur in the data contained within the bezdekIris.data file. Therefore, the bezdekIris.data file is used in this project. 

The data set contains of a total of 150 instances consisting of 50 samples from each of three species of Iris (*Iris setosa*, *Iris virginica* and *Iris versicolor*). The data set contains four numeric attributes measured in Fisher's study and one predictive attribute for each instance:
    - sepal length in centimetres (cm)
    - sepal width in centimetres (cm)
    - petal width in centimetres (cm)
    - class:
        - *Iris setosa*
        - *Iris virginica*
        - *Iris versicolor*

The analysis.py file developed for this project analyses the data set and outputs graphical representations of the data. 

##### Scope

The scope of is this project is...

#### Methodology

The methodology is...

#### Examples of interesting analyses

https://github.com/RitRa/Project2018-iris

### Analysis.py

#### Libraries Used

1. Pandas (imported as pd). 
```python
import pandas as pd
```
Pandas is is a high-level data manipulation tool built on the Numpy package. Its key data structure is called the DataFrame. DataFrames allow the storing and manipulation of tabular data in rows of observations and columns of variables<sup>[3</sup>.

#### Code
##### 1. Import Data

The first stage of the program is to import the data from the downloaded text files, arrange the data, and output to a text file:

```python
irisData = pd.read_csv('bezdekIris.data', header=None) 
irisData.columns = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Class']
pd.set_option('display.max_rows', 150)

with open('IrisData.txt', "wt") as f:
    f.write(str(irisData))
```

The code first uses Pandas to create a DataFrame by importing the bezdekIris.data file using pd.read_csv.

References: https://www.learnpython.org/en/Pandas_Basics