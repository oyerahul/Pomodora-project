from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
BLUE = "#205295"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    checkmark_label.config(text='')
    canvas.itemconfig(timer_text, text="00:00")
    global  reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sed = LONG_BREAK_MIN * 60
    marks = " "

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps == 2 or reps == 4 or reps == 6:
        marks += "✓"
        checkmark_label.config(text=marks)
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    elif reps == 8:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sed)
        reps = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "{:02d}".format(count_sec)
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min == 0:
        count_min = "{:02d}".format(count_min)
    elif count_min < 10:
        count_min = "{:02d}".format(count_min)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomoto_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomoto_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)
timer_label.config(padx=20)

checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10))
checkmark_label.grid(row=3, column=1)

start_button = Button(text="Start", fg=BLUE, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", fg=BLUE, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

window, mainloop()
