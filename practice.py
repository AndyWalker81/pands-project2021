# test
# Author: Andy Walker

import pandas as pd



irisData = pd.read_csv('bezdekIris.data', header=None) #sep=",", 
irisData.columns = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Class']
pd.set_option('display.max_rows', 150)


with open('IrisData.txt', "wt") as f:
    f.write(str(irisData))
    #print (myvar)



#myvar = pd.DataFrame(irisData, columns=['IRISG'])   





