import random

Arr = [random.randrange(1,11) for i in range(10)]
Sum = random.randrange(1,50)

## Iterative Approch 
def subset_sum(Arr, Sum):
    l = len(Arr)
    Map = [[False]*(Sum+1) for i  in  range(l)]
    for i in range(l):
        Map[i][0] = True
    for i in range(l):
        for j in range(1,Sum+1):
            if i == 0:
                if Arr[i] == j:
                    Map[i][j] = True
            else:
                Map[i][j] = Map[i-1][j]
                if not Map[i][j] and Arr[i] <= j:
                    Map[i][j] = Map[i-1][j-Arr[i]]
    x = l-1
    y = Sum
    if Map[x][y]:
        ans = list()
        while(x > 0 and y > 0):
            if Map[x-1][y]:
                x = x-1
            else:
                ans.append(Arr[x])
                y = y-Arr[x]
                x = x-1

            if x == 0:
                ans.append(Arr[x])
        return ans
    return False
    
print(subset_sum(Arr, Sum),Arr, Sum)
