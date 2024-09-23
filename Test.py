#!/usr/bin/env python
# coding: utf-8

# In[14]:


#BT KIEM_TRA_30P

def nhaplist(a,n):
    for i in range(n):
        print("Nhap vao phan tu thu", i+1, "=",end='')
        a.append(int(input()))
    print("list ban dau la", a)

def chen_x(a,x):
    a.insert(0,x)
    print("list ban dau sau khi chen x la: ", a)

def tach_so(a,x):
    for i in a:
        if i!=x:
            new_list.append(i)
    print(new_list)

def giam_dan(a):
    a.pop(0)
    for i in range(0, len(a)):
        if a[i]<0:
            for j in range(i+1, len(a)):
                if a[j]<0:
                    if a[i]<a[j]:
                        tg = a[i]
                        a[i] = a[j]
                        a[j] = tg
    print("list ban dau sap xep giam dan la: ", a)
    
    
n = int(input("Nhap n:"))
while(n<1 or n>30):
    n = int(input("Nhap lai n:"))
a = []
new_list = []
nhaplist(a,n)
x = int(input("Nhap x:"))
chen_x(a,x)
tach_so(a,x)
giam_dan(a)

