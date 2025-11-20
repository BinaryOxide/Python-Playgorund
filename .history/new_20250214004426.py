import tkinter as tk
from tkinter import font, colorchooser
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Modern Clock")
root.geometry("400x150")
root.configure(bg='black')

# Default font settings
font_family = "Helvetica"
font_size = 48
font_weight = "normal"
font_color = "white"

# Function to update the time
def update_time():
    current_time = strftime('%H:%M:%S %p')  # Get the current time in HH:MM:SS AM/PM format
    clock_label.config(text=current_time)   # Update the label with the current time
    clock_label.after(1000, update_time)   # Schedule the function to run again after 1000ms (1 second)

# Function to open settings menu
def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Clock Settings")
    settings_window.geometry("300x200")

    # Font Family
    tk.Label(settings_window, text="Font Family:").grid(row=0, column=0, padx=10, pady=10)
    font_family_entry = tk.Entry(settings_window)
    font_family_entry.insert(0, font_family)
    font_family_entry.grid(row=0, column=1, padx=10, pady=10)

    # Font Size
    tk.Label(settings_window, text="Font Size:").grid(row=1, column=0, padx=10, pady=10)
    font_size_entry = tk.Entry(settings_window)
    font_size_entry.insert(0, font_size)
    font_size_entry.grid(row=1, column=1, padx=10, pady=10)

    # Font Weight (Bold)
    tk.Label(settings_window, text="Bold:").grid(row=2, column=0, padx=10, pady=10)
    bold_var = tk.BooleanVar(value=(font_weight == "bold"))
    bold_checkbox = tk.Checkbutton(settings_window, variable=bold_var)
    bold_checkbox.grid(row=2, column=1, padx=10, pady=10)

    # Font Color
    tk.Label(settings_window, text="Font Color:").grid(row=3, column=0, padx=10, pady=10)
    color_button = tk.Button(settings_window, text="Choose Color", command=lambda: choose_color())
    color_button.grid(row=3, column=1, padx=10, pady=10)

    # Apply Button
    apply_button = tk.Button(settings_window, text="Apply", command=lambda: apply_settings(
        font_family_entry.get(),
        int(font_size_entry.get()),
        "bold" if bold_var.get() else "normal",
        font_color
    ))
    apply_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Function to choose font color
    def choose_color():
        global font_color
        color = colorchooser.askcolor()[1]  # Open color picker and get the chosen color
        if color:
            font_color = color

    # Function to apply settings
    def apply_settings(new_font_family, new_font_size, new_font_weight, new_font_color):
        global font_family, font_size, font_weight, font_color
        font_family = new_font_family
        font_size = new_font_size
        font_weight = new_font_weight
        font_color = new_font_color
        clock_label.config(font=(font_family, font_size, font_weight), fg=font_color)
        settings_window.destroy()

# Create a label to display the time
clock_label = tk.Label(root, font=(font_family, font_size, font_weight), fg=font_color, bg='black')
clock_label.pack(expand=True)

# Add a settings button
settings_button = tk.Button(root, text="⚙️", font=("Arial", 12), command=open_settings)
settings_button.pack(side=tk.BOTTOM, pady=10)

# Start the clock
update_time()

# Run the application
root.mainloop()