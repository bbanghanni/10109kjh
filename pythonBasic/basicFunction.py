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
            if(hangman_input_history.index(alphabet)): #이미 입력된 값인지 확인
                print("이미 입력한 값입니다. 새로운 알파벳을 입력해주세요.")
            else:
                return alphabet

def runHangMan():
    hangman_input_history = []
    word = getRandomWord()
    alphabet = getHangmanInput()

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


#전역변수:모든곳에서 쓰임/ 지역변수 : 함수내부or구문내부에서 쓰임(for while if''')쓰고 소멸됨/매개변수 : 함수로 설정되는 변수

