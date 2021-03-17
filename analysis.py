# analysis.py
# Submission for the 20-21: 52167 -- Programming and Scripting Module
# Lecturer -- Andrew Beatty (andrew.beatty@gmit.ie)
# A program to investigate Fisher's iris data set and output the results to files. 
# Author: Andrew Walker (G00398788@gmit.ie)

# import libraries
import pandas as pd

# read the data from file, add column headings, and set number of rows to display
irisData = pd.read_csv('bezdekIris.data', header=None) 
irisData.columns = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Class']
pd.set_option('display.max_rows', 150)

# write the data to text file
with open('IrisData.txt', "wt") as f:
    f.write(str(irisData))
  





