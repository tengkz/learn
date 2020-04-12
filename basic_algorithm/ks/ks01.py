w = [2,1,3,2]
v = [12,10,20,15]

def solveKS(index,capacity):
    if index<0 or capacity<=0:
        return 0
    res = solveKS(index-1,capacity)
    if w[index]<=capacity:
        res = max(res,v[index]+solveKS(index-1,capacity-w[index]))
    return res


def KnapSack(C):
    size = len(w)
    return solveKS(size-1,C)

print KnapSack(5)
