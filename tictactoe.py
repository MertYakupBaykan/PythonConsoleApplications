running = bool
running = True
p1_turn = bool
playing = bool
player1_is_x = bool
count = 0
p1_sign = ''
p2_sign = ''
board = [1,2,3,4,5,6,7,8,9]
def display_board(board):
    print(board[0],'|',board[1],'|',board[2])
    print('----------')
    print(board[3],'|',board[4],'|',board[5])
    print('----------')
    print(board[6],'|',board[7],'|',board[8])
print('Tick Tac Toe')
print('Board Positions')
display_board(board)
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
while running == True:
    xoro = str(input('Do you want to be X or O ? (x/o) '))
    if xoro.lower() == 'x':
        p1_sign = 'X'
        p2_sign = 'O'
        print('Player one is: X')
        print('Player two is: O')
        player1_is_x = True
    else:
        p1_sign = 'O'
        p2_sign = 'X'
        print('Player one is: O')
        print('Player two is: X')
        player1_is_x = False

    playing = True    
    p1_turn = True    
    while playing == True:
        for each in board:
             if each == p1_sign or each == p2_sign:
                    if each == board[0] and each == board[1] and each == board[2]:
                        if each == p1_sign:
                            print('P1 had won the Game')
                            playing = False
                            break
                        else:
                            print('P2 had won the Game')
                            playing = False
                            break
                    elif each == board[3] and each == board[4] and each == board[5]:
                        if each == p1_sign:
                            print('P1 had won the Game')
                            playing = False
                            break
                        else:
                            print('P2 had won the Game')
                            playing = False
                            break
                    elif each == board[6] and each == board[7] and each == board[8]:
                        if each == p1_sign:
                            print('P1 had won the Game')
                            playing = False
                        else:
                            print('P2 had won the Game')
                            playing = False
                    elif each == board[8] and each == board[4] and each == board[0]:
                        if each == p1_sign:
                            print('P1 had won the Game')
                            playing = False
                            break
                        else:
                            print('P2 had won the Game')
                            playing = False
                            break
                    elif each == board[0] and each == board[4] and each == board[8]:
                        if each == p1_sign:
                            print('P1 had won the Game')
                            playing = False
                            break
                        else:
                            print('P2 had won the Game')
                            playing = False
                            break
                    elif each == board[0] and each == board[3] and each == board[6]:
                        if each == p1_sign:
                            print('P1 had won the Game')
                            playing = False
                            break
                        else:
                            print('P2 had won the Game') 
                            playing = False
                            break
                    elif each == board[1] and each == board[4] and each == board[7]:
                        if each == p1_sign:
                            print('P1 had won the Game')
                            playing = False
                            break
                        else:
                            print('P2 had won the Game') 
                            playing = False
                            break
                    elif each == board[2] and each == board[5] and each == board[8]:
                        if each == p1_sign:
                            print('P1 had won the Game')
                            playing = False
                            break
                        else:
                            print('P2 had won the Game')
                            playing = False
                            break
                    elif each == board[2] and each == board[4] and each == board[6]:
                        if each == p1_sign:
                            print('P1 had won the Game')
                            playing = False
                            break
                        else:
                            print('P2 had won the Game')
                            playing = False
                            break        
                    else :
                        continue
        if p1_turn == True and playing == True and count < 9:
            pos =int(input('(P1) Chose your next position(1-9)'))
            if pos <= 9:
                if board[pos-1] == ' ':
                    board[pos-1]=p1_sign
                    count += 1
                    display_board(board)
                    p1_turn = False
                else:
                    print('Position is Occupied')
                    pass
            else:
                print('Please enter a value between 1-9')
                pass
        elif p1_turn == False and playing == True and count < 9:
            pos =int(input('(P2) Chose your next position(1-9)'))
            if pos <= 9:
                if board[pos-1] == ' '  :
                    board[pos-1]=p2_sign
                    count += 1
                    display_board(board)
                    p1_turn = True
                else:
                    print('Position is Occupied')
                    pass
            else:
                print('Please enter a value between 1-9')
                pass  
        elif playing == True and count == 9:
            print('Tie')
            playing = False
            
        else:
            break
    
    if playing == False:
        decision = input('Do you wanna Play again? (y/n)')
        if decision.lower() ==  'y':
            count = 0
            board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            continue
        elif decision.lower()=='n' :
            
            break
        else:
            break
            