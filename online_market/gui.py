from tkinter import *
from customer import Customer

...
vdd = Customer()


def clicked():
    vdd.shop()


window = Tk()

window.title("Yigit Market")
window.geometry('640x480')
btn = Button(window, text="Siparis", command=clicked)

btn.grid(column=0, row=0)

window.mainloop()

