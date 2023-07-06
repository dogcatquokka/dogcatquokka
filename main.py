import random

print("로또 추첨 왜 충돌이 안나지?!!!")

for i in range(5) :
    lotto = random.sample(range(1,46),6)
    print(lotto)
