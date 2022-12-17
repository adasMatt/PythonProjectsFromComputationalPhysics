# ttk tutorial.py but with a button added.
# 16Dec - Matt

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

myapp.mainloop()