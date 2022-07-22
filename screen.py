import turtle as tu

FONT = ("Courier", 24, "normal")

screen = tu.Screen()
screen.title = "U.S States Games"
screen.bgpic("blank_states_img.gif")

screen.exitonclick()


## ler texto da tela
screen.write("texto", align="left", font=FONT)