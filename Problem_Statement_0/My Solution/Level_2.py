from All_Functions import Read,Make_List,sum_function,copy_function,SortDisplay,Listprint,BarChart,Save,Search,KHeavy

#The above calling takes in Functions from All_Functions, which is a Python File attached along with this file. In it, all user defined functions are present.
#I have tried to write user-defined functions for as many built-in functions as possible!

Capacity=int(input("Enter The Maximum Capacity: "))
times=1
    
while(1!=0):#Used this Condition for Multi-Ship Processing
    print(f"Status of Ship No.{times}:")
    Contlist=[int(input(f"Enter The Weight Value of {i+1}th Container:")) for i in range(int(input("Enter Number Of Containers:")))]
    
    List=copy_function(Contlist)
    SortDisplay(List)
    
    Cont=Make_List(Contlist,Capacity)
    print("\n")
    Listprint(Cont,len(Cont))
    
    BarChart(Contlist)
    Search(Contlist)
    KHeavy(List)
    Save(Cont)
    Read(Capacity)
    
    cont=input("\nContinue Entering Other Ships' Data?:")
    if(cont=="yes"):
        times+=1
        continue
    else:
        break
    
print(f"\nTotal Ships Processed:{times}") #Output of Number Of Ships
    
    
