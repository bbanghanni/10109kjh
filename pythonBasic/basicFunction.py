# f(x) = 3x + 5 ?
import random
def tmpFunction(x):
    return 3 * x + 5

print(tmpFunction(5))
def menuprint():
    print("=========GAME=========")
    print("1. 행맨")
    print("2. 업다운")
    print("0, 종료")
    print("=========GAME=========")

def getRandomWord():
    words = ["hang", "pretty", "apple", "ant", "water", "MCdonalds", "fluent", "voca", "galaxy"]
    return words[random.randrange(0, len(words))]

hangman_input_history = []
def getHangmanInput():
    while True:
        user_input = input("Input alphabet ::: ")
        if(user_input.isalpha()): #알파벳인지 확인
            alphabet = user_input[0].lower()
            if(alphabet in hangman_input_history): #이미 입력된 값인지 확인
                print("이미 입력한 값입니다. 새로운 알파벳을 입력해주세요.")
            else:
                return alphabet

def printCorrectWords(a,b,c):
    dap = list(a)
    for i in b:
        if i == c:
            dap[b.find(c)] = c
            dap[b.rfind(c)] = c # 문제점 : 중복 알파벳 3개 이상 있을 때 답을 맞출 수 없음
    dap = ''.join(dap)
    return dap


def runHangMan():
    global hangman_input_history
    hangman_input_history = []
    chance = 7
    word = getRandomWord()
    correct = "_"*len(word)
    while chance > 0:
        alphabet = getHangmanInput()
        hangman_input_history.append(alphabet)
        correct = printCorrectWords(correct, word, alphabet)
        if word.find(alphabet) != -1:
            print("존재합니다!")
            print(correct)
            if correct == word:
                print("정답입니다!! 게임을 종료하겠습니다.")
                break

        else:
            chance = chance - 1
            print("남은 기회 :", chance)






def runUpDown():
    answer = random.randrange(0, 10)
    chance = 3
    while chance > 0:
        user_input = int(input("값을 입력하세요 >>"))

        if user_input == answer:
            print("정답입니다!")
            break
        else:
            chance = chance - 1
            if user_input > answer:
                print("down")
            else:
                print("up")

userinput = -1

while userinput != 0:
    menuprint()
    userinput = int(input("SELECT MENU ::: "))

    if userinput == 1:
        runHangMan()
    elif userinput == 2:
        runUpDown()



# 1. 모든 정답을 맞췄을때 게임이 끝나지 않음
# -> 맞추면 alive  출력해주고 그만하기 (break문을 사용)

# 2. 내가 맞춘 정답들이 어디에 위치해있는지 알수없음
# -> s _ _ s _ _ _ 출력
# printCorrectWords() 함수를 선언(optional)해서 그 안에서 입력되었던 맞는 항목을 위치에 맞게 출력
