import tkinter as tk
from tkinter import messagebox

def calculate_product(event=None): # Added 'event' to support Enter key binding
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        label_result.config(text=f"Product: {result:,.2f}", fg="green") # Added formatting
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

def clear_fields():
    entry1.delete(0, tk.END)
    entry2.get()
    entry2.delete(0, tk.END)
    label_result.config(text="Product: ", fg="black")
    entry1.focus() # Put the cursor back in the first box

root = tk.Tk()
root.title("Product Calculator")
root.geometry("300x250")

# Using a simple padding configuration for all widgets
padx_val = 10
pady_val = 5

tk.Label(root, text="First Number:").pack(pady=pady_val)
entry1 = tk.Entry(root)
entry1.pack(pady=pady_val)
entry1.focus() # Start with the cursor here

tk.Label(root, text="Second Number:").pack(pady=pady_val)
entry2 = tk.Entry(root)
entry2.pack(pady=pady_val)

# Bind the Enter key to the calculation
root.bind('<Return>', calculate_product)

btn_multiply = tk.Button(root, text="Multiply", command=calculate_product, bg="#e1e1e1")
btn_multiply.pack(pady=10)

btn_clear = tk.Button(root, text="Clear", command=clear_fields)
btn_clear.pack()

label_result = tk.Label(root, text="Product: ", font=("Arial", 12, "bold"))
label_result.pack(pady=20)

import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        # Get numbers from Entry widgets
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        result = num1 * num2
        
        # Clear the Text box and insert the result
        # '1.0' means start at line 1, character 0
        text_result.config(state=tk.NORMAL) # Unlock for editing
        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, f"Result: {result}")
        text_result.config(state=tk.DISABLED) # Lock it back
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

# 1. Initialize the Window
root = tk.Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")
root.configure(bg="#f0f0f0") # Light grey background

# 2. Description Label
lbl_desc = tk.Label(root, text="This application calculates the product of two numbers.", 
                    wraplength=350, bg="#f0f0f0", font=("Arial", 10, "italic"))
lbl_desc.pack(pady=10)

# 3. Input Labels and Entry Widgets
tk.Label(root, text="Enter First Number:", bg="#f0f0f0").pack()
entry_num1 = tk.Entry(root, bg="#ffffff")
entry_num1.pack(pady=2)

tk.Label(root, text="Enter Second Number:", bg="#f0f0f0").pack()
entry_num2 = tk.Entry(root, bg="#ffffff")
entry_num2.pack(pady=2)

# 4. Calculation Button
# Hex code used for a nice 'Calculated' Blue
btn_calc = tk.Button(root, text="Calculate Product", command=calculate_product, 
                     bg="#3498db", fg="white", font=("Arial", 10, "bold"))
btn_calc.pack(pady=15)

# 5. Text Box for Result
# Height=1 makes it look more like a single-line result box
text_result = tk.Text(root, height=1, width=30, state=tk.DISABLED, bg="#ecf0f1")
text_result.pack(pady=5)

root.mainloop()