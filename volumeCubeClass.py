""" 
This is a program that uses Class "App" (to be renamed "Cube") to take user input in the interface to compute and display the volume of a cube. 
https://docs.python.org/3/library/tkinter.html#tk-option-data-types 

->
-> Work on making another widget to show volume within the GUI instead of having the function print to the terminal. 
-> ctrl+f this one: action = , AND buttonthingy, and maybe.. self.entrythingy.bind,

14Dec2022 Matt

"""

from tkinter import *
from tkinter import ttk

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()

        # making tkinter variables
        #self.volume = DoubleVar()
        self.volume = StringVar()
        #meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        self.length_input = StringVar()
        # Set it to some default value.
        self.length_input.set(2.0)

        # making widgets
        self.lengthEntry = Label(text="Enter side length: ").grid(column=0,row=0)
        self.entrythingy = Entry()
        self.entrythingy.grid(column=1,row=0)
        
        self.volumeCalculated = Label(text="Volume of this cube is: ").grid(column=0,row=1)
        self.labelthingy = Label(textvariable=self.volume)
        self.labelthingy.grid(column=1,row=1)
        self.buttonthingy = ttk.Button(text="Compute", command=self.button_volume_compute)
        self.buttonthingy.grid(column=1,row=2)
        
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.length_input        

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.volume_compute)
        
    def volume_compute(self, event):
        #this just prevents errors from string inputs instead of numbers
        try:
            length = self.length_input.get()
            self.volume.set(int(float(length)**3.0 * 10000)/10000.0)        
        except ValueError:
            pass
    
    # Rewritten from volume_compute above but with *args instead of event as the argument
    def button_volume_compute(self, *args):
        try:
            length = self.length_input.get()
            self.volume.set(int(float(length)**3.0 * 10000)/10000.0)        
        except ValueError:
            pass



root = Tk()
root.title("Volume of Cube")
myapp = App(root)
myapp.mainloop()