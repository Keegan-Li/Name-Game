def modeOne(name):
#prints new name that is the truncation of the inputted name to the number of letters the player chooses
    counter = 0
    print('how many times do you want to play this game?')
    
    gameLimit = input()
    gameLimit = int(gameLimit)
    
    for counter in range(gameLimit):
        counter += 1
        print('choose a number between 1 and ' , len(name))
        number = input()
        number = int(number)
        
        while number > len(name):
            print('This number is too large. Choose one between 1 and ', len(name), ' or you cannot proceed')
            number = input()
            number = int(number)

        print('Your new name is ', name[0:number])
        
    if gameLimit == 1:
        print('You have completed the single round of the game.')
    else:
        print('You have completed all ' , gameLimit, ' rounds of the game.')
    
def modeTwo(name):
    print('This is not a game mode, just watch it play out. Type ok')
    response = input()
    counterTwo = len(name)
    
    while response != 'ok':
        print('You did not type "ok", please try again or may not proceed with the game.')
        response = input()
    
    for counterTwo in range(len(name)+1):
        counterTwo -= 1
        print(name[0:counterTwo])
        
    print('Thank you for playing')
    
def modeThree(name):
    print('This is not a game mode, just watch it play out. Type ok')
    responseTwo = input()
    
    while responseTwo != 'ok':
        print('You did not type "ok", please try again or may not proceed with the game.')
        responseTwo = input()
    
    counterThree = int(len(name))
    
    for counterThree in range(len(name)+1):
        counterThree -= 1
        print(name[0 : len(name)-counterThree])
        
    print('Thank you for playing')
    
def Main():
    print('Please type your name')
    name = input()
    print('Nice you meet you, ', name, '. Would you like to play mode 1 of this game or mode 2 or mode 3? Just type the number')
    gameMode = input()
    gameMode = int(gameMode)
    if gameMode == 1:
        modeOne(name)
    
    elif gameMode == 2:
        modeTwo(name)
    
    elif gameMode == 3:
        modeThree(name)
    
    else:
        print('That is not an available game mode')
#Defining functions

Main()

