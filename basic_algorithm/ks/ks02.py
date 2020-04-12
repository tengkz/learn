w = [2,1,3,2]
v = [12,10,20,15]
size = len(w)
C = 5
memory = [[0 for i in range(C+1)] for j in range(size)]

def solveKS(index,capacity):
    if index<0 or capacity<=0:
        return 0
    if memory[index][capacity]!=0:
        return memory[index][capacity]
    res = solveKS(index-1,capacity)
    if w[index]<=capacity:
        res = max(res,v[index]+solveKS(index-1,capacity-w[index]))
    memory[index][capacity] = res
    return res

def knapSack():
    return solveKS(size-1,C)

print knapSack()
