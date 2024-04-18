import os
import glob
import tkinter as tk
from ttkthemes import ThemedTk

def root_window_selector(theme, theme_name):
    if theme:
        print(f"Applying the {theme_name}")
        return ThemedTk(theme=theme_name)
    print("Applying the legacy theme")
    return tk.Tk()