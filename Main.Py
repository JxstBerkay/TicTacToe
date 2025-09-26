Board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

playertable = ["X","O"]

currentindex = 0

Flag = True

Movecounter = 0 #Keeping track of The Moves
def printboard(board):
    print([board[0],board[1],board[2]])
    print([board[3],board[4],board[5]])
    print([board[6],board[7],board[8]])

def windetection(board):
    #vertical detection
    global Flag

    

    if board[0] == board[1] == board[2] and board[2] != "-":
        print(f"{playertable[currentindex]} WON!")
        Flag = False
    elif  board[3] == board[4] == board[5] and board[4] != "-":
         print(f"{playertable[currentindex]} WON!")
         Flag = False
    elif  board[6] == board[7] == board[8] and board[7] != "-": 
         print(f"{playertable[currentindex]} WON!")
         Flag = False

    #horizontal detection
    elif board[0] == board[3] == board[6] and board[3] != "-":
        print(f"{playertable[currentindex]} WON!")
        Flag = False
    elif  board[1] == board[4] == board[7] and board[4] != "-":
         print(f"{playertable[currentindex]} WON!")
         Flag = False
    elif  board[2] == board[5] == board[8] and board[8] != "-": 
         print(f"{playertable[currentindex]} WON!")
         Flag = False
    #iDiagonal Detection
    elif board[0] == board[4] == board[8] and board[4] != "-":
        print(f"{playertable[currentindex]} WON!")
        Flag = False
    elif  board[6] == board[4] == board[2] and board[4] != "-":
         print(f"{playertable[currentindex]} WON!")
         Flag = False
    
    if Movecounter == 9 and Flag == True:
        print(f"No One Won.")
        Flag = False
    

printboard(Board)

while Flag:
    if currentindex >= 2:
        currentindex = 0
    plrinput = int(input(f"Its The Turn Of {playertable[currentindex]} ") )
    

    if plrinput <= 9 and plrinput >= 0:
        if Board[plrinput -1] == "-":
            Movecounter += 1
            Board[plrinput -1 ] = playertable[currentindex]
            printboard(Board)
            windetection(Board)
            currentindex += 1

