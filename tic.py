import random
#Create a dictionary
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|'+board['mid-M']+'|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|'+board['low-M']+'|' + board['low-R'])
printBoard(theBoard)
def isWinner(board,turn):
    if not board['top-L']==' ' and board['top-L']==board['top-M'] and not board['top-M']==' ' and board['top-M']==board['top-R']:
        print(board['top-L']+ " Is the Winner")
        return True
    elif not board['mid-L']==' ' and board['mid-L']==board['mid-M'] and not board['mid-M']==' ' and board['mid-M']==board['mid-R']:
        print(board['mid-L']+ " Is the Winner")
        return True
        
    elif not board['low-L'] == ' ' and board['low-L']==board['low-M'] and not board['low-M'] == ' ' and board['low-M']==board['low-R']:
        print(board['low-L']+ " Is the Winner")
        return True
    elif not board['top-L']==' ' and board['top-L']==board['mid-L'] and not board['mid-L']==' ' and board['mid-L']==board['low-L']:
        print(board['top-L']+ " Is the Winner")
        return True
    elif not board['top-M']==' ' and board['top-M']==board['mid-M'] and not board['mid-M']==' ' and board['mid-M']==board['low-M']:
        print(board['top-M']+ " Is the Winner")
        return True
    
    elif not board['top-R']==' ' and board['top-R']==board['mid-R'] and not board['mid-R']==' ' and board['mid-R']==board['low-R']:
        print(board['top-R']+ " Is the Winner")
        return True
    
    #     Digonals check
    elif not board['top-L']==' ' and board['top-L']==board['mid-M'] and not board['mid-M']==' ' and board['mid-M']==board['low-R']:
        print(board['top-L']+ " Is the Winner")
        return True
    
    elif not board['top-R']==' ' and board['top-R']==board['mid-M'] and not board['mid-M']==' ' and board['mid-M']==board['low-L']:
        print(board['top-R']+ " Is the Winner")
        return True

def resetBoard(board):
    for k in board.keys():
        board[k]=' '
resetBoard(theBoard)
#Let's take two players
players = ['X','O']
turn = random.choice(players)
for i in range(9):
    print("Turn for "+turn+ ". Which place you want go?")
    print("Your choices are :")
    for k in theBoard.keys():
        if theBoard[k]== ' ':
            print(k,end=" ")
    move = input()     
    if move not in theBoard.keys():
        print("Incorrect Move")
    theBoard[move] = turn 
    printBoard(theBoard)
    isWon = isWinner(theBoard,turn)     
    if isWon:
        print("Congratulations!!")
        #If someone is winner then reset the board for the next game
        resetBoard(theBoard)
        break
    if turn=='X':
        turn = 'O'
    else:
        turn = 'X'
    
    if i==8:
        print("Match draw!!")
