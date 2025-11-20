import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Modern Clock")
root.geometry("400x150")
root.configure(bg='black')

# Initial font size
font_size = 48
font =" bold"
fon
# Function to update the time
def update_time():
    current_time = strftime('%H:%M:%S %p')  # Get the current time in HH:MM:SS AM/PM format
    clock_label.config(text=current_time)   # Update the label with the current time
    clock_label.after(1000, update_time)   # Schedule the function to run again after 1000ms (1 second)

# Function to adjust font size
def adjust_font_size(event):
    global font_size
    if event.keysym == "plus" or event.delta > 0:  # Ctrl + '+' or Mouse Wheel Up
        font_size += 5
    elif event.keysym == "minus" or event.delta < 0:  # Ctrl + '-' or Mouse Wheel Down
        font_size -= 5
    # Ensure font size doesn't go below 10
    font_size = max(10, font_size)
    # Update the font size of the clock label
    clock_label.config(font=('Helvetica', font_size))

# Create a label to display the time
clock_label = tk.Label(root, font=('Helvetica', font_size), fg='white', bg='black')
clock_label.pack(expand=True)

# Bind keyboard and mouse wheel events
root.bind("<Control-plus>", adjust_font_size)  # Ctrl + '+'
root.bind("<Control-minus>", adjust_font_size)  # Ctrl + '-'
root.bind("<Control-MouseWheel>", adjust_font_size)  # Ctrl + Mouse Wheel

# Start the clock
update_time()

# Run the application
root.mainloop()