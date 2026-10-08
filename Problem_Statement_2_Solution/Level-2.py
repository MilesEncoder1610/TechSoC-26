'''Please Enter The Statements One by One for Execution In Interactive Mode!
Else, Please drop it directly here!'''


class Bender:
    damage=(self.att * self.move[num][1]) / name1.Def
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
        a=f"{self.name} used {self.move[num][0]}!\n"
        b=f"{name1.name} took {round(damage)} damage!\n"
        if (name1.hp>round(damage)):
            name1.hp-=round(damage)
        else:
            name1.hp-=name1.hp
        print(a+b)
    def is_fainted(self):
        return True if self.hp==0 else False
class Duel:
    from random import random
    def __init__(self,nam1,nam2):
        self.opp1=nam1
        self.opp2=nam2
    def turn_order(self):
        if self.opp1.speed > self.opp2.speed:
            return (self.opp1,self.opp2)
        elif self.opp2.speed > self.opp1.speed:
            return (self.opp2,self.opp1)
        else:
            return random.choice([(self.opp1, self.opp2), (self.opp2, self.opp1)])
    def enhanced_damage(self):
        b=random.choice(a[turn%2].move)
        print(f"{a[turn%2].name} used {b[0]}")
        base_damage=(a[turn%2].att * b[1]) / a[turn%2+1].Def
        set1={"Earth":1,"Air":2,"Fire":3,"Water":4}
        set2={"Water":1,"Earth":2,"Air":3,"Fire":4}
        if(set1[self.opp1.ele]==set2[self.opp2.ele]):
            type_multiplier=2.0
            Label="Super Effective! ({self.opp1.ele} is strong against {self.opp2.ele})"
        elif(set2[self.opp1.ele]==set1[self.opp2.ele]):
            type_multiplier=0.5
            Label="Not Very Effective... ({self.opp1.ele} is weak against {self.opp2.ele})"
        else:
            type_multiplier=1.0
            Label="Neutral.. (Both are Equally Strong)"
        print(Label)
        critical_hit=random() < 0.1
        if(critical_hit):
            critical_multiplier=2.0
            print("Critical Hit!")
        else:
            critical_multiplier=1.0
        final_damage=base_damage*type_Multiplier*critical_multiplier
        return max(1,round(final_damage))
    def start_duel(self):
        print(f"=== THE BATTLE BEGINS! ===")
        print(f"{self.opp1.name} ({self.oop1.ele}, HP: {self.opp1.hp}/{self.opp1.max_hp} VS ", end="")
        print(f"{self.opp2.name} ({self.oop2.ele}, HP: {self.opp2.hp}/{self.opp2.max_hp}")
        turn=1
        a=turn_order(self)
        while(self.opp1.hp>0 and self.opp2.hp>0):
            print(f"Turn {turn}: ",end="")
            if(turn%2==0):
                print(f"{a[1].name} strikes back!")
            elif(turn==1):
                print(f"{a[0].name} goes first! (Speed: {a[0].speed} vs {a[1].speed})")
            else:
                print(f"{a[0].name} goes first!")
            dam=enhanced_damage(self)
            if(dam>a[turn%2].hp):
                a[turn%2].hp==0
            else:
                a[turn%2].hp-=dam
            print(f"{a[turn%2].name} took {dam} damage!")
            print(f"{a[turn%2].name} HP: {a[turn%2].hp}/{a[turn%2].max_hp}\n")
            turn+=1
        if(turn%2==0):
            print(f"{a[1].name} fainted!")
            print(f"{a[0].name} wins the duel!")
        else:
            print(f"{a[0].name} fainted!")
            print(f"{a[1].name} wins the duel!")
        print("Duel Summary:")
        print(" Winner:
