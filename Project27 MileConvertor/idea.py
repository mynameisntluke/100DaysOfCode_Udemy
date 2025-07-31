import tkinter, time

t = time.localtime()
name = "Luke"

def greet(hour):
    if hour < 12 and hour > 5:
        msg = "Good Morning"
    elif hour < 17:
        msg = "Good Afternoon"
    elif hour < 20:
        msg = "Good Evening"
    else:
        msg = "Good Night"
    return msg

print(f"{greet(t.tm_hour)} {name}.\nThe time is: {t.tm_hour}:{t.tm_min}")