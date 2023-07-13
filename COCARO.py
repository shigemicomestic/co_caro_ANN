import datetime
import pygame
import pygame_menu
from tkinter import Tk,ttk,Button
from tkinter import messagebox

ActivePlayer = 1
p1 = []
p2 = []
b=[]
mov = 0
size = 0
win = False
mTimePassed = False
mBestMove = 0

def SetLayout(id,player_symbol):
    b[id-1].config(text= player_symbol)
    b[id-1].state(['disabled'])

def check_Size3():
    i=0
    while(i<9):
        if(i+1 in p1) and (i+2 in p1) and (i+3 in p1): 
            return 1
        
        if(i+1 in p2) and (i+2 in p2) and (i+3 in p2):
            return 2
        
        if(i==3):
            if((i-2 in p1) and (i+2 in p1) and (i+6 in p1)) or ((i in p1) and (i+2 in p1) and (i+4 in p1)):
                return 1
            
            if((i-2 in p2) and (i+2 in p2) and (i+6 in p2)) or ((i in p2) and (i+2 in p2) and (i+4 in p2)):
                return 2
        i+=3
        
    for i in range(1,4):
        if(i in p1) and (i+3 in p1) and (i+6 in p1): 
            return 1
        
        if(i in p2) and (i+3 in p2) and (i+6 in p2):
            return 2
    return -1

def check_Size5():
    i=0
    while(i<25):
        if(i+1 in p1) and (i+2 in p1) and (i+3 in p1) and (i+4 in p1) and (i+5 in p1): 
            return 1
        
        if(i+1 in p2) and (i+2 in p2) and (i+3 in p2) and (i+4 in p2) and (i+5 in p2):
            return 2
        
        if(i==5):
            if((i-4 in p1) and (i+2 in p1) and (i+6 in p1) and (i+14 in p1) and (i+21 in p1)) or \
                ((i in p1) and (i+4 in p1) and (i+8 in p1) and (i+12 in p1) and (i+16 in p1)):
                return 1
            
            if((i-4 in p2) and (i+2 in p2) and (i+6 in p2) and (i+14 in p2) and (i+21 in p2)) or \
                ((i in p2) and (i+4 in p2) and (i+8 in p2) and (i+12 in p2) and (i+16 in p2)):
                return 2
        i+=5
        
    for i in range(1,6):
        if(i in p1) and (i+5 in p1) and (i+10 in p1) and (i+15 in p1) and (i+20 in p1): 
            return 1
        
        if(i in p2) and (i+5 in p2) and (i+10 in p2) and (i+15 in p2) and (i+20 in p2): 
            return 2
    return -1

def check_Size10():
    i = 1
    posi_1 = []
    posi_2 = []
    while(i<100):
        x=i%10
        x+=i//10
        for j in range(6):
            posi_1.clear()
            posi_2.clear()
            x+=j*10
            for k in range(5):
                posi_1.append(i+j+k)
                posi_2.append(x+k*10)
            
            if all(item in p1 for item in posi_1) or all(item in p1 for item in posi_2):
                return 1
            
            if all(item in p2 for item in posi_1) or all(item in p2 for item in posi_2):
                return 2
        i+=10

    x_1 = 1
    x_2 = 10        
    posi_1.clear()
    posi_2.clear()
    for q in range(9):
        
        if q >4:
            if all(item in p1 for item in posi_1) or all(item in p1 for item in posi_2):
                return 1
            if all(item in p2 for item in posi_1) or all(item in p2 for item in posi_2):
                return 2
            posi_1.remove(posi_1[0])
            posi_2.remove(posi_2[0])
        posi_1.append(x_1)
        posi_2.append(x_2)
        x_1 += 11
        x_2 += 9
    
    for i in range(5,11):
        x_1=i
        posi_1.clear()
        for j in range(i-4):
            for k in range(5):
                posi_1.append(x_1)
                x_1+=9
            if all(item in p1 for item in posi_1):
                posi_1.remove(posi_1[0])
                return 1
            
            if all(item in p2 for item in posi_1):
                posi_1.remove(posi_1[0])
                return 2


    return -1



