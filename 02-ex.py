import random
### 전역 변수 선언 부분 ###
dice1, dice2, dice3 = [0]*3
throwCount = 0

## 메인 코드 부분 ##
while True:
    throwCount += 1

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)

    if dice1 == dice2 == dice3:
        print("3개의 주사위가 모두 동일한 숫자가 나옴 ->", dice1, dice2, dice3)
        break

    print(dice1, dice2, dice3)

print("3개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수 -->", throwCount)