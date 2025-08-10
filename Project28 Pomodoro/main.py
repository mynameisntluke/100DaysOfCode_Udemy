import math
import winsound
from tkinter import *

#TODO 1: Sound effects
#TODO 2: Format break labels so they fit on screen

#website - Color Hunt
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
MILLI_SEC = 1000

on_break = False
reps = 0
total_reps = 4
timer =  None


BTN_FONT = (FONT_NAME, 18, "normal")

CANVAS_WIDTH = 220
CANVAS_HEIGHT = 246

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_app():
    global reps, timer, on_break
    reps = 0
    on_break = False
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    add_ticks()
    start_btn["state"] = "active"
    if timer:
        window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    start_btn["state"] = "disabled"
    if on_break:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break")
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work")

    # if reps % 8 == 0:
    #     count_down(LONG_BREAK_MIN * 60)
    #     title_label.config(text = "Long Break")
    # elif reps % 2 == 0:
    #     count_down(SHORT_BREAK_MIN * 60)
    #     title_label.config(text = "Break")
    # else:
    #     count_down(WORK_MIN * 60)
    #     title_label.config(text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer, on_break, reps

    minutes = math.floor(count/60)
    seconds = count % 60

    seconds = format_time(seconds)
    minutes = format_time(minutes)

    canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(MILLI_SEC, count_down, count - 1)
    else:
        # canvas.itemconfig(timer_text, text = "goodbye")
        alarm()
        start_btn["state"] = "active"
        add_ticks()
        on_break = not on_break
        # start_timer()

        if on_break:
            # If on_break one rep has just been completed.
            # (Break has ended)
            reps +=1


def format_time(t):
    if t == 0:
        t = "00"
    elif t < 10:
        t = f"0{t}"
    return t

def add_ticks():
    ticks = ""
    for _ in range(reps):
        ticks += "✓"
    tick_label.config(text = ticks)

def alarm():
    winsound.Beep(700, 100)
    winsound.Beep(900, 100)
    winsound.Beep(800, 100)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)


title_label = Label(text = "Timer", bg = YELLOW, fg = GREEN, font = (FONT_NAME, 35, "bold"))
title_label.grid(column = 1, row = 0)

tom_img = PhotoImage(file = "tomato.png")
canvas = Canvas(width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = YELLOW, highlightthickness = 0 )
canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image = tom_img)
timer_text = canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2 + 20, text = "00:00", fill = "white", font = (FONT_NAME, 25, "bold") )
canvas.grid(column = 1, row = 1)

start_btn = Button(text = "Start", font = BTN_FONT, bg = PINK, fg = "white", command = start_timer)
start_btn.grid(column = 0, row = 2)

reset_btn = Button(text = "Reset", font = BTN_FONT, bg = PINK, fg = "white", command = reset_app)
reset_btn.grid(column = 2, row = 2)

tick_label = Label(bg = YELLOW, fg = "GREEN", font = (FONT_NAME, 16, "normal"))
tick_label.grid(column = 1, row = 3)




window.mainloop()
# ---------------------------- FYI ------------------------------- #

#start_button["state"] = "disabled"
#start_button["state"] = "active"
#start_button["disabledforeground"] = start_button["foreground"]