def CheckWinner():
    global mov
    winner = -1
    
    if mov > (size*2 -1) and (size == 3 or size == 5):
        if size==3:
            winner = check_Size3()
        else:
            winner = check_Size5()
    
    if mov > 9 and size == 10:
        winner = check_Size10()
            
    
    if winner ==1:
        messagebox.showinfo(title="Congratulations.",
            message="Player win!")
        Restart()
    elif winner ==2:
        messagebox.showinfo(title="GAMEOVER.",
            message="Bot win!")
        Restart()
    elif mov == size**2:
        messagebox.showinfo(title="Draw",
            message="Draw!!")
        Restart()

def checkDraw():
    i=1
    while(i<=size**2):
        if(i not in p1 and i not in p2):
            return False
        i+=1
    
    return True
    

def checkWhichMarkWon(player):
    i=0

    if size==3:
        while(i<size**2):
            if(i+1 in player) and (i+2 in player) and (i+3 in player):
                return True
            
            if(i==3):
                if((i-2 in player) and (i+2 in player) and (i+6 in player)) or ((i in player) and (i+2 in player) and (i+4 in player)):
                    return True
                
            i+=3
            
        for i in range(1,size+1):
            if(i in player) and (i+3 in player) and (i+6 in player): 
                return True

    elif size==5:
        while(i<size**2):
            if(i+1 in player) and (i+2 in player) and (i+3 in player) and (i+4 in player) and (i+5 in player): 
                return True
            
            if(i==5):
                if((i-4 in player) and (i+2 in player) and (i+6 in player) and (i+14 in player) and (i+21 in player)) or \
                    ((i in player) and (i+4 in player) and (i+8 in player) and (i+12 in player) and (i+16 in player)):
                    return True
                
            i+=5
            
        for i in range(1,size+1):
            if(i in player) and (i+5 in player) and (i+10 in player) and (i+15 in player) and (i+20 in player): 
                return True
    else:
        i = 1
        posi_1 = []
        posi_2 = []
        while(i<size**2):
            x=i%10
            x+=i//10
            for j in range(6):
                posi_1.clear()
                posi_2.clear()
                x+=j*10
                for k in range(5):
                    posi_1.append(i+j+k)
                    posi_2.append(x+k*10)
    
                if all(item in player for item in posi_1) or all(item in player for item in posi_2):
                    return True
            i+=10
    
        x_1 = 1
        x_2 = 10        
        posi_1.clear()
        posi_2.clear()
        for q in range(9):
            x_1 += 11
            x_2 += 9
            posi_1.append(x_1)
            posi_2.append(x_2)
        
        if all(item in player for item in posi_1) or all(item in player for item in posi_2):
            return True

        x_1 = 1
        x_2 = 10        
        posi_1.clear()
        posi_2.clear()
        for q in range(9):
            
            if q >4:
                if all(item in player for item in posi_1) or all(item in player for item in posi_2):
                    return True
                
                posi_1.remove(posi_1[0])
                posi_2.remove(posi_2[0])
            posi_1.append(x_1)
            posi_2.append(x_2)
            x_1 += 11
            x_2 += 9
        
        for i in range(5,11):
            x_1=i
            posi_1.clear()
            for j in range(i-4):
                for k in range(5):
                    posi_1.append(x_1)
                    x_1+=9
                if all(item in player for item in posi_1):
                    posi_1.remove(posi_1[0])
                    return True
                
    return False

def ButtonClick(id):
    global ActivePlayer
    global p1,p2
    global mov
    if(ActivePlayer ==1):
        SetLayout(id,"X")
        p1.append(id)
        mov +=1
        CheckWinner()
        ActivePlayer =2
        AutoPlay()
    elif(ActivePlayer==2):
        SetLayout(id,"O")
        p2.append(id)
        mov +=1
        CheckWinner()
        ActivePlayer =1
    

def AutoPlay():
    global mTimePassed
    startTime = datetime.datetime.now()
    endTime = startTime + datetime.timedelta(0, 1)
    depth = 1
    position = None
    mTimePassed = False
    while True:
        currentTime = datetime.datetime.now()
        if currentTime >= endTime:
            break
        best, position = minimax(depth, True, -10000000, 10000000, currentTime, endTime-currentTime)
        depth += 1

    if position is None:
        position = mBestMove

    ButtonClick(position)

def checkGameState():
    if checkWhichMarkWon(p1):
        return 1

    if checkWhichMarkWon(p2):
        return 2

    if checkDraw():
        return 0

    return -1

