import random
class Combat:
    def __init__(self, character, weapon):
        character = character[0]
        weapon = weapon[0]

        self.fast_attack = random.randrange((weapon[0]*(character[1]/weapon[1]))/1.25, weapon[0]*(character[1]/weapon[1]))
        self.strong_attack = round(random.uniform((weapon[0]+(character[1]*weapon[2]))/1.25, weapon[0]+(character[1]*weapon[2])), 2) 
        self.chance_of_dodge = round(random.uniform((character[2]/weapon[2])/4, character[2]/weapon[2])/2 ,2)
        self.chance_of_escape = round(random.uniform((character[4]/(weapon[2]*2))/1.25, character[4]/(weapon[2]*2)),2)
        
        
        print(self.chance_of_escape)

Warrior_with_sword = Combat([(120,100,60,20,30)],[(100,50,1.35)])
Wizard_with_fire = Combat([(60,140,20,100,20)],[(200,10,0.20)])
Archer_with_short = Combat([(80,120,80,60,50)],[(100, 50, 0.50)])