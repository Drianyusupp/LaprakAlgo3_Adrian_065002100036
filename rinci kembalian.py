# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 09:36:02 2021

@author: User
"""

a = int(input("Masukkan total harga belanjaan Anda : "))
b = int(input("Masukkan jumlah uang Anda : "))
c = b-a

print("Kembalian Anda sejumlah : ",c)

print("Pecahan uang yang dibutuhkan :")
d = [100000, 50000, 20000, 10000, 5000, 1000, 500, 200, 100, 50]
for x in range (0,10):
    i=0
    while c >= d[x]:
        c = c - d[x]
        i = i + 1
        if(i>0):
            print("Uang kertas %d sebanyak %d lembar"%(d[x],i))
        
