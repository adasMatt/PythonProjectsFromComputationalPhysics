""" 
This is a program that will use Class "App" to take user input in the form of a "picker" choice to select a shape of which to compute the volume of. The GUI label widgets will change based on this input and then the interface will take a new input for a length (side of cube, radius of sphere, etc) and it will then compute and display the volume of the selected shape. 
https://docs.python.org/3/library/tkinter.html#tk-option-data-types 

->
-> Work on parent "App" class 
-> ctrl+f: might be put into parent, I want

14Dec2022 Matt

"""

from tkinter import *
from tkinter import ttk
from numpy import pi

class App(Frame):
    #everything within class "App" will be common to any shape.
    #this is where a picker will go for choosing a shape. This class will run, a shape will be chosen and the GUI widgets will change according to selected shape?
    def __init__(self, master):                     
        super().__init__(master)
        self.grid()
        
        self.volume = StringVar()

        self.length_input = StringVar()
        # Set it to some default value.
        self.length_input.set(2.0)
        # I want the fields to be disabled before user selects a shape?
        self.entrythingy = Entry()                  # might be put into parent
        self.entrythingy.grid(column=1,row=0)       # might be put into parent
        self.volume_field_label = Label(textvariable=self.volume) # might be put into parent
        self.volume_field_label.grid(column=1,row=1)              # might be put into parent
        self.entrythingy["textvariable"] = self.length_input     

        

# will inherit variables from "App" that are common to any other shape, then will calculate volume of a cube
class Cube(App):
    def __init__(self, master):                     
        super().__init__(master)
        self.grid()

        # making widgets
        self.lengthEntry = Label(text="Enter side length: ").grid(column=0,row=0)
        
        self.volumeCalculated = Label(text="Volume of this cube is: ").grid(column=0,row=1)
        
        self.buttonthingy = ttk.Button(text="Compute", command=self.button_volume_compute)
        self.buttonthingy.grid(column=1,row=2)
        
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
class Sphere(App):
    def __init__(self, master):                     
        super().__init__(master)
        self.grid()
        
        self.length_input.set(0.90856)
        # ~0.90856 is the cube root of 0.75 which will be used as default for Sphere

        # making widgets
        self.lengthEntry = Label(text="Enter radius length: ").grid(column=0,row=0)
        
        self.volumeCalculated = Label(text="Volume of this sphere is: ").grid(column=0,row=1)
        
        self.buttonthingy = ttk.Button(text="Compute", command=self.button_volume_compute)
        self.buttonthingy.grid(column=1,row=2)
        
        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.volume_compute)
        
    def volume_compute(self, event):
        #this just prevents errors from string inputs instead of numbers
        try:
            radius = self.length_input.get()
            self.volume.set(int((4/3)*pi*float(radius)**3.0 * 10000)/10000.0)        
        except ValueError:
            self.volume.set("")
            #pass
    
    def button_volume_compute(self, *args):
        #this just prevents errors from string inputs instead of numbers
        try:
            radius = self.length_input.get()
            self.volume.set(int((4/3)*pi*float(radius)**3.0 * 10000)/10000.0)        
        except ValueError:
            self.volume.set("")

root = Tk()
root.title("Volume of Something")

#myapp = Cube(root)
myapp = Sphere(root)
#myapp = App(root)           #keep this for when there is a picker or something
myapp.mainloop()