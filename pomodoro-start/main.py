from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    Title.config(text="Timer")
    Tick.config(text="")
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        Title.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        Title.config(text="Break", fg=PINK)
    elif reps % 2 != 0:
        count_down(work_sec)
        Title.config(text="Work!", fg=GREEN)
    # if 2nd/4th/6th:


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 300)
    else:

        reps = reps + 1
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        Tick.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=1000, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

button = Button(text="Start", highlightthickness=0, command=start_timer)
button.grid(column=0, row=2)

Title = Label(text="Timer", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
Title.grid(column=1, row=0)

Tick = Label(font=("Arial", 16), bg=YELLOW, fg=GREEN, highlightthickness=0)
Tick.grid(column=1, row=3)

button2 = Button(text="Reset", highlightthickness=0, command=reset_timer)
button2.grid(column=2, row=2)

window.mainloop()
