import random
def PSR():
    win_phrase=['woo, you destroyed it!', 'Well done, human','The machine has been defeted! Good job.','You win!!' ]
    lose_phrase=['Poor human, you cannot do anything against the machines.', 'You have been defeted','Ah-ah-ah you have lost so badly!','You lose!! Try agin if you dare', ]
    want_to_play=['Great','You are feeling brave','Wow, that is fantastic', 'Are you sure?' ]
    user_choice = input("Welcome to the duel! Do you want to compete with the most intelligent and advanced machine ? y / n ")

    wapons=['Rock' , 'Paper','Scissors']
    if user_choice =='y':
        print( random.choice(want_to_play))
        wu=input( "State you wapon: Rock (r), Paper (p) or Scissors (s).  ")
    def translate(i):
        if i =='r':
            j='Rock'
        elif   i =='p': 
            j='Paper'
        elif  i=='s':
            j='Scissors'
        else:
            j=None
        return j    
    i=0
    while translate(wu) in wapons:
        computer=random.choice(wapons)
        print("\n-----------------------------")
        print('GAME #', i)
        print("You vs Computer")
        print( translate(wu) +' X '+computer)
        print("------------------------------\n")    
            
        if wu=='p':
            if computer==translate('r'): print(random.choice(win_phrase))
            elif computer==translate('p'): print('Parity! You did lose, but neither did the computer.')
            else: 
                print(random.choice(lose_phrase))  
                wu=None  
        if wu=='r':
            if computer==translate('s'): print(random.choice(win_phrase))
            elif computer==translate('r'): print('Parity! You did lose, but neither did the computer.')
            else: 
                print(random.choice(lose_phrase)) 
                wu=None
        if wu=='s':
            if computer==translate('p'): print(random.choice(win_phrase))
            elif computer==translate('s'): print('Parity! You did lose, but neither did the computer.')
            else:
                print(random.choice(lose_phrase)) 
                wu=None 
        if wu is not None:           
            wu=input( "\nState you wapon or leave the game: ")
        i=i+1

if __name__ == "__main__":
    PSR()