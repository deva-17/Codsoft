# simple calculator
from tkinter import *

root = Tk()
root.title("calculator")
input = Entry(root, width=70, font=("helvicta", 8))
input.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def click(num):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(num))


def add():  # addition operation
    global fnum
    current = input.get()
    fnum = int(current)
    input.delete(0, END)


def sub():  # subtraction operation
    global fnum
    current = input.get()
    fnum = int(current)
    input.delete(0, END)


def mul():  # multiplication operation
    global fnum
    current = input.get()
    fnum = int(current)
    input.delete(0, END)


def div():  # division operation
    global fnum
    current = input.get()
    fnum = int(current)
    input.delete(0, END)


def bool():  # percentage operation
    global fnum
    current = input.get()
    fnum = int(current)
    input.delete(0, END)


def exponent():  # exponenet operation
    global fnum
    current = input.get()
    fnum = int(current)
    input.delete(0, END)


def clear():
    input.delete(0, END)


def equal():
    current = input.get()
    snum = int(current)
    if operation == "+":
        input.delete(0, END)
        input.insert(0, str(fnum + snum))
    elif operation == "-":
        input.delete(0, END)
        input.insert(0, str(fnum - snum))
    elif operation == "*":
        input.delete(0, END)
        input.insert(0, str(fnum * snum))
    elif operation == "/":
        input.delete(0, END)
        input.insert(0, str(fnum / snum))
    elif operation == "%":
        input.delete(0, END)
        input.insert(0, str(fnum % snum))
    elif operation == "**":
        input.delete(0, END)
        input.insert(0, str(fnum ** snum))


# buttons
button_1 = Button(root, text="1", padx=50, pady=25, command=lambda: click(1))
button_2 = Button(root, text="2", padx=50, pady=25, command=lambda: click(2))
button_3 = Button(root, text="3", padx=50, pady=25, command=lambda: click(3))
button_4 = Button(root, text="4", padx=50, pady=25, command=lambda: click(4))
button_5 = Button(root, text="5", padx=50, pady=25, command=lambda: click(5))
button_6 = Button(root, text="6", padx=50, pady=25, command=lambda: click(6))
button_7 = Button(root, text="7", padx=50, pady=25, command=lambda: click(7))
button_8 = Button(root, text="8", padx=50, pady=25, command=lambda: click(8))
button_9 = Button(root, text="9", padx=50, pady=25, command=lambda: click(9))
button_0 = Button(root, text="0", padx=110, pady=25, command=lambda: click(0))

button_add = Button(root, text="+", font=('cooper black', 15), padx=43, pady=18, fg="orange",
                    command=lambda: (add(), set_operation("+")))
button_sub = Button(root, text="-", font=('cooper black', 15), padx=45, pady=18, fg="orange",
                    command=lambda: (sub(), set_operation("-")))
button_mul = Button(root, text="*", font=('cooper black', 15), padx=42, pady=18, fg="orange",
                    command=lambda: (mul(), set_operation("*")))
button_div = Button(root, text="/", font=('cooper black', 15), padx=43, pady=18, fg="orange",
                    command=lambda: (div(), set_operation("/")))
button_int = Button(root, text="%", font=('cooper black', 15), padx=40, pady=18, fg="orange",
                    command=lambda: (bool(), set_operation("%")))
button_float = Button(root, text="**", font=('cooper black', 15), padx=36, pady=18, fg="orange",
                      command=lambda: (exponent(), set_operation("**")))

button_clear = Button(root, text="AC", padx=45, pady=25, command=clear, bg="orange")
button_equal = Button(root, text="=", font=('cooper black', 15), padx=100, pady=18, command=equal, bg="orange")

# Button layout
button_clear.grid(row=1, column=0)
button_float.grid(row=1, column=1)
button_int.grid(row=1, column=2)
button_div.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_0.grid(row=5, column=0, columnspan=2)
button_equal.grid(row=5, column=2, columnspan=2)


def set_operation(op):
    global operation
    operation = op


root.mainloop()
