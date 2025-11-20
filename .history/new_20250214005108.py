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
    background_image = tk.PhotoImage(file="G:\personalization\wallpaper\AESTHETIC\ff9235cd827885e439aef1bb9e153754_upscayl_3x_realesrgan-x4plus.png )  # Replace with your image path
except Exception as e:
    print(f"Error loading image: {e}")
    background_image = None

# Create a canvas to hold the background image and the clock
canvas = tk.Canvas(root, width=800, height=400)
canvas.pack(fill="both", expand=True)

# Add the background image to the canvas
if background_image: