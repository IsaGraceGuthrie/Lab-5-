#the author's names are Isa Guthrie and Ellen Kevin
#part 2
import turtle
riley=turtle.Turtle()
riley.width(5)
riley.speed(5)
mood=input("How are you feeling? \n")
def draw_star(color):
    for side in range(5):
        riley.color(color)
        riley.forward(100)
        riley.right(144)
if mood == "happy":
    draw_star("pink")
elif mood== "sad":
    draw_star("blue")
elif mood== "sleepy":
    draw_star("green")
else:
    draw_star("red")

#authors names are Isa Grace and Ellen Kevin
#part 3
def perfect_number(n):
    x=0
    for y in range (1,n):
        if n%y==0:
            x=x+y
    if x==n:
        print("true")
    else:
        print("false")
perfect_number(6)
perfect_number(15)
perfect_number(1000)
perfect_number(10000)