def genrate():
    possibleMoves = []
    for cell in range(size**2):
            if (cell+1 not in p1 and cell+1 not in p2):
                possibleMoves.append(cell+1)
            
    return possibleMoves


def calculateLine_Diagonal(direction):
    oSum = 0
    xSum = 0
    
    if direction == 0:
        posi = 1
        while posi <= size**2:
            if posi in p2:
                oSum += 1
            elif posi in p1:
                xSum += 1
            posi += size+1
        return oSum, xSum
    elif direction == 1:
        posi = size
        while posi < size**2:
            if posi in p2:
                oSum += 1
            elif posi in p1:
                xSum += 1
            posi += size-1
        return oSum, xSum
    
def calculateLine_Row(i):
    oSum = 0
    xSum = 0
    posi = i+1
    for j in range(size):
        if posi+i*3 in p2:
            oSum+=1
        elif posi+i*3 in p1:
            xSum+=1
    return oSum, xSum

def calculateLine_Column(i):
    oSum = 0
    xSum = 0
    posi = i*size
    for j in range(1,size+1):
        if posi+j in p2:
            oSum+=1
        elif posi+j in p1:
            xSum+=1
    return oSum, xSum

def getScore(oSum, xSum):
    score = 0
    if xSum == 0 and oSum != 0:
        if oSum == size:
            score += 11 ** (oSum - 1)
        score += 10 ** (oSum - 1)
    if oSum == 0 and xSum != 0:
        score += -(10 ** (xSum - 1))
    return score

def evaluate():
    score = 0
    for i in range(size):
        oSum, xSum = calculateLine_Row(i)
        score += getScore(oSum, xSum)
        oSum, xSum = calculateLine_Column(i)
        score += getScore(oSum, xSum)
    
    for i in range(2):
        oSum, xSum = calculateLine_Diagonal(i)
        score += getScore(oSum, xSum)
    return score

def minimax(depth, isMaximizing, alpha, beta, startTime, timeLimit):
    global mTimePassed
    global p1,p2
    global mBestMove
    moves = genrate()
    score = evaluate()
    position = None

    if datetime.datetime.now() - startTime >= timeLimit:
        mTimePassed = True

    if not moves or depth == 0 or mTimePassed:
        gameResult = checkGameState()
        if gameResult == 1:
            return -10**(size+1), position
        elif gameResult == 2:
            return 10**(size+1), position
        elif gameResult == 0:
            return 0, position

        return score, position

    if isMaximizing:
        for i in moves:
                p2.append(i)
                score, dummy = minimax(depth-1, not isMaximizing, alpha, beta, startTime, timeLimit)
                if score > alpha:
                    alpha = score
                    position = i
                    mBestMove = i

                p2.remove(i)
                if beta <= alpha:
                    break

        return alpha, position
    else:
        for i in moves:
            p1.append(i)
            score, dummy = minimax(depth-1, not isMaximizing, alpha, beta, startTime, timeLimit)
            if score < beta:
                beta = score
                position = i
                mBestMove = i
            p1.remove(i)
            if alpha >= beta:
                break

        return beta, position

def EnableAll():
    for i in b:
        i.config(text= " ")
        i.state(['!disabled'])
    
def Restart():
    global p1,p2,mov,ActivePlayer
    p1.clear(); p2.clear()
    mov,ActivePlayer = 0,1
    EnableAll()



def Size3():
    b[0].config(command = lambda : ButtonClick(1))
    b[1].config(command = lambda : ButtonClick(2))
    b[2].config(command = lambda : ButtonClick(3))
    b[3].config(command = lambda : ButtonClick(4))
    b[4].config(command = lambda : ButtonClick(5))
    b[5].config(command = lambda : ButtonClick(6))
    b[6].config(command = lambda : ButtonClick(7))
    b[7].config(command = lambda : ButtonClick(8))
    b[8].config(command = lambda : ButtonClick(9))

