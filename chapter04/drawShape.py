import turtle

t = turtle.Turtle()
t.shape("turtle")

while  True: #무한 루프는 항상 '참
    c = turtle.textinput("color","컬러(red,green,pink)")
    if c == '0':
        break
    t.color(c)

    s = turtle.textinput("shape","n각형")
    s = int(s)

    for i in range(s):
        t.forward(100)
        t.left(360/s)

    """ if s == '3':
        t.forward(100)
        t.left(360/s)
        t.forward(100)
        t.left(360/s)
        t.forward(100)   
    elif s == '4':
        t.forward(100)
        t.left(360/s)
        t.forward(100)
        t.left(360/s)
        t.forward(100)
        t.left(360/s)
        t.forward(100)
    else:
        print("도형을 잘못 입력했습니다.") """
    
    
turtle.done()