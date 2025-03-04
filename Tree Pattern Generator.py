
import math


total_stars=11
print(*[" "*(math.ceil((total_stars-i-1)/2))+"*"*(i)+""*int(i%2==0)+" "*(math.floor((total_stars-i-1)/2))+"\n" for i in range(1,total_stars+1) if i%2!=0])
print(math.ceil(3.5),math.floor(3.5))
