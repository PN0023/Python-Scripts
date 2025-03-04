import math
import os
import datetime

def is_prime_lt1000(n,x=1):
    if n<2:
        return True
    elif x==n-1:
        return True
#    print(n,x,n%(x+1)!=0)
    return n%(x+1)!=0 and is_prime_lt1000(n,x+1)

def is_prime(n):
    return len([True for i in range(2,n) if n%i==0])==0
    
def largest_prime_no(n):
   if n<=3:
        return True
   for i in range(n,4,-1):
        #print(n,is_prime(n))
            if is_prime(i):
                print("largest prime found upto {}: {}".format(n,i))
                break    

print(is_prime(8))
largest_prime_no(8798797)

