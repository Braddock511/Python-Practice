import time
from Database import *
from Combat import *
from Story import *

def main():
    dbase = Db(host="localhost", port = 5432, db="postgres", user="postgres", password="123")

    # print('Welcome in Adventure Game!')
    # print("")
    # acc = input('Do you have account? (Y/N) ')
    # if acc.upper() == 'Y':
    #     dbase.login()
    #     dbase.user_character()
    # elif acc.upper() == 'N':
    #     dbase.new_user()
    #     dbase.new_character()
    #     dbase.add_to_main()
    #     print('')
    #     print('Sign in now')
    #     dbase.login()
    #     dbase.user_character()

    # stats = dbase.user_stats()

    #Loading data
    character_statistics = {'name':'','hp':'','damage':'','agility':'','intelligence':'','speed':''}

    # character = dbase.execute(f"SELECT name, hp, damage, agility, intelligence, speed FROM characters WHERE name='{stats[0][1]}'")
    character = dbase.execute(f"SELECT name, hp, damage, agility, intelligence, speed FROM characters WHERE name='Warrior'")
    
    for i, keys in enumerate(character_statistics.keys()):
        character_statistics[keys] = character[0][i]


    weapon_statistics = {'name':'','attack':'','speed_attack':'','weight':''}

    # weapon = dbase.execute(f"SELECT name, attack, speed_attack, weight FROM weapons WHERE name='{stats[1][2]}'")
    weapon = dbase.execute(f"SELECT name, attack, speed_attack, weight FROM weapons WHERE name='sword'")

    for i, keys in enumerate(weapon_statistics.keys()):
        weapon_statistics[keys] = weapon[0][i]

    list_of_monsters = []

    monsters = dbase.execute('SELECT name, hp, attack, dodge FROM monsters')
    for monster in monsters:
        list_of_monsters.append({'name':monster[0],'hp':monster[1],'attack':monster[2],'dodge':monster[3]})

    
    #story
    # print('-'*60)
    # print('So you picked your hero, now you can go to conquer new land!')
    # time.sleep(2.5)
    # print("But you can't, because...")
    # time.sleep(2)
    # print('You are poor and you have 0 gold, so you need take a contract!')
    # time.sleep(2.5)
    # print('-'*60)
    # input('Press enter to continue ')

    # print("")
    # print('You are in village, you see board with orders')
    # print("")
    # time.sleep(1.5)
    # print('You have 2 options: ')
    # time.sleep(1)
    while True:
        # print("")
        # print('1. Take a contract in which you have to solve riddle in village')
        # print('2. Take a contract on the troll')
        # print('')
        # answer = int(input('Choose: '))

        # #Riddle in village
        # if answer==1:
            rich_villager = Npc('Rich villager')
        #     rich_villager.window(f"Hello stranger!\nRecently in our village has been strange things.\nIn my house start disappeared treasures.\nI'm pissed off!\nI think that blacksmith steal my things!\nFirst go to him and talk with him.\nIf you catch that the bastard, I will pay you 25 gold.\nWhat do you think? You can do it for me?")
            take = input('(Y/N) ')
            if take.upper()=='Y':
                #village location
                village = Room(["Rich villager's house", "Blacksmith's house", "Huntress's house"])

                basement_flag = False

                while True:
                    print('-'*25)
                    print('Village'.center(25))
                    print('-'*25)

                    village.create_rooms()
                    print("")
                    room = int(input('Choose room: '))
                    print("")
                    
                    #Rich villager's house
                    if room==1:
                        while True:
                            village.name_of_room(room)
                            villager_house = Room(['Main room', 'Basement', 'Garden', "Back"])
                            villager_house.create_rooms()
                            print("")
                            doors = int(input('Choose door: '))
                            print("")
                            
                            #main room
                            if doors==1:
                                rich_villager.window('Why are you still here?!\nGo to blacksmith and receive my treasures!')
                                input('Press enter: ')

                            #basement
                            if doors==2:
                                if basement_flag==False:
                                    print("")
                                    print('Oh no! You are attacked in the basement by rabid rat!')
                                    print("")
                                    time.sleep(1.5)
                                    result_of_fight = Combat(character_statistics, weapon_statistics, *[x for x in list_of_monsters if x['name']=='Rat']).fight()

                                    if result_of_fight:
                                        print('You defeated rabid rat! You can search basement now.')
                                        villager_house.name_of_room(doors)
                                        steal_villager_gold = villager_house.items('15 gold', "rich villager's chest")
                                        basement_flag=True
                                    else:
                                        pass
                                    
                                else:
                                    if steal_villager_gold:
                                        print('There is only dust and cobwebs here')
                                        time.sleep(1.5)
                                    else:
                                        villager_house.name_of_room(doors)
                                        steal_villager_gold = villager_house.items('15 gold', "rich villager's chest")


                            #garden                                    
                            if doors==3:
                                print('You see beautiful trees and flowers')
                                time.sleep(1.5)

                            #exit
                            if doors==4:
                                break
                    if room==2:
                        while True:
                            village.name_of_room(room)
                            blacksmith_house = Room(['Smithy', 'Main room', 'Back']).create_rooms()
                            print("")
                            doors = int(input('Choose door: '))
                            print("")

                            if doors==1:
                                print('smithy')

                            if doors==2:
                                print('main room')

                            if doors==3:
                                break


                            break

                    if room==3:
                        while True:
                            village.name_of_room(room)
                            huntress_house = Room(['Hunting hut', 'Forest', 'Back']).create_rooms()
                            print("")
                            doors = int(input('Choose door: '))
                            print("")

                            if doors==1:
                                print('hunting hut')

                            if doors==2:
                                print('forest')

                            if doors==3:
                                break

                                            
                            
                    
                break
            else:
                pass
        
                dbase.close()
        
        
if __name__ == '__main__':
    main()
