import random

n = random.randint(1,100)
print(n)
cnt = 0 #카운트 초기화
while True:
    ans = int(input("1~100 정수를 입력하세요: "))
    cnt = cnt + 1

    if ans == n: #맞춘경우
        print("{n}을 {cnt}만에 맞추셨네요.")
    elif ans > n:
        print("다운")
    else:
        print("업")