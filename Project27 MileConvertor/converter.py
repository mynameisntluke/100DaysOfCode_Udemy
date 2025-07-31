# TODO 1: Add features in grid layout
# TODO 2: Add function
# TODO 3: Add function to button
# TODO 4: Adjust padding and size issues
# TODO 5: Separate class for function

WIDTH = 300
HEIGHT = 160
FONT = ("Arial", 16, "bold")

import tkinter as tk

window = tk.Tk()
window.title("Mile to km Converter")
window.minsize(width = WIDTH, height = HEIGHT)
window.config(padx = 20, pady = 20)

def ignore():
    pass

### TOP ROW ###

# INPUT
# Entry
input_cell = tk.Entry(width = 15)
input_cell.grid(column = 1, row = 0)

# MILES LABEL
miles_label = tk.Label(text = "Miles", font = FONT)
miles_label.grid(column = 2, row = 0)



### MIDDLE ROW ###

# 'is equal to' Label
equal_label = tk.Label(text = "is equal to", font = FONT)
equal_label.grid(column = 0, row = 1)

# Km Value Label
km_value_label = tk.Label(text = "0", font = FONT)
km_value_label.grid(column = 1, row = 1)

# Km label
km_label = tk.Label(text = "Km", font = FONT)
km_label.grid(column = 2, row = 1)


### BOTTOM ROW ###
# Button
button = tk.Button(text = "Calculate", command = ignore)
button.grid(column = 1, row = 2)
#button.config(padx = 50, pady = 30)

window.mainloop()
