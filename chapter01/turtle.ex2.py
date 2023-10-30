import turtle

t = turtle.Turtle()
t.shape("turtle")

t.fillcolor("blue") #색상선택
t.begin_fill() #채우기 시작
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.end_fill() #채우기 끝

t.penup() #선그리던거 띄움
t.goto(250,0) # x,y좌표 지정
t.pendown #선그리기 위해 내려
t.fillcolor("red")
t.begin_fill()
t.goto(300,0)
t.goto(300,50)
t.goto(250,50)
t.goto(250,0)
t.end_fill()
    
turtle.done()