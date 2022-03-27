import time
from Database import *
from Combat import *

def main():
    dbase = Db(host="localhost", port = 5432, db="postgres", user="postgres", password="123")

    print('Welcome in Adventure Game!')
    print("")
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

    #Loading data
    character_statistics = {'name':'','hp':'','damage':'','agility':'','intelligence':'','speed':''}

    character = dbase.execute(f"SELECT name, hp, damage, agility, intelligence, speed FROM characters WHERE name='{stats[0][1]}'")

    for i, keys in enumerate(character_statistics.keys()):
        character_statistics[keys] = character[i]


    weapon_statistics = {'name':'','attack':'','speed_attack':'','weight':''}

    weapon = dbase.execute(f"SELECT name, attack, speed_attack, weight FROM weapons WHERE name='{stats[1][2]}'")

    for i, keys in enumerate(weapon_statistics.keys()):
        weapon_statistics[keys] = weapon[i]
    
    combat = Combat(character_statistics, weapon_statistics, {'id': 1, 'name': 'Troll', 'hp': 1000, 'attack': 10, 'dodge': 30})

    combat.show_statistics()

    #story
    # print('-'*20)
    # print('So you picked your hero, now you can go to conquer new land!')
    # time.sleep(2.5)
    # print("But you can't, because...")
    # time.sleep(2)
    # print('You are poor and you have 0 gold, so you need take a contract on a monster!')
    # time.sleep(2.5)
    # print('-'*20)
    # input('Press enter to continue ')

    # print('You are in village, you see board with orders')
    # time.sleep(2.5)
    # print('You have 2 options: ')
    # time.sleep(1)
    # print("")
    # print('1. Take a contract in which you have to solve riddle in village')
    # print('2. Take a contract in which you have to regain treasure of rich resident from village')
    # print('-'*20)
    # answer = int(input('Choose: '))
        
        
if __name__ == '__main__':
    main()
