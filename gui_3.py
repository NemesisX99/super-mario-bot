from tkinter import *
from tkinter import messagebox  # Import the messagebox module
from PIL import Image, ImageTk
import subprocess

def submit_action():
    selected_option = var_option.get()
    print(f"Submitted! Selected option: {selected_option}")

    # Check the selected option
    if selected_option == "Select steps":
        messagebox.showinfo("Invalid Option", "Please select a valid option.")
    elif selected_option == "1 Lakh":
        subprocess.run(["python", "1_Lakh.py"])
    elif selected_option == "5 Lakh":
        subprocess.run(["python", "5_Lakh.py"])
    elif selected_option == "10 Lakh":
        subprocess.run(["python", "10_Lakh.py"])

def selected_option_action(*args):
    selected_option = var_option.get()
    print(f"Selected option: {selected_option}")

var1_root = Tk()
var1_root.geometry("638x800")

# Background image
background_image_path = "peakpx.jpg"
background_image = Image.open(background_image_path)
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = Label(var1_root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Overlay image
overlay_image_path = "cool5.png"  # Replace with the actual path to your overlay image file
overlay_image = Image.open(overlay_image_path)
overlay_photo = ImageTk.PhotoImage(overlay_image)

# Create a label to display the overlay image
overlay_label = Label(var1_root, image=overlay_photo)
overlay_label.place(x=48, y=85)  # Adjust the position as needed

# Submit button
submit_button = Button(var1_root, text="Let's Go", command=submit_action)
submit_button.place(x=300, y=700)

# Select Option
options = ["Select steps", "1 Lakh", "5 Lakh", "10 Lakh"]
var_option = StringVar(var1_root)
var_option.set(options[0])  # set the default option

# Create a trace to call selected_option_action when the option changes
var_option.trace_add('write', selected_option_action)

option_menu = OptionMenu(var1_root, var_option, *options)
option_menu.place(x=280, y=650)

var1_root.mainloop()
