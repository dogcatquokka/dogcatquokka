import random

<<<<<<< HEAD
#충돌 일어나서 수정 했습니다
print("로또 추첨 왜 충돌이 안나지?!!!")
>>>>>>> f09a84cb00be247e12c1c8d6336e25e325923341

for i in range(5) :
    lotto = random.sample(range(1,46),6)
    print(lotto)


y = input("y 눌러?:")

if y == "y" :
    lotto = random.sample(range(1,46),6)
    print(lotto)


