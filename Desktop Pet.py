import tkinter as tk
import random
from PIL import Image, ImageTk


root = tk.Tk()
root.overrideredirect(True)
root.config(bg="white")
root.attributes("-transparentcolor", "white")
root.attributes("-topmost", True)


canvas = tk.Canvas(
    root,
    width =150,
    height = 150,
    highlightthickness=0,
    bg="white"
)
canvas.pack()

pet = canvas.create_image(
    60,
    60
)

gifs = {
    "back_left": Image.open("bulbasaur_back_left.gif"),
    "back_right": Image.open("bulbasaur_back_right.gif"),
    "left": Image.open("bulbasaur_left.gif"),
    "right": Image.open("bulbasaur_right.gif")
}

gif = gifs["left"]

def choose_direction():
    global gif, frame

    if dy < 0:  # moving UP
        if dx < 0:
            gif = gifs["back_left"]
        else:
            gif = gifs["back_right"]

    elif dy > 0:  # moving DOWN
        if dx < 0:
            gif = gifs["left"]
        else:
            gif = gifs["right"]

    elif dx < 0:
        gif = gifs["left"]

    elif dx > 0:
        gif = gifs["right"]

    if dx == 0:
        if dy == 0:
            gif = gifs["left"]
    frame = 0

frame = 0
def animate():

    global frame

    gif.seek(frame)

    image = gif.copy()
    # image = image.resize((60, 60))
    image = ImageTk.PhotoImage(image)

    canvas.itemconfig(
        pet,
        image=image
    )

    canvas.image = image

    frame += 1

    if frame >= gif.n_frames:
        frame = 0

    root.after(100, animate)
animate()

x =100
y = 400


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

def change_dirn():

    global dx,dy

    dx = random.choice([-3,3,0])
    dy = random.choice([-1,1,0])

    choose_direction()
    time = random.randint(5,10)*1000
    # print("will move for", time/1000,"dx=",dx,"dy=",dy)
    root.after(time, change_dirn)


def move():
    global x, y, dx, dy
    
    x += dx
    y += dy

    if x <= 0 or x >= screen_width - 120:
        dx = -dx
        choose_direction()
    if y <= 0 or y >= screen_height - 120:
        dy = -dy 
        choose_direction()   
    root.geometry(f"120x120+{x}+{y}")

    
    root.after(50, move)


change_dirn()
move()


root.mainloop()