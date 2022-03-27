import random
import time
class Combat:
    def __init__(self, character: dict, weapon: dict, monster: dict):
        self.character = character
        self.weapon = weapon
        self.monster = monster

        #player
        self.hp = self.character['hp']
        self.fast_attack = round(random.randrange((self.weapon['attack']*(self.character['damage']/self.weapon['speed_attack']))/1.25, self.weapon['attack']*(self.character['damage']/self.weapon['speed_attack'])), 2)
        self.strong_attack = round(random.uniform((self.weapon['attack']+(self.character['damage']*self.weapon['weight']))/1.25, self.weapon['attack']+(self.character['damage']*self.weapon['weight'])), 2) 
        self.chance_of_dodge = round(random.uniform((self.character['agility']/self.weapon['weight'])/4, self.character['agility']/self.weapon['weight'])/2 ,2)
        self.chance_of_escape = round(random.uniform((self.character['speed']/(self.weapon['weight']*4))/1.25, self.character['speed']/(self.weapon['weight']*4)), 2)
        self.stamina = 100

        #monster
        self.monster_hp = self.monster['hp']
        self.monster_attack = round(random.uniform(self.monster['attack']/1.5, self.monster['attack']), 2)
        self.monster_dodge = round(random.uniform(self.monster['dodge']/1.5, self.monster['dodge']), 2)

    def fight(self):
        print('Fight!')
        while True:
            #result of fight
            if self.monster_hp<1:
                print("")
                print('You won!')
                break

            if self.hp<1:
                print("")
                print('You lose!')
                break

            luck = random.uniform(0,1)
            self.monster_attack = int(self.monster_attack*random.randint(1,3))

            print('-'*40)
            print(f'Your hp: {int(self.hp)}      | {self.monster["name"]} hp: {int(self.monster_hp)}')
            print(f'Your stamina: {self.stamina} |')
            print('-'*40)
            print('1. Fast attack') 
            print('2. Strong attack') 
            print('3. Rest')
            print('4. Escape')
            print("")
            choice = int(input('Option: '))

            #fast attack
            if choice==1:
                if self.stamina>=25:
                    if luck>self.monster_dodge/100:
                        self.monster_hp-=self.fast_attack
                        print("")
                        print(f"You dealt {self.fast_attack} damage to a {self.monster['name']}!")
                        
                        if luck<=0.1:
                            self.monster_hp-=self.fast_attack
                            print("")
                            print("Double attack!")
                            print("")
                            print(f"You dealt additional {self.fast_attack} damage to a {self.monster['name']}!")
                            time.sleep(1)
                    else:
                        print("")
                        print('Monter dodged your attack!')
                        luck = random.uniform(0,1)

                    self.stamina-=25
                else:
                    print("")
                    print('You have to rest!')
                    pass
                time.sleep(1)

            #strong attack
            if choice==2:
                if self.stamina>=50:
                    if luck>self.monster_dodge/100:
                        self.monster_hp-=self.strong_attack
                        print("")
                        print(f"You dealt {int(self.strong_attack)} damage to a {self.monster['name']}!")
                        
                        if luck<=0.1:
                            self.monster_hp-=self.strong_attack*1.5
                            print("")
                            print("Critical attack!")
                            print("")
                            print(f"You dealt additional {self.strong_attack*1.5} damage to a {self.monster['name']}!")
                            time.sleep(1)
                    else:
                        print("")
                        print('Monter dodged your attack!')
                        luck = random.uniform(0,1)

                    self.stamina-=50
                else:
                    print("")
                    print('You have to rest!')
                    pass
                time.sleep(1)

            #rest
            if choice==3:
                self.stamina=100
                print("")
                print('You rested!')
            
            #escape
            if choice==4:
                if luck<self.chance_of_escape/100:
                    print('You were escaped!')
                    break
                else:
                    print(f"You weren't escaped! You lost {int(self.monster_attack)} hp")
                    self.hp-=self.monster_attack
                    pass
            

            #monster attack player
            if luck>self.chance_of_dodge/100:
                self.hp-=self.monster_attack
                print("")
                print(f'{self.monster["name"]} dealt you {self.monster_attack} damage!')
            else:
                print("")
                print(f'You dodged {self.monster["name"]} attack!')
            time.sleep(1)
            

            time.sleep(.5)

    def show_statistics(self):
        print('-'*20)
        print(f"Hp: {self.character['hp']}")
        print(f"Damage: {self.character['damage']}")
        print(f"Agility: {self.character['agility']}")
        print(f"Intelligence: {self.character['intelligence']}")
        print(f"Speed: {self.character['speed']}")
        print('-'*20)
        input('Press enter to exit ')

