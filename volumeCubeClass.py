""" 
This is a program that uses Class "App" (to be renamed "Cube") to take user input in the interface to compute and display the volume of a cube. 
https://docs.python.org/3/library/tkinter.html#tk-option-data-types 

->
-> Work on making a parent class separate from the soon-to-be-renamed Cube class
-> ctrl+f: might be put into parent

14Dec2022 Matt

"""

from tkinter import *
from tkinter import ttk

class App(Frame):
    #everything within class "App" will be common to any shape.
    #this is where a picker will go for choosing a shape. This class will run, a shape will be chosen and the GUI widgets will change according to selected shape?

    def __init__(self, master):                     
        super().__init__(master)
        self.grid()

        self.volume = StringVar()                   

# will inherit variables from "App" that are common to any other shape, then will calculate volume of a cube
class Cube(App):
    def __init__(self, master):                     # might be put into parent
        super().__init__(master)
        self.grid()

        # making tkinter variables
        #self.volume = StringVar()                   # might be put into parent
        
        self.length_input = StringVar()
        # Set it to some default value.
        self.length_input.set(2.0)

        # making widgets
        self.lengthEntry = Label(text="Enter side length: ").grid(column=0,row=0)
        
        self.entrythingy = Entry()                  # might be put into parent
        self.entrythingy.grid(column=1,row=0)       # might be put into parent
        
        self.volumeCalculated = Label(text="Volume of this cube is: ").grid(column=0,row=1)
        
        self.labelthingy = Label(textvariable=self.volume) # might be put into parent
        self.labelthingy.grid(column=1,row=1)              # might be put into parent
        
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
            self.volume.set("")
            #pass
    
    # Rewritten from volume_compute above but with *args instead of event as the argument
    def button_volume_compute(self, *args):
        try:
            length = self.length_input.get()
            self.volume.set(int(float(length)**3.0 * 10000)/10000.0)        
        except ValueError:
            self.volume.set("")
            #pass

# will inherit variables from "App" that are common to any other shape, then will calculate volume of a sphere


root = Tk()
root.title("Volume of Something")

myapp = Cube(root)
#myapp = App(root)           #keep this for when there is a picker or something
myapp.mainloop()