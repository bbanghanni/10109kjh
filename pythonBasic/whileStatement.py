# number = 0
#
# while number < 5 :
#     print(number)
#     number = number + 1
#
#
#
# #user_input = -1
#
# # while user_input != 2:
# #     user_input = int(input("갑을 입력하세요 >>"))
#
# while True:
#     print("=====메뉴=====")
#     print("1, 시작하기")
#     print("2, 종료하기")
#     print("=============")
#
#     user_input = int(input("값을 입력하세요 >>"))
#     if user_input == 2:
#         break


import random

answer = random.randrange(0, 10)
user_input = -1
chance = 3

 #사용자가 answer 맞출때까지 반복
 #1. 사용자에게 기회 주기
 #2. 틀렸을 떄 updown 출력해주기

while chance > 0:
    user_input = int(input("값을 입력하세요 >>"))

    if user_input == answer:
        print("정답입니다!")
        break
    else :
        chance == chance - 1
        if user_input > answer:
            print("down")

        else:
            print("up")

