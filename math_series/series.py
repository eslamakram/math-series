"""
fibonacci
Create a function called fibonacci. The function should have one parameter n. 
The function should return the nth value in the fibonacci series. 
You may implement the function using recursion 

initialize the first term to 0 and the second term to 1.
where each number in the sequence is always the sum of the two numbers before it.
f(0)=0 , f(1)=1 , f(n)= f(n-1)+f(n-2)

Input : n 
Output : fibonacci(n)

"""

def fibonacci(n):
    #Base case:
    if n in {0,1}:
        return n
    return fibonacci(n-1)+fibonacci(n-2) # Recursive case



""" 
lucas
 Create a function called lucas that returns the nth value in the lucas numbers Again, you will use recursion

 Input : n 
 Output : lucas(n)
 """
 
def lucas(n):
     #Base cases:
     if n == 0: return 2
     elif n == 1: return 1
     else:
          return lucas(n-1)+lucas(n-2)
          

"""
sum_series
Create a function called sum_series that required parameter and two optional parameters.
 The required parameter will determine which element in the series to print. 
 The two optional parameters will have default values of 0 and 1 and 
will determine the first two values for the series to be produced.
"""

def  sum_series(n,param1, param2):
    if param1 == 0 and param2 == 1: return fibonacci(n)
    elif param1 == 2 and param2 == 1 : return lucas(n)
    else:
        if n == 0: return param1
        elif n == 1: return param2
        else:
            return sum_series(n-1,param1,param2)+sum_series(n-2,param1,param2)