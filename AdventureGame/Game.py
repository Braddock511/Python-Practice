import time
from tkinter import W
from Database import *
from Combat import *
from Story import *

def main():
    dbase = Db("localhost", 5432, "postgres", "postgres", "123")

    #region Login
    print("-" * 55)
    print('Welcome in Adventure Game!'.center(55))
    print("-" * 55)

    acc = input('Do you have account? (Y/N) ')

    if acc.upper() == 'Y':
        dbase.login()
        dbase.user_character()

    elif acc.upper() == 'N':
        dbase.new_user()
        dbase.new_character()
        dbase.add_to_main()
        print('')
        print('Sign in now')
        dbase.login()
        dbase.user_character()

    stats = dbase.user_stats()
    #endregion

    #region Loading data

    #character
    character_statistics = {'name':'', 'hp':'', 'damage':'', 'agility':'', 'intelligence':'', 'speed':''}

    character = dbase.execute(f"SELECT name, hp, damage, agility, intelligence, speed FROM characters WHERE name='{stats[0][1]}'")
    
    for i, keys in enumerate(character_statistics.keys()):
        character_statistics[keys] = character[0][i]

    #weapon
    weapon_statistics = {'name':'', 'attack':'', 'speed_attack':'', 'weight':''}

    weapon = dbase.execute(f"SELECT name, attack, speed_attack, weight FROM weapons WHERE name='{stats[1][2]}'")

    for i, keys in enumerate(weapon_statistics.keys()):
        weapon_statistics[keys] = weapon[0][i]

    #enemies
    list_of_enemies = []

    enemies = dbase.execute('SELECT name, hp, attack, dodge FROM enemies')
    for monster in enemies:
        list_of_enemies.append({'name':monster[0], 'hp':monster[1], 'attack':monster[2], 'dodge':monster[3]})
    
    get_enemy = lambda name: [x for x in list_of_enemies if x['name'] == name]

    #gold
    gold = dbase.execute(f"SELECT gold FROM main, characters as ch, weapons as w, users as u WHERE id_user = (SELECT id FROM users WHERE name='{dbase.get_name()}') AND u.name='{dbase.get_name()}' AND main.id_character = ch.id AND id_weapon = w.id AND ch.name = '{stats[0][1]}' AND w.name = '{stats[1][2]}'")[0][0]

    # endregion

    while True:
        print("-" * 55)
        print("Menu".center(55))
        print("-" * 55)

        menu = Room(["Story", "Arena", "Exit"]).create_rooms("")

        if menu == 1:
            print('-' * 60)
            print('You are in village, you see board with orders.')
            print("")
            time.sleep(1.5)
            print('You have 2 contracts: ')
            time.sleep(1)

            contract = answer(["Take a contract in which you have to receive merchant's treasures in village", "Take a contract on the troll"])

            #Merchant's treasures
            if contract == 1:
                #Npc
                merchant = Npc('Merchant')
                blacksmith = Npc('Blacksmith')
                huntress = Npc('Huntress')

                #item
                village_items = Item(gold, [])
                
                #flags
                basement_flag = False
                blacksmith_fight_flag = False 
                blacksmith_visit_flag = False
                forest_flag = False
                huntress_talk = False
                huntress_bribing = False

                end = True

                merchant.window("Hello stranger!\nRecently in our village has been strange things.\nIn my house start disappeared treasures.\nI'm pissed off!\nI think that blacksmith steal my things!\nFirst go to him and talk with him.\nIf you receive my treasures, I will pay you 25 gold.", True, "Ok, I'll go to him and check it out")

                village = Room(["Merchant's house", "Blacksmith's house", "Huntress's house"])

                while end:
                    print('-' * 55)
                    print('Village'.center(55))
                    print('-' * 55)

                    house = village.create_rooms('house')

                    #Rich villager's house
                    if house == 1:
                        while True:

                            village.name_of_room(house)
                            merchant_house = Room(['Main room', 'Basement', 'Garden', "Back"])
                            doors = merchant_house.create_rooms('door')
                            
                            #Main room
                            if doors == 1:
                                if blacksmith_visit_flag == False:
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
                                            dbase.execute(f"UPDATE main SET gold = gold+25 WHERE id_user=(SELECT id from users where name='{dbase.get_name()}')")
                                            end = False
                                            break

                                        if kill_villager==2:
                                            end = False
                                            break

                                    else:
                                        merchant.window("Haha, everything went my way!\nI mean...\nIt's a shame, but it was a thief anyway.\nHere it your reward.", True)
                                        dbase.execute(f"UPDATE main SET gold = gold+25 WHERE id_user=(SELECT id from users where name='{dbase.get_name()}')")
                                        end = False
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
                                    dbase.execute(f"UPDATE main SET gold = gold+15 WHERE id_user=(SELECT id from users where name='{dbase.get_name()}')")
                                    basement_flag = True
                                    
                                else:
                                    if steal_villager_gold:
                                        print('There is only dust and cobwebs here')
                                        time.sleep(1.5)

                                    else:
                                        merchant_house.name_of_room(doors)
                                        steal_villager_gold = village_items.get_gold(15, "in merchant's chest")
                                        dbase.execute(f"UPDATE main SET gold = gold+15 WHERE id_user=(SELECT id from users where name='{dbase.get_name()}')")
                                        


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
                            if doors == 1:
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
                                        Combat(character_statistics, weapon_statistics, *get_enemy('Blacksmith')).fight()

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

                                            print("")
                                            print("*Merchant escaped to his house*")
                                            time.sleep(2)
                                            huntress.window('Let him run away, follow me, we will go to blacksmith.', True)

                                            #blacksmith's house
                                            village.name_of_room(2)

                                            blacksmith.window("Oh, it's you again! With huntress.\nHow's the deal with the merchant?", True, "You were right, merchant is fraud!")

                                            huntress.window("And he wanted kill us!", True)

                                            blacksmith.window("It's too much! We must take revenge!", False)

                                            revenge = answer(["Yes! Let's go kill him!", "Sorry, but I can't. Goodbye."])

                                            #merchant's house
                                            if revenge == 1:
                                                print("")
                                                print("*You are going to merchant*")
                                                time.sleep(1)
                                                print("")
                                                print("Door is barricaded, so you and the blacksmith break them down.")
                                                time.sleep(3)

                                                village.name_of_room(1)

                                                merchant.window("Please, don't kill me!\nI'm sorry for everything!\nI'll give you all my gold which I have!\nPlease...", False)

                                                kill_merchant = answer(["Fine, but you will give us your all treasures\nand you'll get hell out of village!", "I don't care about your gold!\nI will kill you and burn your house!"])

                                                if kill_merchant == 1:
                                                    merchant.window("Thank you! I will take shovel\nand give you the gold right away.", True)
                                                    print("")
                                                    print("*Merchant leaves to garden*")
                                                    time.sleep(1)

                                                    blacksmith.window("That was not the deal, I will kill him.", True)
                                                    print("")
                                                    print("*Blacksmith goes to garden*")
                                                    time.sleep(1)

                                                    blacksmith.window("I took care of him, here is our gold.\nYour plot is 300 gold", False)

                                                    take_gold = answer(["Thanks, bye.", "Why did you kill him? You are barbarian!\nTake the gold for yourself, bye."])

                                                    if take_gold == 1:
                                                        dbase.execute(f"UPDATE main SET gold = gold+300 WHERE id_user=(SELECT id from users where name='{dbase.get_name()}')")
                                                        end = False
                                                        break

                                                    if take_gold == 2:
                                                        end = False
                                                        break

                                            if revenge == 2:
                                                end = False
                                                break

                                        #help merchant
                                        if merchant_talk == 2:
                                            merchant.window("Good job! I will double your reward!\nBut now, mercenaries handcuff her and then handcuff \nblacksmith!", True)

                                            huntress.window("Haha! Over my dead body!", True)
                                            Combat(character_statistics, weapon_statistics, *get_enemy('Huntress')).fight(['Mercenary', 10])

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
                                                dbase.execute(f"UPDATE main SET gold = gold+50 WHERE id_user=(SELECT id from users where name='{dbase.get_name()}')")
                                                end = False
                                                break

                                            #merchant's escort
                                            if merchant_escort == 2:
                                                print("")
                                                print("You and mercenaries escort merchant to forest.")
                                                print("")
                                                time.sleep(2)

                                                print("Mercenary: Watch out! Monster!")
                                                time.sleep(1)

                                                Combat(character_statistics, weapon_statistics, *get_enemy('Troll')).fight(['Mercenaries', 50])

                                                merchant.window("What was that?! It almost kill us!", True, "It was troll, we have to speed up.\nHere is more monsters.")

                                                print("")
                                                print("You are almost at the exit of forest, until suddenly...")
                                                time.sleep(3)
                                                print("")
                                                print("Mercenary is killed by an arrow and bandits\njumps out of the bushes!")
                                                time.sleep(2)

                                                Combat(character_statistics, weapon_statistics, *get_enemy('Bandits'), 10).fight(['Mercenaries', 30])

                                                print("After long fight finally you exit the forest")
                                                time.sleep(2)

                                                merchant.window("I thought I was going to die! You saved me,\nso it is your reward. 100 Gold.It's enough?", False)
                                                merchant_gold = answer(['Yes. Bye...', "Ha! Are you kidding me? 200 gold at least.", "I don't want your money. You piece of shit. Bye."])

                                                if merchant_gold == 1:
                                                    merchant.window("It's a pleasure doing business with you.\nBye!", True)
                                                    dbase.execute(f"UPDATE main SET gold = gold+100 WHERE id_user=(SELECT id from users where name='{dbase.get_name()}')")
                                                    end = False
                                                    break

                                                if merchant_gold == 2:
                                                    merchant.window("You are greedy, but let it be. Here is your 200 gold.\nBye.", True)
                                                    dbase.execute(f"UPDATE main SET gold = gold+200 WHERE id_user=(SELECT id from users where name='{dbase.get_name()}')")
                                                    end = False
                                                    break

                                                if merchant_gold == 3:
                                                    merchant.window("Haha! Whatever, better for me.\nBye.")
                                                    end = False
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

            #Troll
            elif contract == 2:
                #Npc
                principal = Npc("Villager")
                troll = Npc("Troll")
                merchant = Npc("Merchant")

                village = Room(["Principal's house", "Market", "Bridge"])

                #flags
                troll_visit = False
                fight_with_troll = False
                fight_with_troll_2 = False
                troll_trust = False
                convince_troll = False
                lower_fee = False
                do_nothing = False

                end = True

                principal.window("Hello stranger!\nAt the bridge crossing near our village, The troll \nwants payment from the residents for crossing bridge.\nHe counts 10 gold for the passage!\nWho does he think he is!?\nI will pay you 40 gold for his head.\nWhat do you think? You can do it for me?", True, "Ok, I can help you")

                while end:
                    print('-' * 55)
                    print('Village'.center(55))
                    print('-' * 55)

                    place = village.create_rooms('place')

                    #Principal's house
                    if place == 1:
                        if troll_visit == False:
                            principal.window('You have a job to do my friend.', True)

                        if fight_with_troll:
                            principal.window("Oh, You are already here with his terrible head!\nYou're fast. Here is your reward. Bye.", True, "Bye")
                            dbase.execute(f"UPDATE main SET gold = gold + 40 WHERE id_user=(SELECT id from users where name='{dbase.get_name()}')")
                            end = False

                        if troll_trust:
                            principal.window("And? Have you done?", True, "No, because troll said that\ntakes care of bridge and protects it.")
                            principal.window("Whatever, I'll get up few men from the village\nand we'll kill him ourselves.", False)

                            help_principal = answer(["Better not, the troll is big and will kill you with\none blow. Maybe I'll convince the troll to go away or at least\nlower the price", "Good luck! Bye."])

                            if help_principal == 1:
                                principal.window("Ok, you have last chance.\nIf you do it, I will pay you", True)
                                convince_troll = True
                                troll_trust = False

                            if help_principal == 2:
                                end = False

                        if fight_with_troll_2:
                            principal.window("I see you're not good at persuading. Here is your reward. Bye.", True, "Bye")
                            dbase.execute(f"UPDATE main SET gold = gold + 40 WHERE id_user=(SELECT id from users where name='{dbase.get_name()}')")
                            end = False

                        if lower_fee:
                            principal.window("And what? Did you get along with the troll?.", True, "Yes, I managed to convince him to cut the\nprice in half.")
                            principal.window("Well, it wasn't your job, but I won't complain.\nBut I'll have to give you half the reward", False)

                            kill_principal = answer(["You're kidding? Give me all the gold or I'll kill you", "Let it be that way, bye."])

                            if kill_principal == 1:
                                principal.window("Are you crazy?\n*Villager escapes and screams 'Help me!'*", True)
                                print("")
                                print("*You're chasing him*")
                                time.sleep(2)
                                print("")
                                print("*You enter an alley where you are surrounded by armed villagers*")
                                time.sleep(2)

                                principal.window("And what now psycho? Get him!", True)
                                Combat(character_statistics, weapon_statistics, *get_enemy('Armed Villagers'), 15).fight()

                                print("")
                                print("*You have collected 100 gold from the villagers*")
                                time.sleep(3)

                                dbase.execute(f"UPDATE main SET gold = gold + 100 WHERE id_user=(SELECT id from users where name='{dbase.get_name()}')")
                                end = False

                                

                            if kill_principal == 2:
                                dbase.execute(f"UPDATE main SET gold = gold + 20 WHERE id_user=(SELECT id from users where name='{dbase.get_name()}')")
                                end = False
                        
                        if do_nothing:
                            principal.window("And what? Did you get along with the troll?.", True, "No, I failed to convince him")
                            principal.window("Pff, you are useless. Bye", True, "Bye")
                            end = False
                    
                    #Market
                    if place == 2:
                        print("You can hear arguing merchants and a dog barking...")
                        time.sleep(2)

                    #Bridge
                    if place == 3:
                        print("*You are walking towards the bridge.*")
                        time.sleep(2)
                        if troll_visit == False:
                            print("")
                            print("You can hear the troll singing in the distance.")
                            print("")
                            time.sleep(3)

                            print("Troll: Tralala! Lala! Lalala! Hey ho! Hey ho! Lala...")
                            time.sleep(3)

                            print('-'*55)
                            print('Bridge'.center(55))
                            print('-'*55)

                            troll.window("Hey stranger!", True, "Hello. I heared that you want gold for\npassage, the locals don't like it.")

                            troll.window("Ha ha ha ha! I don't give shit to locals!\nI care of this bridge, I restore it and defend it\nagainst bandits and monsters.", False)
                            time.sleep(3.5)

                            kill_troll = answer(["And I don't care, I have a contract on you,\nso you'll either leave this place or\nI'll have to kill you.", "Maybe you're right,\nI will go back to my principal and ask him."])

                            if kill_troll == 1:
                                troll.window("Ha! You're not the first to want to get rid of me!\nStand to fight!", True)
                                Combat(character_statistics, weapon_statistics, *get_enemy('Troll')).fight()
                                fight_with_troll = True
                                troll_visit = True

                            if kill_troll == 2:
                                troll.window("You surprised me.\nI thought you were going to kill me.", True, "You are lucky!")
                                troll_trust = True
                                troll_visit = True

                        elif convince_troll:
                            troll.window("Oh, it's you again.", True, "Hello again. Can you leave this place?\nIf you don't, villagers will kill you")

                            troll.window("I told you I don't go anywhere", False)

                            kill_troll_2 = answer(["Okay, my patience is over. This is your last chance.\nLeave this place or I'll kill you", "Okay, okay, but maybe at least reduce the fee?", "Okay, so goodbye"])

                            if kill_troll_2 == 1:
                                troll.window("Ha! You're not the first to want to get rid of me!\nStand to fight!", True)
                                Combat(character_statistics, weapon_statistics, *get_enemy('Troll')).fight()
                                fight_with_troll_2 = True

                            if kill_troll_2 == 2:
                                troll.window("In fact, I have a lot of gold anyway,\nso I can lower the fee to 5 gold", True, "I'm glad you agreed. The villagers\nshouldn't attack you")
                                lower_fee = True
                                convince_troll = False


                            if kill_troll_2 == 3:
                                do_nothing = True
                                convince_troll = False
                        
                        elif fight_with_troll or fight_with_troll_2:
                            print("You have nothing to do here,\nyou only see the body of the troll and the blood")
                            time.sleep(3)

                        else:
                            troll.window("Oh, it's you again. Do you want to cross the bridge?.", True, "No, I'm just looking around.")

            
            print("")
            print("-" * 55)
            print("You completed the prologue!".center(55))
            print("Now you can repeat it or fight in the arena".center(55))
            print("-" * 55)
            time.sleep(5)

        if menu == 2:
            print('-' * 55)
            print('Arena'.center(55))
            print('-' * 55)

            monsters = [x['name'] for x in list_of_enemies]

            while True:
                option = answer(["Fight", 'Exit'])

                if option == 1:
                    monster_index = random.randint(0, len(monsters) - 1)
                    number_of_monster = random.randint(1, 5)

                    Combat(character_statistics, weapon_statistics, *get_enemy(monsters[monster_index]), number_of_monster).fight(arena = True)

                    print('-' * 40)

                if option == 2:
                    break

        if menu == 3:
            dbase.close()
            quit()


if __name__ == '__main__':
    main()