# Import Library
from tkinter import *
is_on = True


def switch():
    global is_on
    # Determine is on or off
    if is_on:
        second.deiconify()
        is_on = False
    else:
        second.withdraw()
        is_on = True


# Create Object
root = Tk()

# Set title
root.title("Main Window")

# Set Geometry
root.geometry("200x200")


# Open New Window
def launch():
    global second
    second = Toplevel()
    second.title("Child Window")
    second.geometry("400x400")


# Add Buttons
Button(root, text="launch Window", command=launch).pack(pady=10)
# Button(root, text="Show", command=show).pack(pady=10)
Button(root, text="Switch", command=switch).pack(pady=10)

# Execute Tkinter
root.mainloop()

