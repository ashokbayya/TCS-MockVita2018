# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

s=input("STRING")
s1=s
ANS=''
st=list(s)
q=int(input("q"))
arr=list(input().split())
print(s,q,arr)
for i in range(0,len(arr)-1,+2):
    if arr[i]=='L':
        s=st[int(arr[i+1])::]
        re=st[0:int(arr[i+1])]
        s=s+re
        print(s)
        st=s
        o=st[0]
    elif arr[i]=='R':
        s=st[:len(st)-int(arr[i+1])]
        re=st[-int(arr[i+1])::]
        s=re+s
        print(s)
        st=s
        o=st[0]
    ANS=ANS+o
print(ANS)
if(s1.__contains__(ANS)):
    print("Yes")
else:
    print("No")
    
        