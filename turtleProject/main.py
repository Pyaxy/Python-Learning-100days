import turtle
import random

# 提取颜色
# import colorgram
#
# rgb = []
# colors = colorgram.extract('image.jpg', 15)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb.append((r, g, b))
rgb = [(134, 167, 191), (211, 156, 106), (197, 143, 166), (29, 110, 168), (234, 214, 86), (127, 74, 92), (187, 178, 19),
       (26, 136, 66), (55, 18, 26), (142, 20, 40), (38, 175, 113)]
tim = turtle.Turtle()
tim.hideturtle()
tim.speed(0)
tim.penup()
turtle.colormode(255)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)


def draw_row():
    for _ in range(10):
        tim.dot(20, random.choice(rgb))
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)

for _ in range(10):
    draw_row()

screen = turtle.Screen()
screen.exitonclick()