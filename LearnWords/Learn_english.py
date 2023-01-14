import time
import random
# import pyttsx3 as pt

file = open('words.txt','r+')

words = file.read().split("\n")
words.remove("")

class LearnWords():
    idk = []
    dec = 3

    def how_many(self):
        self.dec = int(input("Enter value: "))

    def spelling(self):
        score = 0
        for _ in range(self.dec):
            # choose a random word from the list
            random_word = random.choice(words)
            word, translation = random_word.split("-")

            # print the word to guess
            print("------------")
            print(f'\033[1m{word}\033[0m')
            print("------------")
            user_answer = input("Enter the translation: ")

            # check if the answer is correct
            if user_answer == translation.lower():
                print("============")
                print("\033[1mCorrect\033[0m")
                print("============")
                score += 1
                if random_word in self.idk:
                    self.idk.remove(random_word) # remove correctly answered word from self.idk
            else:
                print("============")
                print(f"\033[1mWrong | Correct is {translation.lower()}\033[0m")
                print("============")
                if self.idk.count(random_word) != 1:
                    self.idk.append(random_word) # add incorrectly answered word to self.idk

        # print final score
        print(f"Your score: {score}/{self.dec}")
        time.sleep(1)
        
            

    def add_word(self):
        pl = input("Add polish word: ")
        eng = input("Add a translation of the word: ")
        
        # write the word and its translation to a file
        with open('words.txt', 'a') as f:
            f.write(f'{pl}-{eng}\n')
        
        # add the word and its translation to the list
        words.append(f'{pl}-{eng}')

    
    def show_words(self):
        for index, element in enumerate(words):
            print(f'{index+1}. {element}')
        
        print("\n")
        input("Press enter to exit ")

    
    def remove_word(self):
        for index, element in enumerate(words):
            print(f'{index+1}. {element}')

        # prompt user for word to remove
        print("\n")
        user_index = int(input("Enter number of word which you would remove: "))

        for index, element in enumerate(words):
            if index+1 == user_index:
                words.remove(words[index])
                # open file and truncate it
                with open('words.txt', 'w') as f:
                    f.write("\n".join(words)+"\n")

    def selection(self):
        score = 0

        for _ in range(self.dec):
            # select 4 random words and split them into word and translation
            random_words = [words[random.randint(0,len(words)-1)] for _ in range(4)]
            guess = random_words[0].split('-')
            rest = [x.split('-') for x in random_words[1:]]
            all = rest+[guess]
            random.shuffle(all)

            dont_know = "-".join(guess)
            try:
                # print the word to guess and the options
                print("------------")
                print(f'\033[1m{guess[0]}\033[0m')
                print("------------")
                print(f'1. {all[0][1]}') 
                print(f'2. {all[1][1]}') 
                print(f'3. {all[2][1]}') 
                print(f'4. {all[3][1]}') 
                print("")

                user_answer = int(input('Choose answer: '))
                print("")
                
                # check if the answer is correct
                if user_answer == 1 and all[0][0] == guess[0]:
                    print("============")
                    print("\033[1mCorrect\033[0m")
                    print("============")
                    score += 1

                    if dont_know in self.idk:
                        self.idk.remove(dont_know)

                elif user_answer == 2 and all[1][0] == guess[0]:
                    print("============")
                    print("\033[1mCorrect\033[0m")
                    print("============")
                    score += 1

                    if dont_know in self.idk:
                        self.idk.remove(dont_know)

                elif user_answer == 3 and all[2][0] == guess[0]:
                    print("============")
                    print("\033[1mCorrect\033[0m")
                    print("============")
                    score += 1

                    if dont_know in self.idk:
                        self.idk.remove(dont_know)

                elif user_answer == 4 and all[3][0] == guess[0]:
                    print("============")
                    print("\033[1mCorrect\033[0m")
                    print("============")
                    score += 1

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
        print()
        print("Hello in learn english words program!")
        print()

        while True:
            print()
            print("1. Spelling")
            print("2. Selection")
            print("3. Pronunciation")
            print("4. Add words")
            print("5. Remove words")
            print("6. Show words")
            print("7. Show words which you don't know")
            print("8. How many times would you like to repeat (Standard value is 3)")
            print("9. Exit")
            print()

            try:
                option = int(input("Choose option 1-9: "))

                if option == 1:
                    self.spelling()

                elif option == 2:
                    self.selection()

                elif option == 3:
                    self.pronunciation()

                elif option == 4:
                    self.add_word()

                elif option == 5:
                    self.remove_word()

                elif option == 6:
                    self.show_words()

                elif option == 7:
                    if self.idk==[]:
                        print("You know all the words!")
                        time.sleep(.5)
                    else:
                        print("\n".join(self.idk))
                        input("Press enter to exit ")

                elif option == 8:
                    self.how_many()
                    
                elif option == 9:
                    exit()

                else:
                    print("Enter a valid number between 1 and 9")

            except ValueError:
                print("Enter a number!")
                time.sleep(.5)

    
learn = LearnWords()

#add voice mode