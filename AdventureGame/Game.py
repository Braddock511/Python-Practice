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

    
    list_of_enemies = []

    enemies = dbase.execute('SELECT name, hp, attack, dodge FROM enemies')
    for monster in enemies:
        list_of_enemies.append({'name':monster[0],'hp':monster[1],'attack':monster[2],'dodge':monster[3]})
    
    get_enemy = lambda name: [x for x in list_of_enemies if x['name']==name]


    # gold = dbase.execute(f"SELECT gold FROM main, characters as ch, weapons as w, users as u WHERE id_user = (SELECT id FROM users WHERE name='{dbase.get_name()}') AND u.name='{dbase.get_name()}' AND main.id_character = ch.id AND id_weapon = w.id AND ch.name = '{stats[0][1]}' AND w.name = '{stats[1][2]}'")[0][0]

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
        # option = answer(["Take a contract in which you have to receive villager's treasures in village", "Take a contract on the troll"])

        #Riddle in village
        # if option==1:
            rich_villager = Npc('Rich villager')
        #     rich_villager.window(f"Hello stranger!\nRecently in our village has been strange things.\nIn my house start disappeared treasures.\nI'm pissed off!\nI think that blacksmith steal my things!\nFirst go to him and talk with him.\nIf you catch that the bastard, I will pay you 25 gold.\nWhat do you think? You can do it for me?", False)

            take = input('(Y/N) ')
            if take.upper()=='Y':
                #village location
                village = Room(["Rich villager's house", "Blacksmith's house", "Huntress's house"])
                blacksmith = Npc('Blacksmith')
                # items = Items(gold)
                items = Items(0)
                
                #flags
                basement_flag = False
                blacksmith_fight_flag = False 
                blacksmith_visit_flag = False
                end_village = True

                while end_village:
                    print('-'*25)
                    print('Village'.center(25))
                    print('-'*25)

                    house = village.create_rooms('house')
                    
                    #Rich villager's house
                    if house==1:
                        while True:
                            village.name_of_room(house)
                            villager_house = Room(['Main room', 'Basement', 'Garden', "Back"])
                            doors = villager_house.create_rooms('door')
                            
                            #main room
                            if doors==1:
                                if blacksmith_visit_flag==False:
                                    rich_villager.window('Why are you still here?!\nGo to blacksmith and receive my treasures!', True)
                                else:
                                    pass

                                #after fight with blacksmith 
                                if blacksmith_fight_flag:
                                    _ = answer(['I receive your treasures, but unfortunately I had to get rid of thief'])

                                    if _ == 1:
                                        #choose after stole gold from villager's chest
                                        if basement_flag:
                                            rich_villager.window("Give it to me and don't show yourself to me here\nanymore you little thief!", False)
                                            kill_villager = answer(['Haha! Either you pay me my reward or I kill you', 'Exit'])

                                            if kill_villager==1:
                                                rich_villager.window("Take it and get the fuck out!", True)
                                                # dbase.execute(f'INSERT INTO main(gold) VALUES({1})')
                                                end_village = False
                                                break
                                            if kill_villager==2:
                                                end_village = False
                                                break
                                        else:
                                            rich_villager.window("Haha, everything went my way!\nI mean...\nIt's a shame, but it was a thief anyway.\nHere it your reward.", True)
                                            end_village = False
                                            break

                            #basement
                            if doors==2:
                                if basement_flag==False:
                                    print("")
                                    print('Oh no! You are attacked in the basement by rabid rats!')
                                    print("")
                                    time.sleep(1.5)
                                    fight_rat = Combat(character_statistics, weapon_statistics, *get_enemy('Rat'), 4).fight()

                                    if fight_rat:
                                        print('You defeated rabid rat! You can search basement now.')
                                        villager_house.name_of_room(doors)
                                        steal_villager_gold = items.get_items('15 gold', "rich villager's chest")
                                        basement_flag = True
                                    
                                else:
                                    if steal_villager_gold:
                                        print('There is only dust and cobwebs here')
                                        time.sleep(1.5)
                                    else:
                                        villager_house.name_of_room(doors)
                                        steal_villager_gold = items.get_items('15 gold', "in rich villager's chest")


                            #garden                                    
                            if doors==3:
                                print('You see beautiful trees and flowers')
                                time.sleep(1.5)

                            #exit
                            if doors==4:
                                break

                    #blacksmith house
                    if house==2:
                        while True:
                            village.name_of_room(house)
                            blacksmith_house = Room(['Smithy', 'Main room', 'Back'])
                            doors = blacksmith_house.create_rooms('door')
                            
                            #smithy
                            if doors==1:
                                if blacksmith_fight_flag==False:
                                    blacksmith.window("You wanna buy something?\nNot now, I'm working on new project.", True)

                                elif blacksmith_fight_flag:
                                    print('You see a huge forge that is impressive.')
                                    time.sleep(1)

                            #main room
                            if doors==2:
                                if blacksmith_visit_flag==False and blacksmith_fight_flag==False: 
                                    blacksmith_house.name_of_room(doors)
                                    items.get_items('precious metals', 'on the table')
                                    blacksmith.window('Hey! What are you doing here?\nWhy are you hanging around?\nExplain yourself!', False)
                                    kill_blacksmith = answer(["I'm looking for treasures which you stole rich villager's!", "Not your business. Give me this treasures!"])

                                    if kill_blacksmith==1:
                                        blacksmith.window('What?! Are you kidding?\nThis dodger has been trying to kick me out of the \nmarket in such ways since last year!\nEhh, I see that he rented another mercenary.', False)
                                        kill_blacksmith2 = answer([f"Hmm...Interesting, why should I trust you?", "I don't care! Give me this treasures!"])

                                        if kill_blacksmith2==1:
                                            blacksmith.window("Go to huntress, she'll confirm my side of the story.", True)
                                            blacksmith_visit_flag = True

                                    if kill_blacksmith == 2 or kill_blacksmith2 == 2:
                                        blacksmith.window('Haha! Fine, stand up for a fight!', True)
                                        fight_blacksmith = Combat(character_statistics, weapon_statistics, *get_enemy('Blacksmith'), 1).fight()

                                        if fight_blacksmith:
                                            print('You recovered treasures.')
                                            time.sleep(1)
                                            blacksmith_fight_flag = True
                                            blacksmith_visit_flag = True

                                elif blacksmith_fight_flag:
                                    print('The whole room is covered in blood and you can smell metal...')
                                    time.sleep(2)


                            #exit
                            if doors==3:
                                break

                    #huntress house
                    if house==3:
                        while True:
                            village.name_of_room(house)
                            huntress_house = Room(['Hunting hut', 'Forest', 'Back'])
                            doors = huntress_house.create_rooms('door')

                            if doors==1:
                                if blacksmith_fight_flag==False:
                                    print('Door is closed.')
                                    time.sleep(1)

                            if doors==2:
                                go_to_forest = answer(["Go to forest", "Back"])

                                if go_to_forest==1:
                                    huntress_house.name_of_room(doors)
                                    print('')
                                    print('Forest is mysterious and dark...')
                                    time.sleep(2)
                                    print('You go deeper and deeper until you notice a pack of wolves!')
                                    time.sleep(2)
                                    fight_with_wolves = answer(["Fight with them!", "Escape!"])

                                    if fight_with_wolves == 1:
                                        fight_wolf = Combat(character_statistics, weapon_statistics, *get_enemy('Wolf'), 3).fight()


                            if doors==3:
                                break

                                            
                            
                    
                break
            else:
                pass
        
                dbase.close()
        
        
if __name__ == '__main__':
    main()


#dodac golda