import time
from dataclasses import dataclass

@dataclass
class Npc():
    name: str

    #creating window of npc's text
    def window(self, text: str, without_choose: bool, answer: str = '') -> None:
        print('-'*55)
        print(f'Person: {self.name}'.center((55)))
        print('')
        print(text)
        print('-'*55)

        if without_choose:
            input(f'Press enter: {answer}')

@dataclass
class Room():
    rooms: list 

    #creating list of rooms to choose
    def create_rooms(self, entry) -> int:
        while True:
            for i, room in enumerate(self.rooms):
                print(f'{i + 1}. {room}')

            try:
                print("")
                choose = int(input(f'Choose {entry}: '))
                print("")
                return choose

            except ValueError:
                print("")
                print('Enter a number!')
                print("")
                time.sleep(1)

    #showing name of room 
    def name_of_room(self, choose: int) -> None:
        print("-"*55)
        print(self.rooms[choose - 1].center(55))
        print("-"*55)

@dataclass
class Item():
    gold: int 
    items: list 

    #items found during game
    def get_items(self, name_of_item: str, where: str) -> list:
        
        while True:
            print('')
            print(f'You found {name_of_item} {where}!')
            print('')
            take = input('You wanna take it? (Y/N) ')

            if take.upper() == 'Y':
                self.items.append(name_of_item)

            elif take.upper() == 'N':
                break
                
            else:
                print("")
                print('You can only choose between yes and no!')
                time.sleep(1)

            return self.items

    #gold found druning game
    def get_gold(self, new_gold: int, where: str, found: bool = True) -> int:
        while True:

            if found:
                print('')
                print(f'You found {new_gold} gold {where}!')
                print('')

                take = input('You wanna take it? (Y/N) ')

                if take.upper() == 'Y':
                    self.gold += new_gold

                elif take.upper() == 'N':
                    break
                
                else:
                    print("")
                    print('You can only choose between yes and no!')
                    time.sleep(1)

            else:
                self.gold += new_gold

            return self.gold

    #gold subtraction
    def gold_sub(self, gold: int) -> int:
        self.gold -= gold
        return self.get_gold
    
    #remove item from list
    def remove_item(self, item: str) -> list:
        try:
            self.items.remove(item)

        except ValueError:
            pass

        return self.items


    def return_items(self) -> list:
        return [self.gold, self.items]


def answer(answers: list) -> int:
    while True:

        for i, answer in enumerate(answers):
            print("")
            print(f'{i + 1}. {answer}')
        print("")

        try:
            choose = int(input('Choose answer: '))

            if choose > len(answers):
                print("")
                print('The number is out of range!')
                print("")
                time.sleep(1)
                continue

            return choose

        except ValueError:
            print('')
            print('Enter a number!')
            print('')
            time.sleep(1)