def Size5():
    b[0].config(command = lambda : ButtonClick(1))
    b[1].config(command = lambda : ButtonClick(2))
    b[2].config(command = lambda : ButtonClick(3))
    b[3].config(command = lambda : ButtonClick(4))
    b[4].config(command = lambda : ButtonClick(5))
    b[5].config(command = lambda : ButtonClick(6))
    b[6].config(command = lambda : ButtonClick(7))
    b[7].config(command = lambda : ButtonClick(8))
    b[8].config(command = lambda : ButtonClick(9))
    b[9].config(command = lambda : ButtonClick(10))
    b[10].config(command = lambda : ButtonClick(11))
    b[11].config(command = lambda : ButtonClick(12))
    b[12].config(command = lambda : ButtonClick(13))
    b[13].config(command = lambda : ButtonClick(14))
    b[14].config(command = lambda : ButtonClick(15))
    b[15].config(command = lambda : ButtonClick(16))
    b[16].config(command = lambda : ButtonClick(17))
    b[17].config(command = lambda : ButtonClick(18))
    b[18].config(command = lambda : ButtonClick(19))
    b[19].config(command = lambda : ButtonClick(20))
    b[20].config(command = lambda : ButtonClick(21))
    b[21].config(command = lambda : ButtonClick(22))
    b[22].config(command = lambda : ButtonClick(23))
    b[23].config(command = lambda : ButtonClick(24))
    b[24].config(command = lambda : ButtonClick(25))

def Size10():
    b[0].config(command = lambda : ButtonClick(1))
    b[1].config(command = lambda : ButtonClick(2))
    b[2].config(command = lambda : ButtonClick(3))
    b[3].config(command = lambda : ButtonClick(4))
    b[4].config(command = lambda : ButtonClick(5))
    b[5].config(command = lambda : ButtonClick(6))
    b[6].config(command = lambda : ButtonClick(7))
    b[7].config(command = lambda : ButtonClick(8))
    b[8].config(command = lambda : ButtonClick(9))
    b[9].config(command = lambda : ButtonClick(10))
    b[10].config(command = lambda : ButtonClick(11))
    b[11].config(command = lambda : ButtonClick(12))
    b[12].config(command = lambda : ButtonClick(13))
    b[13].config(command = lambda : ButtonClick(14))
    b[14].config(command = lambda : ButtonClick(15))
    b[15].config(command = lambda : ButtonClick(16))
    b[16].config(command = lambda : ButtonClick(17))
    b[17].config(command = lambda : ButtonClick(18))
    b[18].config(command = lambda : ButtonClick(19))
    b[19].config(command = lambda : ButtonClick(20))
    b[20].config(command = lambda : ButtonClick(21))
    b[21].config(command = lambda : ButtonClick(22))
    b[22].config(command = lambda : ButtonClick(23))
    b[23].config(command = lambda : ButtonClick(24))
    b[24].config(command = lambda : ButtonClick(25))
    b[25].config(command = lambda : ButtonClick(26))
    b[26].config(command = lambda : ButtonClick(27))
    b[27].config(command = lambda : ButtonClick(28))
    b[28].config(command = lambda : ButtonClick(29))
    b[29].config(command = lambda : ButtonClick(30))
    b[30].config(command = lambda : ButtonClick(31))
    b[31].config(command = lambda : ButtonClick(32))
    b[32].config(command = lambda : ButtonClick(33))
    b[33].config(command = lambda : ButtonClick(34))
    b[34].config(command = lambda : ButtonClick(35))
    b[35].config(command = lambda : ButtonClick(36))
    b[36].config(command = lambda : ButtonClick(37))
    b[37].config(command = lambda : ButtonClick(38))
    b[38].config(command = lambda : ButtonClick(39))
    b[39].config(command = lambda : ButtonClick(40))
    b[40].config(command = lambda : ButtonClick(41))
    b[41].config(command = lambda : ButtonClick(42))
    b[42].config(command = lambda : ButtonClick(43))
    b[43].config(command = lambda : ButtonClick(44))
    b[44].config(command = lambda : ButtonClick(45))
    b[45].config(command = lambda : ButtonClick(46))
    b[46].config(command = lambda : ButtonClick(47))
    b[47].config(command = lambda : ButtonClick(48))
    b[48].config(command = lambda : ButtonClick(49))
    b[49].config(command = lambda : ButtonClick(50))
    b[50].config(command = lambda : ButtonClick(51))
    b[51].config(command = lambda : ButtonClick(52))
    b[52].config(command = lambda : ButtonClick(53))
    b[53].config(command = lambda : ButtonClick(54))
    b[54].config(command = lambda : ButtonClick(55))
    b[55].config(command = lambda : ButtonClick(56))
    b[56].config(command = lambda : ButtonClick(57))
    b[57].config(command = lambda : ButtonClick(58))
    b[58].config(command = lambda : ButtonClick(59))
    b[59].config(command = lambda : ButtonClick(60))
    b[60].config(command = lambda : ButtonClick(61))
    b[61].config(command = lambda : ButtonClick(62))
    b[62].config(command = lambda : ButtonClick(63))
    b[63].config(command = lambda : ButtonClick(64))
    b[64].config(command = lambda : ButtonClick(65))
    b[65].config(command = lambda : ButtonClick(66))
    b[66].config(command = lambda : ButtonClick(67))
    b[67].config(command = lambda : ButtonClick(68))
    b[68].config(command = lambda : ButtonClick(69))
    b[69].config(command = lambda : ButtonClick(70))
    b[70].config(command = lambda : ButtonClick(71))
    b[71].config(command = lambda : ButtonClick(72))
    b[72].config(command = lambda : ButtonClick(73))
    b[73].config(command = lambda : ButtonClick(74))
    b[74].config(command = lambda : ButtonClick(75))
    b[75].config(command = lambda : ButtonClick(76))
    b[76].config(command = lambda : ButtonClick(77))
    b[77].config(command = lambda : ButtonClick(78))
    b[78].config(command = lambda : ButtonClick(79))
    b[79].config(command = lambda : ButtonClick(80))
    b[80].config(command = lambda : ButtonClick(81))
    b[81].config(command = lambda : ButtonClick(82))
    b[82].config(command = lambda : ButtonClick(83))
    b[83].config(command = lambda : ButtonClick(84))
    b[84].config(command = lambda : ButtonClick(85))
    b[85].config(command = lambda : ButtonClick(86))
    b[86].config(command = lambda : ButtonClick(87))
    b[87].config(command = lambda : ButtonClick(88))
    b[88].config(command = lambda : ButtonClick(89))
    b[89].config(command = lambda : ButtonClick(90))
    b[90].config(command = lambda : ButtonClick(91))
    b[91].config(command = lambda : ButtonClick(92))
    b[92].config(command = lambda : ButtonClick(93))
    b[93].config(command = lambda : ButtonClick(94))
    b[94].config(command = lambda : ButtonClick(95))
    b[95].config(command = lambda : ButtonClick(96))
    b[96].config(command = lambda : ButtonClick(97))
    b[97].config(command = lambda : ButtonClick(98))
    b[98].config(command = lambda : ButtonClick(99))
    b[99].config(command = lambda : ButtonClick(100))

