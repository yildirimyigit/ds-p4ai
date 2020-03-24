"""
  @author: yigit.yildirim@boun.edu.tr
"""

from tkinter import *

from world import World


# Window-related stuff begins
# initializing root
root = Tk()
root.title("Contagion")
root.resizable(False, False)
# initializing canvas
canvas = Canvas(root, width=1000, height=500)
canvas.pack()
root.update_idletasks()
# Window-related stuff ends

world = World(canvas)

# call when resizing
# world.update_points()
world.run(70, 40)

root.mainloop()
