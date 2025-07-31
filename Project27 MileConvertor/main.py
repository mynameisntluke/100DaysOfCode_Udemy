import tkinter

window = tkinter.Tk()
window.title("My First GUI")
window.minsize(width = 500, height = 300)
window.config(padx = 20, pady = 20)

def button_clicked():
    print("Clickedy Click Click")
    my_label["text"] = input_cell.get()
    # my_label.config(text = "wahhhhooooo")

# Label
my_label = tkinter.Label(text = "I Am A Label", font = ("Arial", 20, "bold"))
# my_label.pack()
# my_label.place(x = 100, y = 50)
my_label.grid(column = 0, row = 0)

# Button
button = tkinter.Button(text = "Click Me Forever", command = button_clicked)
button.grid(column = 1, row = 1)
button.config(padx = 50, pady = 30)

# Second Button
button_two = tkinter.Button(text = "Hanging with Label")
button_two.grid(column = 2, row = 0)

# Entry
input_cell = tkinter.Entry(width = 15)
input_cell.grid(column = 3, row = 3)

window.mainloop()