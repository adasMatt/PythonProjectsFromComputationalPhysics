# ttk tutorial.py but with a button added.
# in progress, haven't started besides copy/pasting from tutorial and adding note about where to potentially put the button.
# 15Dec - Matt

import tkinter as tk

root = tk.Tk()

# Define a function
def print_contents(event):
        print("Hi. The current entry content is:",
              contents.get())

def button_print_contents(*args):
        print("Hi. The current entry content is:",
              contents.get())

# Create and place widget
entrythingy = tk.Entry()
entrythingy.pack()

# Create the application variable.
contents = tk.StringVar()
# Set it to some value.
contents.set("this is a variable")
# Tell the entry widget to watch this variable.
entrythingy["textvariable"] = contents

# Is "callback" incorrect terminology for this now?
# Define a callback for when the user hits return.
# It prints the current value of the variable.
entrythingy.bind('<Key-Return>',
                        print_contents)
buttonthingy = tk.Button(text="button", command=button_print_contents).pack()

root.mainloop()

'''

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)
    
        #self.buildbutton(self)
    
    # Same error everywhere, this goes in hand with self.buildbutton above
    #def buildbutton(self, *args):
    #    self.buttonthingy = tk.Button(text="button", command=self.print_contents).pack()

    
    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())'''


        #self.buildbutton(self)

################################################
        # IS IT FAILING BECAUSE IT CAN'T BE PART OF THE __init__(self, master)?
        # LET'S TRY ADDING A BUTTON TO DO THE SAME THING
        # GUI starts, but clicking the button yields error:
        # AppData\Local\Programs\Python\Python311\Lib\tkinter\__init__.py", line 1948, in __call__
        # return self.func(*args)
        #   ^^^^^^^^^^^^^^^^
        # TypeError: App.print_contents() missing 1 required positional argument: 'event'
        # self.buttonthingy = tk.Button(text="button", command=self.print_contents).pack()
# still have the button on GUI and same error as calling within __init__ inside the class.
#buttonthingy = tk.Button(text="button", command=print_contents).pack()

#root.mainloop()