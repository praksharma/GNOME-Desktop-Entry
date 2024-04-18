import tkinter as tk
import customtkinter

# A flag to choose between legacy theme or customtkinter theme
# For the entire dev process we will use the legacy theme
theme = False


# make a class to employ legacy theme or customtheme based on the theme flag.
"""    
# Create as customtkinter window
#root = customtkinter.CTk()
# Setting up the theme for the app
customtkinter.set_appearance_mode("dark")

# setting up the component themes
customtkinter.set_default_color_theme("green")
"""

# Make legacy window
root = tk.Tk()
root.title("Hello Tkinter")
root.geometry("300x400")



# 

# Create a button widget
button = tk.Button(root, text="Click Here")
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Start the GUI event loop
root.mainloop()
