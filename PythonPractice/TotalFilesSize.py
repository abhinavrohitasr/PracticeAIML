import os;
totalSize=0
for file in os.listdir('G:\\Python\\IDLE - Udemy'):
    if not os.path.isfile(os.path.join('G:\\Python\\IDLE - Udemy', file)):
        continue;
    totalSize = totalSize + os.path.getsize(os.path.join('G:\\Python\\IDLE - Udemy', file))
print (totalSize)
