import pygame

colors = {'white':(255, 255, 255)
         ,'black': (0 ,0 ,0),
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
          '2048':(213, 0, 0)}

def initScreen():
    size = (500, 500)
    screen = pygame.display.set_mode(size)
    screen.fill(colors['white'])
    pygame.display.update()

isGameRunning = True

def run2048():
    pygame.init()
    initScreen()
    print("2048 게임 시작")
    while isGameRunning:
        pass
    pygame.quit()

run2048()
