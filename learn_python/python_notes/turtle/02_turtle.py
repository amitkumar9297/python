import turtle
# create a turtle window and hide turtle and img insert
# hum ne ek turtle ki window create karna hai , ek variable ko module.function assign karate hue
turtle_window = turtle.Turtle()

# hum ne tutle screen ka change kar ke white karna hai
# jis ke lye hum ne module.screen.bgcolor() ka use krna hai
turtle_window.screen.bgcolor("white")

# turtle screen ka color toh change ho gya hai pr screen pe turtle show ho reha hai
# aur ab hum ne show hor rhe turtle ko hide krna hai
# jis ke lye hum ne hide tutle method use karna hai
turtle_window.hideturtle()

turtle_window.screen.bgpic("bg1.gif")
