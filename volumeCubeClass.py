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
        self.pack()

        self.entrythingy = Entry()
        self.entrythingy.pack()

        # to use textvariable in a Label, the variable needs to be first declared and THEN set to a value. Cannot set the value within DoubleVar() such as DoubleVar("8.0").
        self.defaultvol = DoubleVar()
        self.defaultvol.set(8.0)
        
        #self.outputthingy = Label(root, textvariable=self.defaultvol)
        self.outputthingy = Label(textvariable=self.defaultvol)     # did not need root here
        self.outputthingy.pack()
        self.outputthingy["textvariable"] = 8.0

        self.cubed = DoubleVar()
        self.cubed.set(3.0)

        # Create the cube length variable.
        self.length_input = DoubleVar()
        # Set it to some default value.
        self.length_input.set(2.0)
        
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.length_input        

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.volume_compute)

        #######################################################
        #first things first I have a button, this is great. However I would like clicking the button to do the same as pressing return key for now.
        # Next I would like this to print in a separate widget instead of being printed to terminal
        self.buttonthingy = ttk.Button(text="Compute", command=self.button_volume_compute)
        self.buttonthingy.pack()
        
    # Rewritten from volume_compute used in Entry but with *args instead of event as the argument
    def button_volume_compute(self, *args):

        length = self.length_input.get()
        volume = length**self.cubed.get()
        print("The volume of a cube with sides of length", length, "is:", volume)

    # this prints result to terminal
    def volume_compute(self, event):
        
        length = self.length_input.get()
        volume = length**self.cubed.get()
        print("The volume of a cube with sides of length", length, "is:", volume)
        


root = Tk()
myapp = App(root)
myapp.mainloop()