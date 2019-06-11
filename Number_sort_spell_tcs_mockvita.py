#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:38:58 2019

@author: ashok
"""
def numtoword(n):
    t=str(n)
    l=len(t)
    if l==5:
        tens=10000
    elif l==4:
        tens=1000
    elif l==3:
        tens=100
    else:
        tens=10
    single_digits = ["zero", "one", "two", "three", 
    					"four", "five", "six", "seven", 
    					"eight", "nine"]; 
    if l==1:
        return(single_digits[n])
    	# The first string is not used, 
    	# it is to make array indexing simple 
    two_digits = ["", "ten", "eleven", "twelve", 
				"thirteen", "fourteen", "fifteen", 
				"sixteen", "seventeen", "eighteen", 
				"nineteen"]; 
    if n>=10 and n<=20:
        return(two_digits[(n%10)+1])
    	# The first two string are not used, 
    	# they are to make array indexing simple 
    tens_multiple = ["", "", "twenty", "thirty", "forty", 
    					"fifty", "sixty", "seventy", "eighty", 
    					"ninety"]; 
    
    tens_power = ["hundred", "thousand"];
    ans=""
    while(tens!=1):
        s=n%tens
        n=n//tens
        tens=tens//10
        if l==2:
            if s==0:
                ans=ans+tens_multiple[n]
                break
            ans=ans+tens_multiple[n]+" "+single_digits[s]
        if l==3:
            if s==0:
                ans=ans+single_digits[n]+" "+tens_power[0]
                break
            ans=ans+single_digits[n]+" "+tens_power[0]+" "
            l=l-1
            n=s
        if l==4:
            if s==0:
                ans=ans+single_digits[n]+" "+tens_power[1]
                break
            ans=ans+single_digits[n]+" "+tens_power[1]+" "
            l=l-1
            n=s
        if l==5:
            ans=ans+tens_multiple[n]+" "
            l=l-1
            n=s
    return(ans)
#n=int(input("enter number"))
#sol=numtoword(n)
#print(sol)
ar=list(map(int,input().split()))
#print(ar)
if ar[0]==ar[1]:
    #print("here am")
    print("1")
else:
    while(1):
        f=ar[0]
        s=[]
        ar.sort()
        #print(ar)
        if f==ar[0]:
            for i in ar:
                b=numtoword(i)
                s.append(b)
            #print(s)
            fin=s[0]
            s.sort()
            #print(s)
            if fin==s[0]:
                for j in range(len(ar)):
                    ar[j]=ar[j]*2
            else:
                print(sum(ar))
                break
        


























            
        
        