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

def printPresentWords(word):
    printStr = ""
    for i in word:
        if i in hangman_input_history:
            printStr = printStr + i
        else:
            printStr = printStr + "_"
    print(printStr)

def runHangMan():
    global hangman_input_history
    hangman_input_history = []
    chance = 7
    correct = 0
    word = getRandomWord()
    wordSet = set(word)
    while chance > 0:
        printPresentWords(word)
        alphabet = str(getHangmanInput())
        hangman_input_history.append(alphabet)
        if word.find(alphabet) != -1:
            correct = correct + 1
            print("존재합니다!")
        else:
            chance = chance - 1
            if chance == 0:
                print("You die")
            else:
                print("남은 기회 :", chance)
        if correct >= len(wordSet):
            print("Alive!")
            break


        #a.find(b)가 속해있지 않을 때 -1
        #alphabet이 word에 속해있으면 정답, 아니면 기회깎기



    # for문으로 맞는 글자 바꾸기
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
