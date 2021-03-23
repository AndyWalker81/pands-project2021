# pands-project2021
## Andrew Walker (G00398788@gmit.ie)

### README file for the 20-21: 52167 -- Programming and Scripting Module

#### Lecturer -- Andrew Beatty (andrew.beatty@gmit.ie)

### Summary 

This file is the submission README file for the 2021 Project concerned with Fisher's *Iris* data set. This file contains an introduction to the project and the data set, scope, methodology, examples of interesting analsyes that others have pursued, code, references, and comments. 

The output from the project is a file called analysis.py that:

- outputs a summary of each variable from the data set to a single text file,
- saves a histogram of each variable to a png file,
- outputs a scatter plot of each pair of variables.

### Introduction 

Fisher's *Iris* data set is a multivariate data set first published by R A Fisher in his 1936 paper *The use of multiple measurements in taxonomic problems*<sup>[1]</sup>. The data set used is taken from the UCI Machine Learning Repository<sup>[2]</sup>. The data consists of three files:

- iris.names
- bezdekIris.data
- iris.data
    
The former file is a description of the data set; the latter two files contain the data. The data is in Comma Separated Values (CSV) format. A CSV file is a plain text file that contains a list of data separated by commas. The first five lines of data are shown below as an example:

![alt text](https://github.com/AndyWalker81/PANDS/blob/main/firstFiveRows.PNG "Iris Data")

<sub>Figure 1</sub> 


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

##### References

1. Fisher, R. A., (1936) The use of multiple measurements in taxonomic problems, *Annals of Eugenics* [Online] Available at: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x (Accessed 20th March 2021)
2. UCI (n.d.) *Iris Data Set*, [Online] Available at: http://archive.ics.uci.edu/ml/datasets/Iris (Accessed 20th March 2021)

### Scope

The scope of is this project is...

## Methodology

The methodology is...
Iterative...will be developed as continue through the project...

## Examples of interesting analyses

https://github.com/RitRa/Project2018-iris
https://www.sisense.com/blog/data-visualizations-in-python-and-r/
https://github.com/vwalsh86/Iris-Data-Set-Project

## Analysis.py

The following sections detail the code used in the analysis.py program. 

### Code

#### 1. Import Libraries

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
```

1. Pandas 

Pandas is is a high-level data manipulation tool built on the Numpy package. Its key data structure is called the DataFrame. DataFrames allow the storing and manipulation of tabular data in rows of observations and columns of variables<sup>[1]</sup>.

2. Matplotlib (pyplot)

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python<sup>[2]</sup>. ```matplotlib.pyplot``` is a collection of functions which make some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc<sup>[3]</sup>.

3. NumPy

NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices.s<sup>[4]</sup>. 

##### References

1. learnpython.org (n.d.) *Pandas Basics* [Online] Available at: https://www.learnpython.org/en/Pandas_Basics (Accessed 20th March 2021)
2. Matplotlib (2021) *Matplotlib: Visualization with Python* [Online] Available at: https://matplotlib.org/ (Accessed 20th March 2021)
3. Matplotlib (2021) *Pyplot tutorial* [Online] Available at: https://matplotlib.org/stable/tutorials/introductory/pyplot.html (Accessed 20th March 2021)
4. W3Schools (n.d.) *NumPy Introduction* [Online] Available at: https://www.w3schools.com/python/numpy_intro.asp

#### 2. Import Data from Fisher's *Iris* data set

The first stage of the program is to import the data from the downloaded files and arrange the data:

```python
irisData = pd.read_csv('bezdekIris.data', header = None) 
irisData.columns = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Class']
pd.set_option('display.max_rows', 150)
```

1. The code first uses Pandas to create a DataFrame (irisData) by importing the bezdekIris.data file using pd.read_csv. ```header = None``` is used otherwise pandas takes the first row as the header.
2. The five column headings are defined.
3. The number of rows to display (150) is defined. Without the ```python pd.set_option('display.max_rows', 150)``` code the results would be truncated showing only the first five and last five lines of data.

It is noted that the DataFrame will contain an Index running from 0 to 149.

References: 
https://www.learnpython.org/en/Pandas_Basics
https://community.insaid.co/hc/en-us/community/posts/360027461213-pd-read-csv-not-able-to-show-all-rows
https://stackoverflow.com/questions/32940709/missing-first-row-while-reading-from-file-python-pandas


#### 2. Save Data to .txt File

Next, the data is saved as irisData.txt:

```python
with open('IrisData.txt', "wt") as f:
    f.write(str(irisData))
```

#### 3. Save Data to .txt File

A summary of the statistical data is saved as summaryIrisData.txt 

```python
summaryIrisData = irisData.describe()
with open('summaryIrisData.txt', "wt") as f:
     f.write(str(summaryIrisData))
```
References: 
https://www.tutorialspoint.com/python_pandas/python_pandas_descriptive_statistics.htm








## Learnings and Further Points

Use of loops. This was a data set with unchangeable values. However, if a 'live' data set was being used it would be good to automate (e.g. if new data added)