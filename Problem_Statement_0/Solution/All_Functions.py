# This Document Has Been Written to explain the Logic Of the Functions Used In The Main Program
# The Main Programs had become too long to add this part

def sum_function(List): # Computes The List Of Elements(Numerical only) in a given List
    value=0
    for i in List:
        value+=i
    return value

def max_function(List): # Computes The Highest Value out of all elements in the List
    maximum=List[0]
    for i in List[1:]:
        if(i>maximum):
            maximum=i
    return maximum

def min_function(List): # Computes The Least value Out Of all elements in The List
    minimum=List[0]
    for i in List[1:]:
        if(i<minimum):
            minimum=i
    return minimum

def copy_function(List): # Creates A duplicate of The Given List
    List1=[]
    for i in List:
        List1.append(i)
    return List1

def SortDisplay(List): #Display in Sorted Order without list.sort()/sorted Function
    for i in range(len(List)-1):
        for j in range(len(List)-1-i):
            if(List[j]>List[j+1]):
                List[j],List[j+1]=List[j+1],List[j]
    print("\nContainers in Sorted Order:")
    for i in range(len(List)):
        print(f"{i+1}. {List[i]}")

def Listprint(List,n): #Prints The Required Statements
    for i in range(n):
        print(List[i])

def BarChart(List): #Helps to Represent Bar Graph
    print("\nContainer Weight Bar Chart:")
    for i in range(len(List)):
        print(f"Container {i+1} ({List[i]}) : ",end="")
        print("*"*int(List[i]/5))
    print("(Each * represents 5 Units)\n")

def Save(List): #Written so that contents are saved to file as needed
    save=input("\nDo you want to Save?:")
    if(save=="yes"):
        file_name=input("Enter The Name of to-be saved file:")
        with open(file_name,"w") as file:
            for i in List:
                file.write(str(i)+"\n")
        print(f"Report Saved to {file_name}")

def Search(List): #Searches For The Required Element, else returns "No Container"
    weight=int(input("Enter The Weight to be searched:"))
    for i in range(len(List)):
        if(weight==List[i]):
            print("Container Found!")
            print(f"Container {i+1} has weight {weight}")
            break
    else:
        print(f"No Container found with weight {weight}")

def KHeavy(List): #Retrieves kth Heaviest Element
    num=int(input("\nEnter 'k' for kth Heaviest Container:"))
    if(num>len(List)):
        print(f"Invalid input: Only {len(List)} containers exist.")
    elif(num>0):
        print(f"The {num}st Heaviest Container has weight: {List[-1*num]}")
    else:
        print("Invalid input: N must be at least 1.")

def Make_List(reqlist,Capacity):
    a="Heavy" if sum_function(reqlist)>=200 else "Light"
    b="Shipment Can be unloaded" if sum_function(reqlist)<=Capacity else "Shipment exceeds port capacity"
    List=[f"Total Shipment Weight: {sum_function(reqlist)}",
          f"Average Container Weight: {sum_function(reqlist)/len(reqlist)}",
          f"Heaviest Container: {max_function(reqlist)}",
          f"Lightest Container: {min_function(reqlist)}",
          f"Classification: {a}",
          f"Port Capacity: {Capacity}",
          f"Status: {b}"]
    return List

def Read(Capacity):
    check=1
    while(check!=0):
        file_name=input("\nEnter the Name Of The File to read:")
        try:
            with open(file_name,"r") as file:
                list1=file.readlines()
                list1[-1]+="\n"
            print(f"Loaded {len(list1[1:])} containers from {file_name}")
            for i in range(len(list1)):
                list1[i]=int(list1[i][:-1])
            print("Weights: ",end="")
            for i in list1[1:-1]:
                print(i,end=", ")
            print(list1[-1],"\n")
            list2=Make_List(list1[1:],Capacity)
            Listprint(list2,5)
            check=int(input("Enter 1 for more file-reading, else 0:"))
        except FileNotFoundError:
            print("No such File Exists.")
            bool1=bool(int(input("Enter 1 to read other file, else enter 0:")))
            if(bool1==0):
                break
            else:
                continue
            break
