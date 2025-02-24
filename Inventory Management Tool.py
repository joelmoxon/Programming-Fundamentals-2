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

# Defines a function to add items to the inventory
def add_item():
    name = name_entry.get()
    description = description_entry.get()

# Handles any errors with the entered value for the quantitiy field
    if not quantity_entry.get():
        messagebox.showerror("Error", "Quantity field cannot be empty")
        return
        
    try:
        quantity = int(quantity_entry.get())
        if quantity < 0:
            messagebox.showerror("Error", "Quantity cannot be negative")
            return
    except ValueError:
        messagebox.showerror ("Error", "Quantity must be a whole number")
        return

# Adds the validated item to the inventory list
    inventory.append({
        "Name": name,
        "Description": description,
        "Quantity": quantity
    })

# Creates a button to call the add item function
button_frame = tk.Frame(main_frame)
button_frame.pack(pady=10)
tk.Button(button_frame, text="Add Item", command=add_item).pack(side=tk.LEFT, padx=5)

root.mainloop()
