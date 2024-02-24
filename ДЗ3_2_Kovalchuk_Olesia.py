import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    recursion_level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))

    screen = turtle.Screen()
    screen.bgcolor("white")

    snowflake = turtle.Turtle()
    snowflake.speed(100)  

    snowflake.penup()
    snowflake.goto(-150, 90)
    snowflake.pendown()

    koch_snowflake(snowflake, recursion_level, 300)

    screen.exitonclick()

if __name__ == "__main__":
    main()
