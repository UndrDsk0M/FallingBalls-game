import tkinter as tk
import random

def move(event):
    if event.keysym == 'Left':
        canvas.move(platform, -20, 0)
    elif event.keysym == 'Right':
        canvas.move(platform, 20, 0)

def create_ball():
    x = random.randint(10, 390)
    ball = canvas.create_oval(x, 10, x+10, 20, fill="red")
    balls.append(ball)
    main.after(1500, create_ball)

def update_game():
    for ball in balls[:]:
        canvas.move(ball, 0, 5)
        if canvas.coords(ball)[3] > 400 :
            canvas.delete(ball)
            balls.remove(ball)
            update_score(1)
        elif canvas.coords(ball)[3] >= canvas.coords(platform)[1] and \
            canvas.coords(platform)[0] < canvas.coords(ball)[0] < canvas.coords(platform)[2]:
            canvas.delete(ball)
            balls.remove(ball)
            update_score(2)
    main.after(25, update_game)
def update_score(a):
    global score
    if a == 1:
        score -= 1
        canvas.itemconfig(score_text, text=f"Score:{score}", fill="black")
    elif a == 2:
        score += 1
    canvas.itemconfig(score_text, text=f"Score:{score}")
    if score > 10:
        canvas.itemconfig(score_text, text=f"😉 Well Done Score:{score}", fill="gray")
    if score <= 0:
        canvas.itemconfig(score_text, text=f"😥 You Lost The Game", fill="black")
        update_score(0)


main= tk.Tk()
main.title("FallingBalls Game ")
canvas =tk.Canvas(main, width=400, height=400, bg='white')
canvas.pack()

# x1 y1 x2 y2
platform = canvas.create_rectangle(150,380,250,395, fill='lightPink', outline='gray')
balls, score = [], 0

score_text = canvas.create_text(300,20, text="Score", font=("Arial", 13), fill="black")

try_again_btn = tk.Button(main ,text="Try Again", command=update_score)
try_again_btn.pack()
canvas.bind_all('<KeyPress-Left>', move)
canvas.bind_all('<KeyPress-Right>', move)

create_ball()
update_game()
main.mainloop()
