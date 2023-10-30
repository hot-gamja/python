import random

#주사위를 두 번 던져서 나오는 수의 합 맞추는 게임
x = random.randint(1,6)
y = random.randint(1,6)

answer = int(input("두수의 합은?"))
flag = 1 if x+y == answer else 0
if flag == 1:
    print(f"{X}+{y} == {answer}")
else:
    print(f"{x}+{y} != {answer}")