def start(n):
    global size
    size = n
    root = Tk()
    root.title("Tic Tac Toe")
    st = ttk.Style()
    st.configure("my.TButton", font=('Time New Roman',15,'bold'))
    Button(text="New Game", font=('Time New Roman', 15), 
            bg='#FF6633', fg='white', border=5, width=4,command = lambda :Restart()).grid(row=0, column=0, sticky="we",columnspan=2)
    
    b.clear()
    for i in range(1,size+1):
        for j in range(0,size):
            b_x = ttk.Button(root, text=" ", style="my.TButton")
            b_x.grid(row=i, column=j, sticky="nwse",ipady=10)
            b.append(b_x)

    if size==3:
        Size3()
    elif size == 5:
        Size5()
    else:
        Size10()

    root.resizable(0,0)
    root.mainloop()
def display_Size(screen):
    menu = pygame_menu.Menu('Tic Tac Toe', 400, 250,
                       theme=pygame_menu.themes.THEME_ORANGE,
                       center_content=True,
                       columns=3,
                       rows=1)

    menu.add.button('3 x 3', start,3)
    menu.add.button('5 x 5', start,5)
    menu.add.button('10 x 10', start,10)
    menu.mainloop(screen)

pygame.init()
pygame. display. set_caption('Bài Tập Nhóm Số 1')
width, height = 400,250
screen = pygame.display.set_mode((width, height))
menu = pygame_menu.Menu('Nhóm 14', width, height,
                       theme=pygame_menu.themes.THEME_ORANGE)

menu.add.label('Tic Tac Toe')
menu.add.button('Play', display_Size,screen)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)