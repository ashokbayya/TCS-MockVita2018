from itertools import permutations
import math
def permute(S,k):
    c=0
    perm=permutations(S)
    for i in perm:
        lis=list(i)
        for j in range(len(lis)-1):
            if j==0 and lis[j+1]==S[j+1]:
                c=c+1
                break
            elif S.index(lis[j])==len(lis)-1:
                break
            elif S[(S.index(lis[j]))+1]==lis[j+1]:
                c=c+1
                break
    return math.factorial(len(S))-c
inp=[]
T=int(input())
for b in range(T):
    N=int(input())
    inp.append(N)
for N in inp:
    li=[]
    for a in range(1,N+1,+1):
        if N%a==0:
            li.append(a)
    n=len(li)
    go=permute(li,n)
    print(go)