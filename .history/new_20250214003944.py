import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Modern Clock")
root.geometry("400x150")
root.configure(bg='black')

# Function to update the time
def update_time():
    current_time = strftime('%H:%M:%S %p')  # Get the current time in HH:MM:SS AM/PM format
    clock_label.config(text=current_time)   # Update the label with the current time
    clock_label.after(1000, update_time)   # Schedule the function to run again after 1000ms (1 second)

# Create a label to display the time
clock_label = tk.Label(root, font=('Helvetica', 48), fg='white', bg='black')
clock_label.pack(expand=True)

# Start the clock
update_time()

# Run the application
root.mainloop()