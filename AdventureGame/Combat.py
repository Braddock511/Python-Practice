import random
import time
class Combat:
    def __init__(self, character: dict, weapon: dict, enemy: dict):
        self.character = character
        self.weapon = weapon
        self.enemy = enemy

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

        #enemy
        self.enemy_hp = self.enemy['hp']
        self.enemy_attack = enemy['attack']
        self.enemy_dodge = enemy['dodge']

        

    def fight(self) -> bool:
        print('-'*40)
        print('Fight!'.center(40))
        print('-'*40)
        while True:
            #player
            self.fast_attack = int(random.uniform((self.attack / self.weight * (self.damage / self.speed_attack)) / 1.25, self.attack / self.weight * (self.damage / self.speed_attack)))
            self.strong_attack = int(random.uniform((self.attack + (self.damage * self.weight)) / 1.25, self.attack + (self.damage * self.weight))) 
            self.chance_of_dodge = round(random.uniform((self.agility / self.weight) / 4, self.agility / self.weight) / 2)
            self.chance_of_escape = round(random.uniform((self.speed / (self.weight * 4)) / 1.25, self.speed / (self.weight * 4)))
            
            #enemy
            self.attack_enemy = int(random.uniform(self.enemy_attack / 1.5, self.enemy_attack))*random.randint(1,4)
            self.dodge_enemy = round(random.uniform(self.enemy_dodge / 1.5, self.enemy_dodge))

            #luck in events
            luck = random.uniform(0,1)
            
            #lose
            if self.hp<1:
                print("")
                print('You lose!')
                return exit()

            print('-'*40)
            print(f'Your hp: {self.hp}      {self.enemy["name"]} hp: {self.enemy_hp}')
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
                    if luck > self.enemy_dodge / 100:
                        self.enemy_hp-=self.fast_attack
                        print("")
                        print(f"You dealt {self.fast_attack} damage to a {self.enemy['name']}!")
                        
                        if luck <= 0.1:
                            self.enemy_hp-=self.fast_attack
                            print("")
                            print("Double attack!")
                            print("")
                            print(f"You dealt additional {self.fast_attack} damage to a {self.enemy['name']}!")
                            time.sleep(1)
                    else:
                        print("")
                        print('Enemy dodged your attack!')
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
                    if luck > self.enemy_dodge / 100:
                        self.enemy_hp-=self.strong_attack
                        print("")
                        print(f"You dealt {self.strong_attack} damage to a {self.enemy['name']}!")
                        if luck <= 0.1:
                            self.enemy_hp-=self.strong_attack*1.5
                            print("")
                            print("Critical attack!")
                            print("")
                            print(f"You dealt additional {self.strong_attack*1.5} damage to a {self.enemy['name']}!")
                            time.sleep(1)
                    else:
                        print("")
                        print('Enemy dodged your attack!')
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
            if self.enemy_hp < 1:
                print("")
                print('You won!')
                return True

            else:
                #enemy attacks player
                if luck > self.chance_of_dodge/100:
                    self.hp-=self.attack_enemy
                    print("")
                    print(f'{self.enemy["name"]} dealt you {self.attack_enemy} damage!')
                else:
                    print("")
                    print(f'You dodged {self.enemy["name"]} attack!')
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