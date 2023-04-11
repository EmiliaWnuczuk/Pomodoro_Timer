from tkinter import *
import math
from tkinter import messagebox
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
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
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_checkmark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        label_timer.config(text="Break", fg=RED)
        messagebox.showinfo(title=":)", message="20 minut break time")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        label_timer.config(text="Break", fg=PINK)
        messagebox.showinfo(title=":)", message="5 minut break time")
    else:
        count_down(WORK_MIN * 60)
        label_timer.config(text="Work", fg=GREEN)
        messagebox.showinfo(title="Work", message="Work!")


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
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        label_checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Label
label_timer = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)
label_checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
label_checkmark.grid(column=1, row=3)


#Buttons
def start():
    start_timer()


button_start = Button(text="Start", bg="white", command=start, font=(FONT_NAME, 10))
button_start.grid(column=0, row=2)
button_start = Button(text="Reset", bg="white", command=reset_timer, font=(FONT_NAME, 10))
button_start.grid(column=2, row=2)

window.mainloop()

