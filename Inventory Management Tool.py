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

root.mainloop()
