""" num = int(input("정수를 입력하시오:"))

#양수일때는 짝수인지 홀수인지 판단하고
# 음수일때는 양수인지 음수인지만 출력
if num>0:
    if (num % 2 == 0): # (%:나머지 연산) 
        print(f"{num} => 짝수")
    else:
        print(f"{num} => 홀수")
else:
        print(f"{num} => 음수") """

x=100
y=200
# 참 if 조건 else 거짓
max_val = (x if x>y else y)
absolute_value = (x if x> 0 else -x)
print(f"x: {x}, y: {y}, max_val: {max_val}, absolute_value : {absolute_value}")

