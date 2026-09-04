def mapint_function(k):
    return int(k[0]),int(k[1])
def sum_alive(i,j,List):
    alive=0
    for k in range(i-1,i+2):
        for l in range(j-1,j+2):
            if(List[k][l]=="#"):
                alive+=1
    if(List[i][j]=="#"):
        return alive-1
    else:
        return alive
def Matrix_print(gen,List):
    print(f"Generation: {gen}   Population:{alive_count(List)}")
    for i in List[1:-1:]:
        print(i[1:-1:])
    print("\n"*32)
def Matrix_print_2(gen,List):
    print(f"Generation {gen}:")
    for i in List[1:-1:]:
        print(i[1:-1:])
def alive_count(List):
    alive=0
    for i in range(1,len(List[1:-1])+1):
        for j in range(1,len(List[0][1:-1:])+1):
            if(List[i][j]=="#"):
                alive+=1
    return alive
def Peak_count(List,P):
    if(alive_count(List)>P):
            P=alive_count(List)
    return P
def Matrix_form(List,P,G):
    Row=len(List[1:-1:])
    Column=len(List[0][1:-1:])
    for gen in range(G):
        temp=["."*(Column+2)]
        for i in range(1,Row+1):
            str1="."
            for j in range(1,Column+1):
                alive=sum_alive(i,j,List)
                if(List[i][j]=="."):
                    if(alive==3):
                        str1+="#"
                    else:
                        str1+="."
                if(List[i][j]=="#"):
                    if(alive<2 or alive>3):
                        str1+="."
                    elif(alive==2 or alive==3):
                        str1+="#"
            str1+="."
            temp.append(str1)
        temp.append("."*(Column+2))
        P=Peak_count(temp,P)
        Matrix_print(gen+1,temp)
        List=temp
    return List,P,alive_count(List)
from time import sleep
def Matrix_form_l3(List,P,G):
    Row=len(List[1:-1:])
    Column=len(List[0][1:-1:])
    print("\n")
    Matrix_print(0,List)
    for gen in range(G):
        temp=["."*(Column+2)]
        for i in range(1,Row+1):
            str1="."
            for j in range(1,Column+1):
                alive=sum_alive(i,j,List)
                if(List[i][j]=="."):
                    if(alive==3):
                        str1+="#"
                    else:
                        str1+="."
                if(List[i][j]=="#"):
                    if(alive<2 or alive>3):
                        str1+="."
                    elif(alive==2 or alive==3):
                        str1+="#"
            str1+="."
            temp.append(str1)
        temp.append("."*(Column+2))
        P=Peak_count(temp,P)
        Matrix_print(gen+1,temp)
        List=temp
        sleep(1)
    print("Simulation Complete!")
    return List,P,alive_count(List)
