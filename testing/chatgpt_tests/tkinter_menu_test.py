import tkinter as tk
from tkinter import ttk

def on_button_click():
    print("Button clicked")

def on_toggle_change():
    print("Toggle changed:", toggle_var.get())

# Create the main window
root = tk.Tk()
root.title("Video Game Interface")

# Set the window size
window_width = 600
window_height = 400
root.geometry(f"{window_width}x{window_height}")

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(root)

# Tab 1
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Tab 1")

button1 = ttk.Button(tab1, text="Click Me", command=on_button_click)
button1.pack(padx=10, pady=10)

# Tab 2
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Tab 2")

toggle_var = tk.StringVar()
toggle_button = ttk.Checkbutton(tab2, text="Toggle", variable=toggle_var, command=on_toggle_change)
toggle_button.pack(padx=10, pady=10)

# Place the notebook in the main window
notebook.pack(expand=True, fill="both")

# Start the Tkinter event loop
root.mainloop()
