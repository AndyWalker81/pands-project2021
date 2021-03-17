# test
# Author: Andy Walker

import pandas as pd



#irisData = pd.read_csv('bezdekIris.data', header=None)  
irisData = pd.read_csv('bezdekIris.data', index = False)  
irisData.columns = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Class']
pd.set_option('display.max_rows', 150)
#pd.DataFrame.reset_index(drop = True, inplace = True)
#irisData.reset_index(drop = True, inplace = True)

# print (irisData['Class'])


with open('practiceIrisData.txt', "wt") as f:
     f.write(str(irisData))
   





