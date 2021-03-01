import turtle

SPEED = 11
BG_COLOR = "light blue"
PEN_COLOR = "red"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
DRAWING_WIDTH = 700
DRAWING_HEIGHT = 700
PEN_WIDTH = 3
TITLE = "H-Tree Fractal with Python Turtle Graphics"
FRACTAL_DEPTH = 4

def draw_line(tur, pos1, pos2):
    tur.penup()
    tur.goto(pos1[0], pos1[1])
    tur.pendown()
    tur.goto(pos2[0], pos2[1])

def recursive_draw(tur, x, y, width, height, count):
    draw_line(
        tur,
        [x + width * 0.25, y + height // 2],
        [x + width * 0.75, y + height // 2],
    )
    draw_line(
        tur,
        [x + width * 0.25, y + (height * 0.5) // 2],
        [x + width * 0.25, y + (height * 1.5) // 2],
    )
    draw_line(
        tur,
        [x + width * 0.75, y + (height * 0.5) // 2],
        [x + width * 0.75, y + (height * 1.5) // 2],
    )

    if count <= 0:
        return
    else:
        count -= 1
        recursive_draw(tur, x, y, width // 2, height // 2, count)
        recursive_draw(tur, x + width // 2, y, width // 2, height // 2, count)
        recursive_draw(tur, x, y + width // 2, width // 2, height // 2, count)
        recursive_draw(tur, x + width // 2, y + width // 2, width // 2, height // 2, count)

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title(TITLE)
    screen.bgcolor(BG_COLOR)

    artist = turtle.Turtle()
    artist.hideturtle()

    artist.pensize(PEN_WIDTH)
    artist.color(PEN_COLOR)
    
    artist.speed(SPEED)

    recursive_draw(artist, - DRAWING_WIDTH / 2, - DRAWING_HEIGHT / 2, DRAWING_WIDTH, DRAWING_HEIGHT, FRACTAL_DEPTH)

    turtle.done()