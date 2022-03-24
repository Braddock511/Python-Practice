import time
import pymysql as sql
from Login import *

def main():
    #zrobic logowanie (zmienna name nie od razu jest zapisywana w tabeli users, przez co nie można wpisać danych do tabeli main)
    con = sql.Connect(host='127.0.0.1', unix_socket='', user='root', password='', db='dbgame') 
    db = con.cursor() 
    log = Login(con, db)
    gold = 0
    
    #Loading data
    query = 'SELECT * FROM characters WHERE id=1;'

    character_statistics = {'id':'','name':'','hp':'','damage':'','agility':'','intelligence':'','speed':''}

    db.execute(query)

    for x in db:
        counter=0
        for keys in character_statistics.keys():
            character_statistics[keys]=x[counter]
            counter+=1
            

    query2 = 'SELECT id, name, attack, speed_attack, weight FROM weapons WHERE id=1;'

    weapon_statistics = {'id':'','name':'','attack':'','speed_attack':'','weight':''}

    db.execute(query2)

    for x in db:
        counter=0
        for keys in character_statistics.keys():
            weapon_statistics[keys]=x[counter]
            counter+=1
        

    print(character_statistics)
    print(weapon_statistics)



    # print('Welcome in Adventure Game!')
    # print("")
    # acc = input('Do you have account? (Y/N) ')
    # if acc.upper()=='Y':
    #     log.login()
    # elif acc.upper()=='N':
    #     log.register()
    #     log.add_to_main()
    
    
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
        pass

main()