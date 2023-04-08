import numpy as np
import scipy.stats as stats
#import  as pnd

#Задача1

#cov = np.array
#zp = np.array([35, 45, 190, 200, 40,70,54, 150, 120,110])
#ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

#cov = np.mean(zp*ks) - np.mean(zp) * np.mean(ks)
#print (cov)
#9157.839999999997

#print (np.cov(zp, ks))
#array [[ 3882.93333333 10175.37777778]
#array[10175.37777778 33854.32222222]

#print (np.corrcoef(zp, ks))
#[[1.         0.88749009]
#[0.88749009 1.        ]]

#Задача2

data = (131, 125, 115, 122, 131, 115, 107, 99, 125, 111)

print (np.mean(data))
print(len(data)-1)
print(stats.sem(data))
stats.t.interval(confidence=0.05, df=len(data)-1, loc=np.mean(data), scale=stats.sem(data))
print(stats.t.interval)