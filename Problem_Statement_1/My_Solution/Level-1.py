#Welcome To Conway's Game Of Life:
#All the Functions are in the File Mentioned!
from My_Functions import mapint_function,Matrix_print,alive_count,Matrix_form
while True:
    R,C=mapint_function(input("Enter The Number Of Rows and Columns:").split())
    G=int(input("Enter the Number Of Generations:"))
    print("Enter . for Dead, # for Alive:")
    Game_List=["."*(C+2)]
    for i in range(R):
        lines="."+input(f"Enter the {C} characters of The {i+1}th line:")+"."
        Game_List.append(lines)
    Game_List.append("."*(C+2))

    a0=alive_count(Game_List)
    Peak=a0
    Matrix_print(0,Game_List)

    Game_List,Peak,Final=Matrix_form(Game_List,Peak,G)
    print(f"\nInitial Population:{a0}")
    print(f"Final Population:{Final}")
    print(f"Peak Population:{Peak}")
    print(f"Final Grid Of",end=" ")
    Matrix_print(G,Game_List)
