import random
import time
from dataclasses import dataclass

@dataclass
class Combat:
    character: dict 
    weapon: dict 
    enemy: dict 
    number_of_enemies: int = 1

    def __post_init__(self) -> None:
        #character
        self.hp = self.character['hp']
        self.damage =  self.character['damage']
        self.agility =  self.character['agility']
        self.speed =  self.character['speed']
        self.stamina = 100
        self.elixirs = 2
        self.static_hp = self.hp
        
        #weapon
        self.attack = self.weapon['attack']
        self.speed_attack = self.weapon['speed_attack']
        self.weight = self.weapon['weight']

        #enemy
        self.enemy_hp = self.enemy['hp'] * self.number_of_enemies
        self.enemy_attack = self.enemy['attack'] + self.number_of_enemies
        self.enemy_dodge = self.enemy['dodge']

    def fight(self, help: list[str, int] = ['', 0], arena: bool = False) -> bool:
        print('-'*40)
        print('Fight!'.center(40))
        print('-'*40)
        
        while True:
            #player
            self.fast_attack = int(random.uniform((self.attack * self.weight * (self.damage / self.speed_attack)) / 1.25, self.attack * self.weight * (self.damage / self.speed_attack)))
            self.strong_attack = int(random.uniform((self.attack + (self.damage * self.weight)) / 1.25, self.attack + (self.damage * self.weight))) 
            self.chance_of_dodge = round(random.uniform((self.agility / self.weight) / 4, self.agility / self.weight) / 2)
            
            #enemy
            self.attack_enemy = int(random.uniform(self.enemy_attack / 1.5, self.enemy_attack)) * random.randint(1,4)
            self.dodge_enemy = round(random.uniform(self.enemy_dodge / 1.5, self.enemy_dodge))

            #help from someone
            someone_name = help[0]
            someone_attack = int(random.uniform(help[1] / 1.5, help[1]))

            #luck in events
            luck = random.uniform(0,1)
            
            #lose
            if self.hp<1:
                print("")
                print('You lose!')
                time.sleep(2)
                
                if arena:
                    break
                
                return exit()
            
            #player choosing
            while True:
                print('-' * 40)
                print(f'Your hp: {self.hp}      {self.enemy["name"]} hp: {self.enemy_hp}')
                print(f'Your stamina: {self.stamina}')
                print('-' * 40)
                print('1. Fast attack') 
                print('2. Strong attack') 
                print('3. Rest')
                print(f'4. Drink elixir of vitality ({self.elixirs})')
                print("")

                try:
                    choice = int(input('Option: '))
                    break

                except ValueError:
                    print("")
                    print('Enter a number!')
                    print("")
                    time.sleep(1)
                    
            #fast attack
            if choice == 1:
                if self.stamina >= 25:
                    if luck > self.enemy_dodge / 100:
                        self.enemy_hp -= self.fast_attack
                        print("")
                        print(f"You dealt {self.fast_attack} damage to a {self.enemy['name']}!")
                        
                        if luck <= 0.1:
                            self.enemy_hp -= self.fast_attack
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
                        self.enemy_hp -= self.strong_attack
                        print("")
                        print(f"You dealt {self.strong_attack} damage to a {self.enemy['name']}!")

                        if luck <= 0.1:
                            self.enemy_hp -= self.strong_attack * 1.5
                            print("")
                            print("Critical attack!")
                            print("")
                            print(f"You dealt additional {self.strong_attack * 1.5} damage to a {self.enemy['name']}!")
                            time.sleep(1)

                    else:
                        print("")
                        print('Enemy dodged your attack!')
                        luck = random.uniform(0,1)

                    self.stamina -= 50

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
            
            #elixir of vitality
            if choice == 4:
                if self.elixirs != 0:
                    if self.static_hp != self.hp:
                        restore_hp = random.randint(int(self.static_hp / 2), self.static_hp)

                        if self.hp + restore_hp > self.static_hp:
                            restore_hp = self.static_hp - self.hp  
                        self.hp += restore_hp

                        print(f'You restored {restore_hp} hp!')
                        self.elixirs -= 1
                        time.sleep(1)
                        continue

                    else:
                        print("")
                        print("You have full hp!")
                        time.sleep(1)
                        continue

                else:
                    print("")
                    print("You don't have elixirs!")
                    time.sleep(1)
                    continue
                
                
            #someone attacks enemy
            if someone_attack > 0:
                if luck > self.enemy_dodge / 100:
                    print("")
                    self.enemy_hp -= someone_attack
                    print(f"{someone_name} dealt {someone_attack} damage to a {self.enemy['name']}!")
                    
                else:
                    print("")
                    print(f'Enemy dodged {someone_name} attack!')
                    luck = random.uniform(0,1)
                time.sleep(1)

            #win
            if self.enemy_hp < 1:
                print("")
                print('You won!')
                time.sleep(2)
                return True

            else:
                #enemy attacks player
                if luck > self.chance_of_dodge / 100:
                    self.hp -= self.attack_enemy
                    print("")
                    print(f'{self.enemy["name"]} dealt you {self.attack_enemy} damage!')

                else:
                    print("")
                    print(f'You dodged {self.enemy["name"]} attack!')
                time.sleep(1)
            
            time.sleep(.5)

    def show_statistics(self):
        print('-' * 20)
        print(f"Hp: {self.character['hp']}")
        print(f"Damage: {self.character['damage']}")
        print(f"Agility: {self.character['agility']}")
        print(f"Intelligence: {self.character['intelligence']}")
        print(f"Speed: {self.character['speed']}")
        print('-' * 20)
        input('Press enter to exit ')