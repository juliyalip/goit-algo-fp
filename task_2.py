import turtle
import math

def draw_tree(t, length, level):
    if level == 0:
        return
    
    t.forward(length)

    pos = t.position()
    heading = t.heading()

    t.left(45)
    draw_tree(t, length * math.sqrt(2)/2, level -1)
    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.pendown()

    t.right(45)
    t.right(45)
    draw_tree(t, length*math.sqrt(2) /2, level -1)

    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.pendown()

if __name__=="__main__":
    level= int(input("Введіть рівень рекурсії для побудови дерева: "))

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Дерево Піфагора")
    t=turtle.Turtle()
    t.color("gray")
    t.speed(0)
    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()

    draw_tree(t, 100, level)
    turtle.done()