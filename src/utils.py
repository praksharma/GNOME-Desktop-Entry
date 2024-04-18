import os
import glob
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

def root_window_selector(theme, theme_name):
    """
    Retuns the root window depending on the theme flag and theme_name
    """
    if theme:
        print(f"Applying the {theme_name}")
        return ThemedTk(theme=theme_name)
    print("Applying the legacy theme")
    return tk.Tk()

def themed_widget(widget_type, theme):
    """
    Returns a themed widget if theme is True, otherwise returns a standard tk widget.
    """
    if theme:
        # Return the ttk (themed) version of the widget
        return getattr(ttk, widget_type)
    # Return the standard tk version of the widget
    return getattr(tk, widget_type)

class custom_tk:
    """
    A class to dynamically use the object of this class as a placeholder for tk or ttk based on the value of theme flag.
    """
    def __init__(self, theme=True):
        self._theme = theme
        self._tk = tk
        self._ttk = ttk

    def __getattr__(self, item):
        if self._theme:
            # Try returning the attribute from ttk
            try:
                return getattr(self._ttk, item)
            except AttributeError:
                pass
        # Fallback to tk if not found in ttk
        return getattr(self._tk, item)
