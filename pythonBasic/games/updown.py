import random
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
runUpDown()