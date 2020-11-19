
# simple code to implement Runs  
# test of randomnes 
  
import random 
import math 
import statistics 
from scipy.stats import norm
import numpy as np
  
def runsTest(l): 
  
    runs, n1, n2 = 0, 0, 0
      
    # Checking for start of new run 
    if(l[0]==0):
        n1+=1
    else:
        n2+=1
    runs=1

    for i in range(1,len(l),1): 
          
        # no. of runs 
        if ((l[i] == 0 and l[i-1] ==1 ) or (l[i] == 1 and l[i-1] == 0)): 
            runs += 1  
          
        # no. of zero values 
        if l[i]==0: 
            n1 += 1   
        # no. of one values 
        else: 
            n2 += 1   
    
    runs_exp = ((2*n1*n2)/(n1+n2))+1
    stan_dev = math.sqrt(((2*n1*n2)*(2*n1*n2-n1-n2))/((n1+n2)**2 * (n1+n2-1))) 
    print('Runs-' , runs)
    print('Zeros-',  n1)
    print('Ones- ',n2)
    
    return runs,runs_exp,stan_dev 
    
# Making a list of 100 random numbers  
#W, L, L, L, W, L, L, W, L, L, W, L, L, W, L, W, L, L, L, L, W, L, W, L
#0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1
#l = [1,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,0,1,1,1,1]
#l=[0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1] 

l=np.random.randint(2,size=100)       

runs,mean,std = runsTest(l) 
print(runs,mean,std)
pvalue=2*min(1 - norm.cdf((runs-0.5-mean)/std),norm.cdf((runs+0.5-mean)/std))
#print('Z-statistic= ', Z)
print('pvalue = ', pvalue)


alpha=0.05
p_cap=1-alpha

samples=1000
diff = (p_cap*(1-p_cap))/samples

diff=3*math.sqrt(diff)

upper_limit=p_cap+diff

lower_limit=p_cap-diff


def getTest(samples):
    count=0
    for i in range(samples):
        l=np.random.randint(2,size=100)
        runs,mean,std=runsTest(l)
        pvalue=2*min(1 - norm.cdf((runs-0.5-mean)/std),norm.cdf((runs+0.5-mean)/std))
        if(pvalue>alpha):
            count+=1
    return count/samples

import matplotlib.pyplot as plt

#perform 20 tests
test_values=[]
for i in range(20):
    test_values.append(getTest(1000))



plt.axhline(y=upper_limit,color='r',linestyle='-')
plt.axhline(y=lower_limit,color='r',linestyle='-')
plt.plot(test_values,'g^')
plt.ylabel("Proportion Values")
plt.show()