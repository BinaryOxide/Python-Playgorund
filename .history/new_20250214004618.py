import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Modern Clock")
root.geometry("400x150")
root.configure(bg='black')

# Set your desired font properties here
FONT_FAMILY = "Arial"  # Change to any font you like, e.g., "Times New Roman", "Courier"
FONT_SIZE = 48         # Change the font size
FONT_WEIGHT = "bold"   # Set to "bold" for bold text, or "normal" for regular text
FONT_COLOR = "#00FF00" # Set the font color (e.g., "#FF0000" for red, "#00FF00" for green)

# Function to update the time
def update_time():
    current_time = strftime('%H:%M:%S %p')  # Get the current time in HH:MM:SS AM/PM format
    clock_label.config(text=current_time)   # Update the label with the current time
    clock_label.after(1000, update_time)   # Schedule the function to run again after 1000ms (1 second)

# Create a label to display the time
clock_label = tk.Label(
    root,
    font=(FONT_FAMILY, FONT_SIZE, FONT_WEIGHT),  # Set font family, size, and weight
    fg=FONT_COLOR,                               # Set font color
    bg='black'                                   # Set background color
)
clock_label.pack(expand=True)

# Start the clock
update_time()

# Run the application
root.mainloop()