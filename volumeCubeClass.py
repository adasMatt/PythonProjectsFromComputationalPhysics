""" 
This is a program that uses Class "App" (to be renamed "Cube") to take user input in the interface to compute and display the volume of a cube. 

->
-> Work on making another widget to show volume within the GUI instead of having the function print to the terminal. 
-> ctrl+f this one: self.entrythingy.bind

14Dec2022 Matt

"""

from tkinter import *

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = Entry()
        self.entrythingy.pack()

        # Create the cube length variable.
        self.length_input = DoubleVar()
        # Set it to some default value.
        self.length_input.set(2.0)
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.length_input

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.volume_compute)       # but I would like this to print below in a separate widget instead of being printed to terminal

    def volume_compute(self, event):
        print("The volume of a cube with the input length", self.length_input.get(), "is:", self.length_input.get()**3)


root = Tk()
myapp = App(root)
myapp.mainloop()