
# coding: utf-8

# In[38]:

##Optimum Function


# In[39]:

import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
get_ipython().magic(u'matplotlib inline')


# Required libraries and packages are imported.

# In[40]:

x = np.arange(-120,80,0.1)


# Random x values were created.

# In[41]:

def f(x):
    return x**4 + 200*(x+2000)**2 + 10000


# Function is defined with x as input variable.

# In[42]:

def df(x):
    return 4*x**3 + 400*(x+2000)


# Derivative of the f(x) is defined.

# In[43]:

plt.plot(x,f(x))


# The plot was generated between input x variable and f(x).

# In[44]:

def optimum_function(x_old,x_new,gamma,precision):
    x_search = [x_new]
    x_iterations = [0] #number of iterations list is assigned zero before the loop
    n = 0 #variable initially set to zero
    while abs(x_new - x_old) > precision:
        x_old = x_new
        x_new = x_old - gamma*df(x_old)
        n = n+1 #Increase the count of the iteration steps
        x_search.append(x_new)
        z = len(x_search) #To get total number of iterations involved in the process
        x_iterations.append(n)
        
    print(z,"iterations")
    print("the local minimum occurs at %f" %x_new)
    print(gamma)
    x_iterations_graph = np.array(x_iterations)
    x_search_graph = np.array(x_search)
    y_search = f(x_search_graph) #decreasing trend of function
    plt.plot(x_iterations_graph,y_search) 
        


# In the above cell, the minimum point at which function has least value is calculated based on precision.
# Next, a plot is generated between the number of iterations and function with decreasing values [x_search--x_new]

# In[45]:

x_old = 70
x_new = 50
gamma = 0.000001
precision = 1e-12
optimum_value = optimum_function(x_old,x_new,gamma,precision)


# This fulfills the optimum_function assignment

# In[46]:

##Adaptive Optimum Function


# In[47]:

def adaptive_optimum(x_old, x_new, gamma, t, precision):
    nextIter = True #boolean condition
    while nextIter:
            gamma *=t #gamma value will be decremented with the value of 't' - decreasing rate of gamma
            x_old_try = x_old 
            x_new_try = x_new 
            count = 0 #variable is set to zero before loop
         
            try:
                while abs(x_new_try - x_old_try) > precision:
                    count = count + 1 #increment the variable
                    x_old_try = x_new_try
                    x_new_try = x_old_try - gamma * df(x_old_try)

                    if (count > 10000): #As per loop runs for 10000 iterations and stops if it is greater than 10000
                        break
        
                if (count <= 10000) and (abs(x_new_try - x_old_try) < precision): 
#If this condition is achieved stop the loop and come out of the loop to print optimum gamma and corresponding minimum x_new_try
                    nextIter = False        
                    break
            except:
                nextIter = True
    
    print("Found gamma:", gamma)
    print("The minimum is at:", x_new_try)
    print("The minimum value of f(x) is:", f(x_new_try))


# In[48]:

x_old = 70 
x_new = 50 

precision = 1e-12

t=0.9

gamma = 1

adaptive_optimum(x_old, x_new, gamma, t, precision)



# Thus, optimum gamma value is calculated by the program as well as corresponding minimum point and function value at this point was calculated. This fulfills the adaptive_optimum assignment.
