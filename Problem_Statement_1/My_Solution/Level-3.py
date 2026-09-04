#Welcome To Conway's Game Of Life:
#All the Functions are in the File Mentioned!

from My_Functions import mapint_function,Matrix_print,Matrix_print_2,alive_count,Matrix_form_l3
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

Game_List,Peak,Final=Matrix_form_l3(Game_List,Peak,G)
print(f"\nInitial Population:{a0}")
print(f"Final Population:{Final}")
print(f"Peak Population:{Peak}")
print(f"Final Grid Of",end=" ")
Matrix_print_2(G,Game_List)

#My Python IDLE did not support screen-clearing via code, so had to resort to printing newlines to give the feel of New screen.
#Possible methods include the os.system('cls') or the subprocess.run('cls' if os.name()=='nt' else 'clear')
#No similar function for IDLE Shell 3.14.6
