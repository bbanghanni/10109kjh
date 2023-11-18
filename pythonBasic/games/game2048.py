import pygame

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

def setEventListener():
    global isGameRunning
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                isGameRunning = False
            elif event == pygame.K_DOWN:
                print("아래")
            elif event == pygame.K_UP:
                print("위")
            elif event == pygame.K_RIGHT:
                print("오른쪽")
            elif event == pygame.K_LEFT:
                print("왼쪽")

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
    while isGameRunning:
        setEventListener()
        drawDisplay()

    pygame.quit()

run2048()
