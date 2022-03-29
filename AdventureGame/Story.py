class Npc():
    def __init__(self, name: str):
        self.name = name

    #creating window of npc's text
    def window(self, text: str):
        print('-'*55)
        print(f'Person: {self.name}'.center((55)))
        print('')
        print(text)
        print('-'*55)


class Room():
    def __init__(self, rooms: list):
        self.rooms = rooms

    #creating list of rooms to choose
    def create_rooms(self):
        for i, room in enumerate(self.rooms):
            print(f'{i+1}. {room}')

    #showing name of room 
    def name_of_room(self, choose: int):
        print("-"*30)
        print(self.rooms[choose-1].center(30))
        print("-"*30)

    #items found during game
    def items(self, name_of_item: str, where: str):
        print('')
        print(f'You found {name_of_item} in {where}!')
        print('')
        take = input('You wanna take it? (Y/N) ')
        if take.upper() == 'Y':
            return True
        else:
            return False

