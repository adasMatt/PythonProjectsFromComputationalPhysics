'''  Volume.py will be a GUI with input boxes that calculates volume given a set of inputs. 

It will start with the simplest shape, a cube, so that there is only one output and one input to start. Later versions will include a "picker" for the user to choose between various shapes (i.e.: cube, rectangular prism, sphere, etc.).

Dec 11 - Matt
'''
# note
#############################
# GUI widgets and variables #
#############################
from tkinter import *               # import all from tkinter
root=Tk()                           # create the root widget, max/min & close buttons, title bar
root.title("Cube Volume")
root.geometry("200x100")

# this only computes volume of a cube for now
def volume_calculation():
    
    #############################
    # code that computes volume #
    #############################

    volume_output = float(user_input_field_double.get())**3.0   # now that I changed user_input_field_double, volume output on the GUI is showing as zero
    volume_output_str = str(volume_output)
    return volume_output_str

#a = Label(root, text='Hello World!')
#a.pack()                           # sizes the Label above automatically
user_input_label = Label(root, text='side length').grid(row=0, column=0)
# k_min = DoubleVar(root, 2.5)
side_length_dbl = DoubleVar(root, 2.0)
# k_min_entry = ttk.Entry(mainframe, width=7, textvariable=k_min)
user_input_field_entry = Entry(root, textvariable=side_length_dbl).grid(row=0, column=1)  # label user input field
user_input_field_double = DoubleVar(user_input_field_entry)

volume_label = Label(root, text='volume').grid(row=1, column=0)
# volume_field_label = Label(root, text=volume_calculation()).grid(row=1, column=1)
# below modifiable number variables for now
volume_button = Button(root, text="Compute", command=volume_calculation()).grid(row=2, column=1)

'''
#button
file_me_button = ttk.Button(mainframe, text="Select File", command=select_file).grid(column=3, row=1, sticky=W)
#entry
file_me_entry = ttk.Entry(mainframe, textvariable=file_me).grid(column=2, row=1, sticky=W) '''

volume_field_label = Label(root, text=volume_calculation()).grid(row=1, column=1)

root.mainloop()










'''
VolumeAndSurfaceArea/Shared/Sphere.swift from Computational Physics course Sp 2021

https://github.com/adasMatt/VolumeAndSurfaceArea/blob/main/Shared/Sphere.swift 
.........................................................................
.........................................................................
import SwiftUI

class Sphere: NDimensionalObj, ObservableObject{
    
    var radius = 1.0

    @Published var surfAreaSphere = 0.0
    @Published var volSphere = 0.0
    @Published var surfAreaSphereText = ""
    @Published var volSphereText = ""
    
    func calculateSphereAreaAndVolume(passedRadius: Double){
        
        radius = passedRadius
        
        surfAreaSphere = 4 * Double.pi * radius * radius
        surfAreaSphereText = String(format: "%7.5f", surfAreaSphere)
        volSphere = 4 / 3 * Double.pi * radius * radius * radius
        volSphereText = String(format: "%7.5f", volSphere)
        return
    }

}

'''