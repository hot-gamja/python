#09월 26일 23:59분까지 제출

while True :
    print("--------Menu------")
    print("1. 계산기: 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/), 나눗셈_몫(//), 나눗셈_나머지(%)")
    print("2. 문자열길이") #len(str)
    print("3. 대소문자변환") #str.upper(), str.lower()
    print("0. 종료")
    print("-------------------")

    Menu = input("기능을 선택하시오...")

    if Menu == "1":
     operation = input("사용할 연사자를 고르시오...(+,-,/,//,%)")
     
     if operation not in ('+','-','/','//','%'):
        print("오류!!오류!! 다시선택!!!")
     else:
            num1 = float(input("숫자1번 일력하시오:"))
            num2 = float(input("숫자2번 입력하시오:"))

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "0으로 나눌수 없습니다..."
            elif operation == "//":
                if num2 != 0:
                    result = num1 // num2
                else:
                    result = "0으로 나눌수 없습니다..."
            elif operation == "%":
                if num2 != 0:
                    result = num1 % num2
                else:
                    result = "0으로 나눌수 없습니다..."

            print("결과:", result)

    elif Menu == "2":
        input_str = input("문자열을 입력하시오: ")
        length = len(input_str) #문자열 길이 알려주는 len
        print("문자열 길이:", length)

    elif Menu == "3":
        input_str = input("문자열을 입력하시오: ")
        print("대문자로 변환:", input_str.upper()) #upper
        print("소문자로 변환:", input_str.lower()) #lower
    
    elif Menu == "0":
        print("프로그램을 종료합니다!!!!")
        break
        
        
    

      