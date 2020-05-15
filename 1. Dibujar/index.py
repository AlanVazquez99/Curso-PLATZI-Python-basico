import turtle

def main():
    window = turtle.Screen()
    box = turtle.Turtle()
    paint(box)
    turtle.mainloop()


def paint(box):
    lados = int(input("Ingresa los lados de la figura: "))
    length = int(input("Ingresa el tamaño por lado: "))
 
    angle = 360 / lados

    for i in range(lados):
        line(box, length, angle)

def line(box, length, angle):
    box.forward(length)
    box.left(angle)

if __name__ == "__main__":
    main()