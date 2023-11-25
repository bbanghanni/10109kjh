import pygame
import random

colors = {'white':(255, 255, 255)
         ,'black': (0 ,0 ,0),
          '-1':(200, 200,200),
          '2':(251, 233, 231),
          '4':(255, 204, 188),
          '8':(255, 171, 145),
          '16':(255, 138, 101),
          '32':(255, 112, 67),
          '64':(255, 87, 34),
          '128':(244, 81, 30),
          '256':(230, 74, 25),
          '512':(216, 67, 21),
          '1024':(191, 54, 12),
          '2048':(213, 0, 0)}#색상 설정 딕셔너리

board = [[-1,-1,-1,-1],
         [-1,-1,-1,-1],
         [-1,-1,-1,-1],
         [-1,-1,-1,-1]]

screensize = (500, 500)
screen = pygame.display.set_mode(screensize)
isGameRunning = True

def initScreen():
    screen.fill(colors['white'])
    pygame.display.update()

def startBlock():
        for i in range(0,2):
            X = random.randint(0, 3)
            Y = random.randint(0, 3)
            board[X][Y] = 2

def addNewBlock():
    canSet = False
    while not canSet:
        randomX = random.randint(0, 3)
        randomY = random.randint(0, 3)
        if board[randomX][randomY] == -1:
            canSet = True

    board[randomX][randomY] = 2 if random.randint(1,10) < 10 else 4 # 1/10확률로 4,이외에는 2가 추가

def setEventListener():
    global isGameRunning
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False
            return
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                isGameRunning = False
                return
            elif event == pygame.K_DOWN:
                kdown()
            elif event == pygame.K_UP:
                kup()
            elif event == pygame.K_RIGHT:
                kright()
            elif event == pygame.K_LEFT:
                kleft()
            addNewBlock()

def kdown():
    for x in range(2,1,-1):
        for y in range(0,4):
            if board[x][y] != -1:
                for z in range(x+1,4):
                    if board[x][z] != board[x][y] and board[x][z] != -1:
                        break
                    elif board[x][z] == board[x][y]:
                        board[x][z] *= 2
                        board[x][y] = -1
                        break
                board[3][y] = board[x][y]
def kup():
    for x in range(1,4):
        for y in range(0,4):
            if board[x][y] != -1:
                for z in range(x-1,1):
                    if board[z][y] != board[x][y] and board[z][y] != -1:
                        break
                    elif board[z][y] == board[x][y]:
                        board[z][y] *= 2
                        board[x][y] = -1
                        break
                board[0][y] = board[x][y]
def kright():
    for x in range(3,-1,-1):
        for y in range(0,4):
            if board[x][y] != -1:
                for z in range(x+1,4):
                    if board[z][y] != board[x][y] and board[z][y] != -1:
                        break
                    elif board[z][y] == board[x][y]:
                        board[z][y] *= 2
                        board[x][y] = -1
                        break
                board[3][y] = board[x][y]
def kleft():
    for x in range(3,-1,-1):
        for y in range(0,4):
            if board[x][y] != -1:
                for z in range(x+1,4):
                    if board[z][y] != board[x][y] and board[z][y] != -1:
                        break
                    elif board[z][y] == board[x][y]:
                        board[z][y] *= 2
                        board[x][y] = -1
                        break
                board[3][y] = board[x][y]



def drawDisplay():
    global screen
    baseX = 35
    baseY = 35
    blockHeight = 100
    blockWidth = 100
    margin = 10
    for i in range(4):
        for j in range(4):
            x = (blockWidth + margin) * j + baseX
            y = (blockHeight + margin) * i + baseY
            data = str(board[i][j])
            if data == -1 :
                pygame.draw.rect(screen, colors[data], [x, y, blockWidth, blockHeight],2)
            else:
                pygame.draw.rect(screen, colors[data], [x, y, blockWidth, blockHeight])
    pygame.display.flip()

def run2048():
    pygame.init()
    initScreen()
    print("2048 게임 시작")
    startBlock()
    while isGameRunning:
        setEventListener()
        drawDisplay()

    pygame.quit()

run2048()



# 0. pygame library 검색 -> 숫자를 화면에 보이게
# 1. 방향키 눌렀을때, 블럭 이동
# 2. 블럭 이동했을때 같은 방향에 같은 숫자가 있는경우, 블럭 합치기
# 3. 2048이 등장하면 게임종료
