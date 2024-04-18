import tkinter as tk
from tkinter import messagebox # submodule
from ttkthemes import ThemedTk

#import customtkinter
import os
import glob
from utils import root_window_selector

# A flag to choose between legacy theme or customtkinter theme
# For the entire dev process we will use the legacy theme
theme = True
theme_name = "winxpblue"


# make a class to employ legacy theme or customtheme based on the theme flag.
search_locations = {'local' : '/usr/share/applications/*.desktop',
                    'system' : '~/.local/share/applications/*.desktop'
                    } 

class DesktopEntryManager:
    """    
    #Create as customtkinter window
    root = customtkinter.CTk()
    #Setting up the theme for the app
    customtkinter.set_appearance_mode("dark")

    # setting up the component themes
    customtkinter.set_default_color_theme("green")
    """
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("GNOME Desktop Entry Manager")
        self.root.geometry("600x500")

        # create a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Load Entries", command=self.load_desktop_entries)
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.root.config(menu = self.menu_bar)

        # Labels top
        left = 0.02
        listbox_width = 0.65
        button_left = 0.7
        text_area_width = 0.95

        self.label_listbox = tk.Label(self.root, text = "List of all desktop entries")
        self.label_listbox.place(relx=left, rely=0.02)
        # Listbox
        self.listbox = tk.Listbox(self.root)
        self.listbox.place(relwidth=listbox_width, relheight=0.45, relx=left, rely=0.05)

        # Label bottom
        self.label_text_area = tk.Label(self.root, text = "Contents of desktop file")
        self.label_text_area.place(relx=left, rely=0.5)

        # Text area
        self.text_area = tk.Text(self.root, state='disabled')
        self.text_area.place(relwidth=text_area_width, relheight=0.4, relx=left, rely=0.53)

        # Buttons
        self.delete_button = tk.Button(self.root, text="Delete Entry")#, command=self.delete_entry)
        self.delete_button.place(relx=button_left, rely=0.2)

        self.view_button = tk.Button(self.root, text="View/Edit Entry", command=self.view_entry)
        self.view_button.place(relx=button_left, rely=0.3)

        # Scrollbar
        # Create the scrollbar
        self.scrollbar = tk.Scrollbar(self.root)

        # Place the scrollbar on the right side of the Listbox, filling the Y-axis
        self.scrollbar.place(relx=listbox_width+left, rely=0.05, relheight=0.45, anchor='ne')

        # Attach the scrollbar to the Listbox
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

    def load_desktop_entries(self):
        files = []
        for path in search_locations.values():
            files.extend(glob.glob(os.path.expanduser(path)))
        self.listbox.delete(0, tk.END)
        for file in files:
            self.listbox.insert(tk.END, file)

    def delete_entry_experimental(self):
        # Need human intervention
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No entry selected")
            return
        file_path = self.listbox.get(selected[0])
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {file_path}?"):
            os.remove(file_path)
            self.load_desktop_entries()
    def view_entry(self):
        self.text_area.config(state='normal')  # Enable widget to modify the text_area
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No entry selected")
            return
        file_path = self.listbox.get(selected[0])
        with open(file_path, 'r') as file:
            file_content = file.read()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, file_content)
        self.text_area.config(state='disabled')  # Disable widget to prevent user editing text_area

if __name__ == "__main__":
    root = root_window_selector(theme, theme_name)
    app = DesktopEntryManager(root)
    root.mainloop()
