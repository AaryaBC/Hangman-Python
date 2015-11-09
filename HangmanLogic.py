y = """
    ________
           |
           |
           |
           |
           |
           |
           |
    -------------
    """
a = """
    ________
    |      |
    |      |
           |
           |
           |
           |
           |
    -------------
    """
b = """
    ________
    |      |
   (_)     |
           |
           |
           |
           |
           |
    -------------
    """
c = """
    ________
    |      |
   (_)     |
    |      |
    |      |
    |      |
           |
           |
    -------------
    """
d = """
    ________
    |      |
   (_)     |
  \ | /    |
   \|/     |
    |      |
           |
           |
    -------------
    """
e = """
    ________
    |      |
   (_)     |
  \ | /    |
   \|/     |
    |      |
   / \     |
  /   \    |
    -------------
    """

drawing = [y,a,b,c,d,e]
last = "no"
import random

def Game():
    with open("C:\\Users\\aarya\\Desktop\\Assignment\\CSCI\\Hangman\\wordsEn.txt") as f:
        word = (random.choice(list(f)))
    b = []
    c = []
    for i in range(len(word)-1):
        b.append("_")
    print(" ".join(b))

    def GuessWord(chances):

        while ("".join(b)) != word[0:len(word)-1].upper() and chances < 5:

            a = input("Guess an alphabet")
            a = a.lower()

            if a in c:
                print("You have already made that guess")
                
            elif word.find(a) != -1:
                i = 0
                
                while i < len(word):
                    if a == word[i]:
                        b[i] = a.upper()
                    i += 1
            
            else:
                print("Oops, not there.")
                chances += 1
            print("\n")    
            print(drawing[chances])
            c.append(a)
            print(" ".join(b))
            
            
        if chances == 5:
            print("YOU LOST!!!\n")
            print(word)
        else:
            print("YOU WON!!!")
            return
                
    GuessWord(0)

while last == "no":
    last = input("Do you want to quit?")
    last = last.lower()
    if last != "no":
        break
    Game()
            
            
        
