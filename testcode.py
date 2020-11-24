#runs test for binary numbers
import statistics
import math
def runsTest_notBinary(sample_list): 
    
    if(len(sample_list)==0):
        return
    runs, n1, n2 = 0, 0, 0
    median = statistics.median(sample_list)
    l=[]
    for i in sample_list:
        if(i <= median):
            l.append(0)
        else:
            l.append(1)
            
    
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
    print(runs_exp,stan_dev) 
    print('Runs-' , runs)
    print('Zeros-',  n1)
    print('Ones- ',n2)
    
    print(median)
    return runs,runs_exp,stan_dev 



#runs test for binary sequence
def runsTest(l): 
  

    if(len(l)==0):
        return

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