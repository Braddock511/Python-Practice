import time
import random
import pyttsx3 as pt

file=open('D:\Programowanie\Programy\projekty\LearnWords\Words.txt','r+')
words=file.read().split("\n")
words.remove("")

class learn():
    idk=[]
    dec=3

    def how_many(self):
        try:
            self.dec= int(input("Enter value: "))
        except ValueError:
            print("")
            print("Enter a number!")
            time.sleep(.5)

    #pisanie slowek
    def spelling(self):
        score=0
        for _ in range(self.dec):
            random_words=random.choice(words)
            guess=random_words.split("-")
            random.shuffle(guess)
            print("------------")
            print('\033[1m'+guess[0]+'\033[0m')
            print("------------")
            odp=input("Enter the translation: ")
            if odp==guess[1].lower():
                print("============")
                print("\033[1mCorrect\033[0m")
                print("============")
                score+=1
                #usuwa słowka z idk na ktore dobrze odpowiedziano
                if random_words in self.idk:
                    self.idk.remove(random_words)
            else:
                print("============")
                print(f"\033[1mWrong | Correct is {guess[1].lower()}\033[0m")
                print("============")
                #dodaje słowka na ktore zle odpowiedziano
                if self.idk.count(random_words)!=1:
                    self.idk.append("-".join(guess))

        print(f"Your score: {str(score)}/{str(self.dec)}")
        time.sleep(1)
        
            

    #dodwanie slowek do pliku ze slowkami
    def add(self):
        pl = input("Add polish word: ")
        eng = input("Add a translation of the word: ")
        file.write(f'{pl}-{eng}\n')
        words.append(f'{pl}-{eng}')
        file.close()

    
    #pokazywanie slowek z pliku ze slowkami
    def show(self):
        print("")
        while True:
            for index,ele in enumerate(words):
                print(f'{index}. {ele}')
            print("")
            odp=input("Press enter to exit ")
            if odp=="":
                break
            else:
                break
    
    #usuwanie slowek z pliku ze slowkami
    def remove(self):
        print("")
        while True:
            for index,ele in enumerate(words):
                print(f'{index}. {ele}')
            print("")
            odp=int(input("Enter number of word which you would remove: "))
            for index,ele in enumerate(words):
                if index==odp:
                    words.remove(words[index])
                    file.seek(0)
                    file.truncate(0)
                    file.write("\n".join(words)+"\n")
                    file.close()
            break

    #wybieranie
    def selection(self):
        score = 0
        for _ in range(self.dec):
            random_words = [words[random.randint(0,len(words)-1)] for _ in range(4)]
            guess= random_words[0].split('-')
            rest = [x.split('-') for x in random_words[1:]]
            all = rest+[guess]
            random.shuffle(all)

            dont_know = "-".join(guess)
            try:
                print("------------")
                print('\033[1m'+guess[1]+'\033[0m')
                print("------------")
                print(f'1.{all[0][0]}') 
                print(f'2.{all[1][0]}') 
                print(f'3.{all[2][0]}') 
                print(f'4.{all[3][0]}') 
                print("")
                odp = int(input('Choose answer: '))
                print("")

                if odp==1:
                    if all[0][0]==guess[0]:
                        print("============")
                        print("\033[1mCorrect\033[0m")
                        print("============")
                        score+=1
                        if dont_know in self.idk:
                            self.idk.remove(dont_know)
                    else:
                        print("============")
                        print(f"\033[1mWrong | Correct is {guess[0]}\033[0m")
                        print("============")
                        if self.idk.count(dont_know)!=1:
                            self.idk.append(dont_know)
                        time.sleep(.5)

                if odp==2:
                    if all[1][0]==guess[0]:
                        print("============")
                        print("\033[1mCorrect\033[0m")
                        print("============")
                        score+=1
                        if dont_know in self.idk:
                            self.idk.remove(dont_know)
                    else:
                        print("============")
                        print(f"\033[1mWrong | Correct is {guess[0]}\033[0m")
                        print("============")
                        if self.idk.count(dont_know)!=1:
                            self.idk.append(dont_know)
                        time.sleep(.5)

                if odp==3:
                    if all[2][0]==guess[0]:
                        print("============")
                        print("\033[1mCorrect\033[0m")
                        print("============")
                        score+=1
                        if dont_know in self.idk:
                            self.idk.remove(dont_know)
                    else:
                        print("============")
                        print(f"\033[1mWrong | Correct is {guess[0]}\033[0m")
                        print("============")
                        if self.idk.count(dont_know)!=1:
                            self.idk.append(dont_know)
                        time.sleep(.5)

                if odp==4:
                    if all[3][0]==guess[0]:
                        print("============")
                        print("\033[1mCorrect\033[0m")
                        print("============")
                        score+=1
                        if dont_know in self.idk:
                            self.idk.remove(dont_know)
                    else:
                        print("============")
                        print(f"\033[1mWrong | Correct is {guess[0]}\033[0m")
                        print("============")
                        if self.idk.count(dont_know)!=1:
                            self.idk.append(dont_know)
                        time.sleep(.5)
            except ValueError:
                print("")
                print("Enter a number!")
                time.sleep(.5)

            
        print(f"Your score: {score}/{self.dec}")
        time.sleep(1)

    #wymowa
    def pronunciation(self):
        print(312) 
            
        
    def __init__(self):
        #Menu główne

        print("")
        print("Hello in learn english words program!")
        while True:
            print("")
            print("1. Spelling")
            print("2. Selection")
            print("3. Pronunciation")
            print("4. Add words")
            print("5. Remove words")
            print("6. Show words")
            print("7. Show words which you don't know")
            print("8. How many times would you like to repeat (Standard value is 3)")
            print("9. Exit")
            print("")
            
            try:
                option=int(input("Choose option 1-9: "))
                if option==1:
                    self.spelling()
                if option==2:
                    self.selection()
                if option==3:
                    self.pronunciation()
                if option==4:
                    self.add()
                if option==5:
                   self.remove()
                if option==6:
                    self.show()
                if option==7:
                    if self.idk==[]:
                        print("")
                        print("You know all the words!")
                        time.sleep(.5)
                    else:
                        while True:
                            print("")
                            print("\n".join(self.idk))
                            print("")
                            odp=input("Press enter to exit ")
                            if odp=="":
                                break
                            else:
                                break
                if option==8:
                    self.how_many()
                if option==9:
                    exit()
                
            except ValueError:
                print("")
                print("Enter a number!")
                time.sleep(.5)

    
first = learn()

#dodanie trybu głosowego
