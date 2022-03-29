import random
import time
class Combat:
    def __init__(self, character: dict, weapon: dict, monster: dict):
        self.character = character
        self.weapon = weapon
        self.monster = monster

        #character
        self.hp = self.character['hp']
        self.damage =  self.character['damage']
        self.agility =  self.character['agility']
        self.speed =  self.character['speed']
        self.stamina = 100
        
        #weapon
        self.attack = self.weapon['attack']
        self.speed_attack = self.weapon['speed_attack']
        self.weight = self.weapon['weight']

        #monster
        self.monster_hp = self.monster['hp']
        self.monster_attack = monster['attack']
        self.monster_dodge = monster['dodge']

        

    def fight(self):
        print('-'*40)
        print('Fight!'.center(40))
        print('-'*40)
        while True:
            #player
            self.fast_attack = random.randrange((self.attack * (self.damage / self.speed_attack)) / 1.25, self.attack * (self.damage / self.speed_attack))
            self.strong_attack = int(random.uniform((self.attack + (self.damage * self.weight)) / 1.25, self.attack + (self.damage * self.weight))) 
            self.chance_of_dodge = round(random.uniform((self.agility / self.weight) / 4, self.agility / self.weight) / 2)
            self.chance_of_escape = round(random.uniform((self.speed / (self.weight * 4)) / 1.25, self.speed / (self.weight * 4)))
            
            #monster
            self.attack_monster = int(random.uniform(self.monster_attack / 1.5, self.monster_attack))*random.randint(1,4)
            self.dodge_monster = round(random.uniform(self.monster_dodge / 1.5, self.monster_dodge))

            # #luck in events
            luck = random.uniform(0,1)

            #lose
            if self.hp<1:
                print("")
                print('You lose!')
                return exit()

            print('-'*40)
            print(f'Your hp: {self.hp}      {self.monster["name"]} hp: {self.monster_hp}')
            print(f'Your stamina: {self.stamina}')
            print('-'*40)
            print('1. Fast attack') 
            print('2. Strong attack') 
            print('3. Rest')
            print('4. Escape')
            print("")
            choice = int(input('Option: '))

            #fast attack
            if choice == 1:
                if self.stamina >= 25:
                    if luck > self.monster_dodge / 100:
                        self.monster_hp-=self.fast_attack
                        print("")
                        print(f"You dealt {self.fast_attack} damage to a {self.monster['name']}!")
                        
                        if luck <= 0.1:
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

                    self.stamina -= 25
                else:
                    print("")
                    print('You have to rest!')
                    pass
                time.sleep(1)

            #strong attack
            if choice == 2:
                if self.stamina >= 50:
                    if luck > self.monster_dodge / 100:
                        self.monster_hp-=self.strong_attack
                        print("")
                        print(f"You dealt {self.strong_attack} damage to a {self.monster['name']}!")
                        if luck <= 0.1:
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
            if choice == 3:
                self.stamina = 100
                print("")
                print('You rested!')
            
            #escape
            if choice==4:
                if luck < self.chance_of_escape/100:
                    print("")
                    print('You were escaped!')
                    return False

                else:
                    print(f"You weren't escaped!")
            
            #win
            if self.monster_hp < 1:
                print("")
                print('You won!')
                return True

            else:
                #monster attacks player
                if luck > self.chance_of_dodge/100:
                    self.hp-=self.attack_monster
                    print("")
                    print(f'{self.monster["name"]} dealt you {self.attack_monster} damage!')
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


# a = Combat({'name': 'Warrior', 'hp': 120, 'damage': 100, 'agility': 60, 'intelligence': 20, 'speed': 30}, {'name': 'sword', 'attack': 100, 'speed_attack': 50, 'weight': 1.35},{'name': 'Troll', 'hp': 500, 'attack': 20, 'dodge': 70}).fight()