from All_Functions import sum_function,max_function,min_function

#The above calling takes in Functions from All_Functions, which is a Python File attached along with this file. In it, all user defined functions are present.
#I have tried to write user-defined functions for as many built-in functions as possible!

C=int(input("Enter The Maximum Capacity(in Kg):"))
N=int(input("Enter The Number of Containers:"))
Contlist=[]
for i in range(N):
    Contlist.append(int(input(f"Enter the Weight of {i+1}th Container:")))
Sumlist=sum_function(Contlist)
print(f"\nTotal Shipment Weight: {Sumlist}")
print(f"Average Container Weight: {Sumlist/N}")
print(f"Heaviest Container: {max_function(Contlist)}")
print(f"Lightest Container: {min_function(Contlist)}")
print("Classification: ","Heavy" if Sumlist>=200 else "Light")
print(f"Port Capacity: {C}")
print("Status: ","Shipment Can be unloaded" if Sumlist<=C else "Shipment exceeds Port Capacity!")
