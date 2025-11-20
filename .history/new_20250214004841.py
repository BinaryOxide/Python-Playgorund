import tkinter as tk
from time import strftime
from PIL import Image, ImageTk, ImageFilter  # Pillow library for image manipulation

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

# Load and blur the background image
def load_and_blur_image(image_path, blur_radius=10):
    # Open the image
    image = Image.open(image_path)
    # Resize the image to fit the window
    image = image.resize((800, 400), Image.Resampling.LANCZOS)  # Adjust size as needed
    # Apply Gaussian blur
    blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))
    return ImageTk.PhotoImage(blurred_image)

# Load the blurred background image
background_image = load_and_blur_image("background.jpg")  # Replace with your image path

# Create a canvas to hold the background image and the clock
canvas = tk.Canvas(root, width=800, height=400)
canvas.pack(fill="both", expand=True)

# Add the blurred background image to the canvas
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
    bg='black'                                   # Set background color (transparent)
)
clock_label.pack(expand=True)

# Place the clock label on top of the canvas
canvas.create_window(400, 200, window=clock_label)  # Center the clock

# Start the clock
update_time()

# Run the application
root.mainloop()