import random

word_list = list()
with open("words.txt","r") as f:
    word_list.append(f.read())
    word_list = word_list[0].split("\n")
word = random.choice(word_list)

def hangman(word = "list"):
    print("Welcome to hangman!")
    
    stages = ["-----------",
              "|          |",
              "|          o",
              "|         \|/",
              "|          |",
              "|         / \ ",
              "|",
              "|",
              "-------------------"]
    for _ in stages:
        print(_)
    print("Word for you is of "+str(len(word))+ " letters\n") 

    block = ["__"]*len(word)
    remaining_word = list(word)
    correct_word = list(word)
    wrong = 0
    win = False
    current_stage = list()
    
    while wrong<5:
        guess = input("Guess a letter!\t")
        current_list = stages[0:wrong+1]
  
        if guess in correct_word:
            print("You guessed correctly!")
            ind = correct_word.index(guess)
            block[ind] = guess
            if guess in remaining_word:
                wrong += 1
                print("You already guessed that letter!:\n")
                break
            remaining_word[ind] = "$"
            print("\n")
            print(block)
            print("\n")
            for _ in current_list:
                print(_)
            print("\n")
            print("\n")
        else:
            print("That is incorrect!")
            wrong += 1
            print("\n")
            print(block)
            print("\n")
            for _ in current_list:
                print(_)
            print("\n")
            print("\n")
        if "__"  not in block:
            print("Congrats! You guessed it.")
            print("The word is \"{}\"\n".format(word))
            
            break

    if wrong == 5:
        print("You lost!")
        print("The correct word is \"{}\"".format(word))
        for _ in stages:
            print(_)
    
    
    


            
              
              
              
              
              

