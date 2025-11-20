import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Modern Clock")
root.geometry("800x400")  # Adjust window size as needed
root.configure(bg='black')

# Set your desired font properties here
FONT_FAMILY = "Arial"  # Change to any font you like, e.g., "Times New Roman", "Courier"
FONT_SIZE = 48         # Change the font size
FONT_WEIGHT = "bold"   # Set to "bold" for bold text, or "normal" for regular text
FONT_COLOR = "#FFFFFF" # Set the font color (e.g., "#FF0000" for red, "#00FF00" for green)

# Load the background image (using tkinter's PhotoImage)
try:
    background_image = tk.PhotoImage(file=import tkinter as tk from time import strftime)

# Create the main window
root = tk.Tk()
root.title("Modern Clock")
root.geometry("800x400")  # Adjust window size as needed
root.configure(bg='black')

# Set your desired font properties here
FONT_FAMILY = "Arial"  # Change to any font you like, e.g., "Times New Roman", "Courier"
FONT_SIZE = 48         # Change the font size
FONT_WEIGHT = "bold"   # Set to "bold" for bold text, or "normal" for regular text
FONT_COLOR = "#FFFFFF" # Set the font color (e.g., "#FF0000" for red, "#00FF00" for green)

# Load the background image (using tkinter's PhotoImage)
try:
    background_image = tk.PhotoImage(file=import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Modern Clock")
root.geometry("800x400")  # Adjust window size as needed
root.configure(bg='black')

# Set your desired font properties here
FONT_FAMILY = "Arial"  # Change to any font you like, e.g., "Times New Roman", "Courier"
FONT_SIZE = 48         # Change the font size
FONT_WEIGHT = "bold"   # Set to "bold" for bold text, or "normal" for regular text
FONT_COLOR = "#FFFFFF" # Set the font color (e.g., "#FF0000" for red, "#00FF00" for green)

# Load the background image (using tkinter's PhotoImage)
try:
    background_image = tk.PhotoImage(file="G:\personalization\wallpaper\AESTHETIC\ff9235cd827885e439aef1bb9e153754_upscayl_3x_realesrgan-x4plus.png")  # Replace with your image path
except Exception as e:
    print(f"Error loading image: {e}")
    background_image = None

# Create a canvas to hold the background image and the clock
canvas = tk.Canvas(root, width=800, height=400)
canvas.pack(fill="both", expand=True)

# Add the background image to the canvas
if background_image:
    canvas.create_image(0, 0, image=background_image, anchor="nw")

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
    bg='',                                       # Set background color to transparent
)
clock_label.pack(expand=True)

# Place the clock label on top of the canvas
canvas.create_window(400, 200, window=clock_label)  # Center the clock

# Start the clock
update_time()

# Run the application
root.mainloop())  # Replace with your image path
except Exception as e:
    print(f"Error loading image: {e}")
    background_image = None

# Create a canvas to hold the background image and the clock
canvas = tk.Canvas(root, width=800, height=400)
canvas.pack(fill="both", expand=True)

# Add the background image to the canvas
if background_image:
    canvas.create_image(0, 0, image=background_image, anchor="nw")

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
    bg='',                                       # Set background color to transparent
)
clock_label.pack(expand=True)

# Place the clock label on top of the canvas
canvas.create_window(400, 200, window=clock_label)  # Center the clock

# Start the clock
update_time()

# Run the application
root.mainloop())  # Replace with your image path
except Exception as e:
    print(f"Error loading image: {e}")
    background_image = None

# Create a canvas to hold the background image and the clock
canvas = tk.Canvas(root, width=800, height=400)
canvas.pack(fill="both", expand=True)

# Add the background image to the canvas
if background_image:
    canvas.create_image(0, 0, image=background_image, anchor="nw")

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
    bg='',                                       # Set background color to transparent
)
clock_label.pack(expand=True)

# Place the clock label on top of the canvas
canvas.create_window(400, 200, window=clock_label)  # Center the clock

# Start the clock
update_time()

# Run the application
root.mainloop()