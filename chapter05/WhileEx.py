# 1~10 누적합 구하기
sum = 0
i = 1
""" while i <= 10:
    sum += i
    i = i + 1
print(f"1~10 누적합 : {sum}") """

# 이거는 for문이 while문 보다 효율적이라
for i in range(1,11):
    sum += i
print(f"1~10 누적합 : {sum}")