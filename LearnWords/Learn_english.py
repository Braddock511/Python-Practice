import time
import random
import pyttsx3 as pt

file=open('LearnWords/words.txt','r+')

words=file.read().split("\n")
words.remove("")

class LearnWords():
    idk=[]
    dec=3

    def how_many(self):
        self.dec = int(input("Enter value: "))

    #spelling words
    def spelling(self):
        score=0

        for _ in range(self.dec):
            random_words=random.choice(words)
            guess=random_words.split("-")
            random.shuffle(guess)

            print("------------")
            print('\033[1m'+guess[0]+'\033[0m')
            print("------------")
            odp = input("Enter the translation: ")

            if odp == guess[1].lower():
                print("============")
                print("\033[1mCorrect\033[0m")
                print("============")
                score+=1

                #removes words from idk that were well answered
                if random_words in self.idk:
                    self.idk.remove(random_words)

            else:
                print("============")
                print(f"\033[1mWrong | Correct is {guess[1].lower()}\033[0m")
                print("============")

                #adds words that were wrongly answered
                if self.idk.count(random_words)!=1:
                    self.idk.append("-".join(guess))

        print(f"Your score: {str(score)}/{str(self.dec)}")
        time.sleep(1)
        
            

    #adding words to a word file
    def add(self):
        pl = input("Add polish word: ")
        eng = input("Add a translation of the word: ")
        file.write(f'{pl}-{eng}\n')
        words.append(f'{pl}-{eng}')
        file.close()

    
    #showing words from a word file
    def show(self):
        print("")
        while True:
            for index, element in enumerate(words):
                print(f'{index+1}. {element}')
            print("")
            input("Press enter to exit ")
            break
    
    #deleting words from the word file
    def remove(self):
        print("")
        while True:
            for index, element in enumerate(words):
                print(f'{index}. {element}')

            print("")
            odp = int(input("Enter number of word which you would remove: "))

            for index, element in enumerate(words):
                if index == odp:
                    words.remove(words[index])
                    file.seek(0)
                    file.truncate(0)
                    file.write("\n".join(words)+"\n")
                    file.close()
            break

    #select ansewers
    def selection(self):
        score = 0

        for _ in range(self.dec):
            random_words = [words[random.randint(0,len(words)-1)] for _ in range(4)]
            guess = random_words[0].split('-')
            rest = [x.split('-') for x in random_words[1:]]
            all = rest+[guess]
            random.shuffle(all)

            dont_know = "-".join(guess)
            try:
                print("------------")
                print('\033[1m'+guess[1]+'\033[0m')
                print("------------")
                print(f'1. {all[0][0]}') 
                print(f'2. {all[1][0]}') 
                print(f'3. {all[2][0]}') 
                print(f'4. {all[3][0]}') 
                print("")

                odp = int(input('Choose answer: '))
                print("")

                match odp:
                    case 1:
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

                    case 2:
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

                    case 3:
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

                    case 4:
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

    #pronunciation
    def pronunciation(self):
        print(312) 
            
        
    def __init__(self):
        #Menu
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
                option = int(input("Choose option 1-9: "))

                match option:
                    case 1:
                        self.spelling()

                    case 2:
                        self.selection()

                    case 3:
                        self.pronunciation()

                    case 4:
                        self.add()

                    case 5:
                        self.remove()

                    case 6:
                        self.show()

                    case 7:
                        if self.idk==[]:
                            print("")
                            print("You know all the words!")
                            time.sleep(.5)

                        else:
                            while True:
                                print("")
                                print("\n".join(self.idk))
                                print("")
                                input("Press enter to exit ")
                                break

                    case 8:
                        self.how_many()

                    case 9:
                        exit()
                
            except ValueError:
                print("")
                print("Enter a number!")
                time.sleep(.5)

    
learn = LearnWords()

#add voice mode