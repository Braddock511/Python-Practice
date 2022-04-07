import time
from Database import *
from Combat import *
from Story import *

def main():
    dbase = Db("localhost", 5432, "postgres", "postgres", "123")

    #region Login
    # print('Welcome in Adventure Game!')
    # print("")
    # acc = input('Do you have account? (Y/N) ')
    # if acc.upper() == 'Y':
    #     dbase.login()
    #     dbase.user_character()
    # elif acc.upper() == 'N':
        # dbase.new_user()
        # dbase.new_character()
        # dbase.add_to_main()
        # print('')
        # print('Sign in now')
        # dbase.login()
        # dbase.user_character()

    # stats = dbase.user_stats()
    #endregion

    #region Loading data
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
    #endregion

    #region Story
    # print('-'*60)
    # print('So you picked your hero, now you can go to conquer new land!')
    # time.sleep(1.5) 
    # print('You are in village, you see board with orders.')
    # print("")
    # time.sleep(1.5)
    # print('You have 2 contracts: ')
    # time.sleep(1)

    
    # print("")
    contract = answer(["Take a contract in which you have to receive merchant's treasures in village", "Take a contract on the troll"])

    #Village
    if contract==1:
        merchant = Npc('Merchant')
        # merchant.window(f"Hello stranger!\nRecently in our village has been strange things.\nIn my house start disappeared treasures.\nI'm pissed off!\nI think that blacksmith steal my things!\nFirst go to him and talk with him.\nIf you receive my treasures, I will pay you 25 gold.\nWhat do you think? You can do it for me?", False)

        take = input('(Y/N) ')
        if take.upper()=='Y':
            village = Room(["Merchant's house", "Blacksmith's house", "Huntress's house"])
            blacksmith = Npc('Blacksmith')
            huntress = Npc('Huntress')
            # items = Item(gold, [])
            village_items = Item(0, [])
            
            #flags
            basement_flag = False
            blacksmith_fight_flag = False 
            blacksmith_visit_flag = False
            forest_flag = False
            huntress_talk = False
            huntress_bribing = False
            end_village = True

            while end_village:
                print('-'*25)
                print('Village'.center(25))
                print('-'*25)

                house = village.create_rooms('house')
                #Rich villager's house
                if house == 1:
                    while True:
                        village.name_of_room(house)
                        merchant_house = Room(['Main room', 'Basement', 'Garden', "Back"])
                        doors = merchant_house.create_rooms('door')
                        
                        #Main room
                        if doors == 1:
                            if blacksmith_visit_flag==False:
                                merchant.window('Why are you still here?!\nGo to blacksmith and receive my treasures!', True)
                            else:
                                pass

                            #after fight with blacksmith 
                            if blacksmith_fight_flag:
                                merchant.window("And what? You get my treasures?", True, 'I receive your treasures, but unfortunately\nI had to get rid of thief. ')
                                #choose after stole gold from villager's chest
                                if basement_flag:
                                    merchant.window("Give it to me and don't show yourself to me here\nanymore you little thief!", False)
                                    kill_villager = answer(['Haha! Either you pay me my reward or I kill you', 'Exit'])

                                    if kill_villager==1:
                                        merchant.window("Take it and get the fuck out!", True)
                                        end_village = False
                                        break
                                    if kill_villager==2:
                                        end_village = False
                                        break
                                else:
                                    merchant.window("Haha, everything went my way!\nI mean...\nIt's a shame, but it was a thief anyway.\nHere it your reward.", True)
                                    end_village = False
                                    break
                            

                        #basement
                        if doors == 2:
                            if basement_flag == False:
                                print("")
                                print('Oh no! You are attacked in the basement by rabid rats!')
                                print("")
                                time.sleep(1.5)
                                Combat(character_statistics, weapon_statistics, *get_enemy('Rat'), 4).fight()

                                print('You defeated rabid rat! You can search basement now.')
                                merchant_house.name_of_room(doors)
                                steal_villager_gold = village_items.get_gold(15, "merchant's chest")
                                basement_flag = True
                                
                            else:
                                if steal_villager_gold:
                                    print('There is only dust and cobwebs here')
                                    time.sleep(1.5)
                                else:
                                    merchant_house.name_of_room(doors)
                                    steal_villager_gold = village_items.get_gold('15 gold', "in merchant's chest")


                        #garden                                    
                        if doors == 3:
                            print('You see beautiful trees and flowers')
                            time.sleep(1.5)

                        #exit
                        if doors == 4:
                            break
                

                #Blacksmith house
                if house == 2:
                    while True:
                        village.name_of_room(house)
                        blacksmith_house = Room(['Smithy', 'Main room', 'Back'])
                        doors = blacksmith_house.create_rooms('door')
                        
                        #smithy
                        if doors==1:
                            if blacksmith_fight_flag == False:
                                blacksmith.window("You wanna buy something?\nNot now, I'm working on new project.", True)

                            elif blacksmith_fight_flag:
                                print('You see a huge forge that is impressive.')
                                time.sleep(1)

                        #main room
                        if doors==2:
                            if blacksmith_visit_flag == False and blacksmith_fight_flag == False: 
                                blacksmith_house.name_of_room(doors)
                                village_items.get_items('precious metals', 'on the table')
                                blacksmith.window('Hey! What are you doing here?\nWhy are you hanging around?\nExplain yourself!', False)
                                kill_blacksmith = answer(["I'm looking for treasures which you stole merchant's!", "Not your business. Give me this treasures!"])

                                if kill_blacksmith == 1:
                                    blacksmith.window('What?! Are you kidding?\nThis dodger has been trying to kick me out of the \nmarket in such ways since last year!\nEhh, I see that he rented another mercenary.', False)
                                    kill_blacksmith2 = answer([f"Hmm...Interesting, why should I trust you?", "I don't care! Give me this treasures!"])

                                    if kill_blacksmith2 == 1:
                                        blacksmith.window("Go to huntress, she'll confirm my side of the story.", True)
                                        blacksmith_visit_flag = True

                                if kill_blacksmith == 2 or kill_blacksmith2 == 2:
                                    blacksmith.window('Haha! Fine, stand up for a fight!', True)
                                    Combat(character_statistics, weapon_statistics, *get_enemy('Blacksmith'), 1).fight()

                                    print('You recovered treasures.')
                                    time.sleep(1)
                                    blacksmith_fight_flag = True
                                    blacksmith_visit_flag = True

                            elif blacksmith_fight_flag:
                                print('The whole room is covered in blood and you can smell metal...')
                                time.sleep(2)


                        #exit
                        if doors == 3:
                            break

                #Huntress house  
                if house == 3:
                    while True:
                        village.name_of_room(house)
                        huntress_house = Room(['Hunting hut', 'Forest', 'Back'])
                        doors = huntress_house.create_rooms('door')

                        #Hunting hut
                        if doors == 1:
                            if blacksmith_visit_flag == False or blacksmith_fight_flag == True:
                                print('Door is closed.')
                                time.sleep(1)
                            
                            elif blacksmith_visit_flag:
                                huntress_bribery = []
                                bribe = None

                                if village_items.return_items()[0] >= 10:
                                    huntress_bribery.append('10 gold')

                                if 'skin wolf' in village_items.return_items()[1]:
                                    huntress_bribery.append('Skin wolf')

                                if huntress_talk == False:
                                    huntress.window("What's up?\nI was on hunting and I'm tired, so talk quickly.", True, 'I talked with blacksmith and he said that \nmerchant is greedy fraud who wants kick him \nout of the market.\nYou will supposedly confirm his side of the story. ')

                                    huntress.window("Yea, it's true.\nI'll tell you more, if you bring me some \nanimal skin or give me 10 gold.", True)
                                    huntress_talk = True

                                    if len(huntress_bribery) == 0:
                                        print("")
                                        print("You don't have gold or skin now")
                                        time.sleep(2)
                                    else:
                                        bribe = answer([*huntress_bribery])
                                else:
                                    huntress.window("And? Do you have something for me?", False)
                                    bribe = answer([*huntress_bribery, 'No'])

                                if bribe == 1:
                                    village_items.gold_sub(10)
                                    huntress_bribing = True 

                                if bribe == 2:
                                    village_items.remove_item('skin wolf')
                                    huntress_bribing = True 

                                if huntress_bribing == True:
                                    huntress.window("Thank you very much.\nSo a week ago when I skined an animal I heard a strange\nnoise in the merchant's house so I sneaked into the him\ngarden and saw him dig a hole then \nthrow in the treasures and bury them...", True, "Look who's come. Merchant with some bandits.")

                                    merchant.window("Hello my friends!\nYou were to talk to blacksmith, not flirt with huntress.", False)
                                    merchant_talk = answer(["Blacksmith didn't rob you! You hid treasures in your \ngarden yourself to frame him!", "I talked with him and I discovered that he robbed you\nand huntress helped him transfer money."])

                                    #help huntress and blacksmith
                                    if merchant_talk == 1:
                                        merchant.window("I knew not to trust you! Mercenaries kill them!", True)
                                        Combat(character_statistics, weapon_statistics, *get_enemy('Mercenary'), 3).fight(['Huntress', 30])

                                        huntress.window('',True)

                                    #help merchant
                                    if merchant_talk == 2:
                                        merchant.window("Good job! I will double your reward!\nBut now, mercenaries handcuff her and then handcuff \nblacksmith!", True)

                                        huntress.window("Haha! Over my dead body!", True)
                                        # Combat(character_statistics, weapon_statistics, *get_enemy('Huntress'), 1).fight(['Mercenary', 10])

                                        merchant.window("Mercenary! Throw her body to lake.", True)

                                        print("")
                                        print("You go to merchant's house with merchant.")
                                        print("")
                                        time.sleep(2)

                                        #merchant's house
                                        village.name_of_room(1)

                                        blacksmith.window("What have you done!? I will go get my colleagues \nand I will kill you!", True, "*Blacksmith leaves house*")

                                        merchant.window("I have to escape! I need escort! Do you help me?\nI will pay you a lot of gold!", False)

                                        merchant_escort = answer(["I did my job and I expect my reward.\nThat's all", "Ehh...\nOkay, but it will cost you a lot of money.\nWhere are we going?"])

                                        #not escort merchant's
                                        if merchant_escort == 1:
                                            merchant.window("Take it and don't show yourself anymore!", True)
                                            village_items.get_gold(50, '', False)
                                            end_village = False
                                            break

                                        #merchant's escort
                                        if merchant_escort == 2:
                                            print("")
                                            print("You and mercenaries escort merchant to forest.")
                                            print("")
                                            time.sleep(2)

                                            print("Mercenary: Watch out! Monster!")
                                            time.sleep(1)

                                            # Combat(character_statistics, weapon_statistics, *get_enemy('Troll'), 1).fight(['Mercenaries', 50])

                                            merchant.window("What was that?! It almost kill us!", True, "It was troll, we have to speed up.\nHere is more monsters.")

                                            print("")
                                            print("You are almost at the exit of forest, until suddenly...")
                                            time.sleep(3)
                                            print("")
                                            print("Mercenary is killed by an arrow and bandits\njumps out of the bushes!")
                                            time.sleep(2)

                                            # Combat(character_statistics, weapon_statistics, *get_enemy('Bandits'), 10).fight(['Mercenaries', 30])

                                            print("After long fight finally you exit the forest")
                                            time.sleep(2)

                                            merchant.window("I thought I was going to die! You saved me,\nso it is your reward. 100 Gold.It's enough?", False)
                                            merchant_gold = answer(['Yes. Bye...', "Ha! Are you kidding me? 200 gold at least.", "I don't want your money. You piece of shit. Bye."])

                                            if merchant_gold == 1:
                                                merchant.window("It's a pleasure doing business with you.\nBye!", True)
                                                village_items.get_gold(100, '', False)
                                                end_village = False
                                                break

                                            if merchant_gold == 2:
                                                merchant.window("You are greedy, but let it be. Here is your 200 gold.\nBye.", True)
                                                village_items.get_gold(200, '', False)
                                                end_village = False
                                                break

                                            if merchant_gold == 3:
                                                merchant.window("Haha! Whatever, better for me.\nBye.")
                                                end_village = False
                                                break
                                            
                        #Forest
                        if doors == 2:
                            if forest_flag == False:
                                huntress_house.name_of_room(doors)
                                print('')
                                print('Forest is mysterious and dark...')
                                time.sleep(2)
                                print('You go deeper and deeper until you notice a pack of wolves!')
                                time.sleep(2)
                                fight_with_wolves = answer(["Fight with them!", "Escape!"])

                                if fight_with_wolves == 1:
                                    Combat(character_statistics, weapon_statistics, *get_enemy('Wolf'), 3).fight()
                                    village_items.get_items('skin wolf', 'from wolves')

                                forest_flag = True
                            else:
                                print('You have nothing to go there.')
                                time.sleep(2)

                        if doors == 3:
                            break
        else:
            pass

    elif contract == 2:
        print("Troll")
    
    dbase.close()

    #endregion
        
if __name__ == '__main__':
    main()

