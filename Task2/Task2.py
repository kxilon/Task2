import sys
import math


with open(str(sys.argv[1]), 'r') as f1:
    file1 = f1.read().split("\n")

with open(str(sys.argv[2]), 'r') as f2:
    lines2 = f2.read().splitlines()


arr = []
for i in range (len(lines2)):
    arr.append(int(lines2[i].split(" ")[0]))
    arr.append(int(lines2[i].split(" ")[1]))


r = int(file1[1])
cx = int(file1[0].split(" ")[0])
cy = int(file1[0].split(" ")[1])

n = int(len(arr) / 2)

for i in range(n):
    x = arr[0] - cx
    arr.pop(0) 
    y = arr[0] - cy
    arr.pop(0)

    if r > math.sqrt((x * x + y * y)):
        print(1)
    elif r < math.sqrt((x * x + y * y)):
        print(2)
    else:
        print(0)
