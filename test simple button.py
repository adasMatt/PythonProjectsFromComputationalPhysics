# ttk tutorial.py but with a button added.
# in progress, haven't started besides copy/pasting from tutorial and adding note about where to potentially put the button.
# 15Dec - Matt

import tkinter as tk

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
        
        self.buttonthingy = tk.Button(text="button", command=self.button_print_contents).pack()

    def button_print_contents(self, *args):
        # but it does the same thing just with a different argument, is there a way to call the function print_contents and avoid the "event" error?
        print("Hi. The current entry content is:",
              self.contents.get())

    
    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)               # sends root = tk.Frame back to the class App

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
#buttonthingy = tk.Button(text="button", command=myapp.print_contents).pack()

myapp.mainloop()