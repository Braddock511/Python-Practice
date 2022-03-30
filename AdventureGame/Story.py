class Npc():
    def __init__(self, name: str):
        self.name = name

    #creating window of npc's text
    def window(self, text: str, without_choose: bool):
        print('-'*55)
        print(f'Person: {self.name}'.center((55)))
        print('')
        print(text)
        print('-'*55)
        if without_choose:
            input('Press enter: ')


class Room():
    def __init__(self, rooms: list):
        self.rooms = rooms

    #creating list of rooms to choose
    def create_rooms(self, entry) -> int:
        for i, room in enumerate(self.rooms):
            print(f'{i+1}. {room}')
        print("")
        choose = int(input(f'Choose {entry}: '))
        print("")
        return choose

    #showing name of room 
    def name_of_room(self, choose: int):
        print("-"*30)
        print(self.rooms[choose-1].center(30))
        print("-"*30)

class Items():
    def __init__(self, gold):
        self.gold = 0
        self.item = [] 
    #items found during game
    def get_items(self, name_of_item: str, where: str) -> bool:
        print('')
        print(f'You found {name_of_item} {where}!')
        print('')
        take = input('You wanna take it? (Y/N) ')

        if take.upper() == 'Y':
            split = name_of_item.split(" ")
            try:
                if split[1] == 'gold':
                    self.gold += int(split[0])
                else:
                    self.item.append(name_of_item)
            except IndexError:
                self.item.append(name_of_item)

            return True
        else:
            return False

    def return_items(self) -> list:
        return [self.gold, self.item]


def answer(answers: list) -> int:
        for i, answer in enumerate(answers):
            print(f'{i+1}. {answer}')
        
        print("")
        choose = int(input('Choose answer: '))
        return choose
