# Imports the tkinter module and components
import tkinter as tk
from tkinter import messagebox, ttk

# Inventory list 
inventory = []

# Main window setup
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("800x600")

# Main frame creation
main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True)

# Title and formatting for main frame 
tk.Label(main_frame, text="Inventory Management", font=("Arial", 14)).pack(pady=10)

# Entry field for item name
tk.Label(main_frame, text="Item Name").pack()
name_entry = tk.Entry(main_frame)
name_entry.pack()

# Entry field for item description
tk.Label(main_frame, text="Description").pack()
description_entry = tk.Entry(main_frame)
description_entry.pack()

# Entry field for Quantity
tk.Label(main_frame, text="Quantity").pack()
quantity_entry = tk.Entry(main_frame)
quantity_entry.pack()

root.mainloop()
