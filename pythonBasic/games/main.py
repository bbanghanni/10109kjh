from pythonBasic.games.updown import runUpDown
from pythonBasic.games.hangman import runHangMan
from pythonBasic.games.game2048 import run2048

import random

def menuprint():
    print("=========GAME=========")
    print("1. 행맨")
    print("2. 업다운")
    print("3, 2048")
    print("0, 종료")
    print("=========GAME=========")


userinput = -1

while userinput != 0:
    menuprint()
    userinput = int(input("SELECT MENU ::: "))

    if userinput == 1:
        runHangMan()
    elif userinput == 2:
        runUpDown()
    elif userinput == 3:
        run2048()



# 1. 모든 정답을 맞췄을때 게임이 끝나지 않음
# -> 맞추면 alive  출력해주고 그만하기 (break문을 사용)

# 2. 내가 맞춘 정답들이 어디에 위치해있는지 알수없음
# -> s _ _ s _ _ _ 출력
# printCorrectWords() 함수를 선언(optional)해서 그 안에서 입력되었던 맞는 항목을 위치에 맞게 출력
