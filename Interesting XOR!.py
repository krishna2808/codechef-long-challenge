import math     
for _ in range(int(input())):
    n,Sum, k    = int(input()),0, 1  
    while(n>= Sum ):
        Sum = int(math.pow(2,k))
        k += 1 
        
    j =  int(math.pow(2,k-2)) 
    v1 = Sum - n 
    print((j-1)*((j-1)+v1))
   
