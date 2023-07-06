import random

print("로또 추첨합니다")

for i in range(5) :
    lotto = random.sample(range(1,46),6)
    print(lotto)
