import tkinter as tk

def convert():
    inches = float(entry.get())
    centimeters = inches * 2.54
    result_label.config(text=f"{centimeters:.2f} cm")

# Create window
root = tk.Tk()
root.title("Length Converter")

# Input label
tk.Label(root, text="Enter length in inches:").pack()

# Input box
entry = tk.Entry(root)
entry.pack()

# Convert button
tk.Button(root, text="Convert", command=convert).pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run application
root.mainloop()