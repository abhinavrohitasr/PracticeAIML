import random

def Rand(start, end, num): 
    res = [] 
  
    for j in range(num): 
        res.append(random.randint(start, end)) 
  
    return res 

num = 100
start = 4000
end = 6000
val = Rand(start, end, num)
for item in val:
	print(item) 
