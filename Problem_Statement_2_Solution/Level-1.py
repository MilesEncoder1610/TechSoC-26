'''Please Enter The Statements One by One for Execution In Interactive Mode!
Else, Please drop it directly here!'''
#Got to learn about round function from this damage definition!


class Bender:
    def __init__(self,name,element,hp,attack,defense,speed,moves):
        self.name=name
        self.ele=element
        self.hp=hp
        self.max_hp=hp
        self.att=attack
        self.Def=defense
        self.speed=speed
        self.move=moves
    def display_stats(self):
        a=f"{self.name} ({self.ele}) - HP: {self.hp}/{self.max_hp}, Attack: {self.att}, Defense: {self.Def}, Speed: {self.speed}"
        b=f"\nMoves: "
        for i in self.move[:-1]:
            b+=f"{i[0]} ({i[1]}), "
        b+=f"{self.move[-1][0]} ({self.move[-1][1]})\n"
        return a+b
    def attack(self,name1,num):
        damage=round((self.att * self.move[num][1]) / name1.Def)
        a=f"{self.name} used {self.move[num][0]}!\n"
        b=f"{name1.name} took {damage} damage!\n"
        if (name1.hp>damage):
            name1.hp-=damage
        else:
            name1.hp-=name1.hp
        print(a+b)
    def is_fainted(self):
        return True if self.hp==0 else False
