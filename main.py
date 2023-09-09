import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Global variables

watermark = Image.open("watermark.png")
file_path = ""

# Function that allows the user to choose a .jpg image

def open_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg")])
    apply_watermark()

# Function that resizes the watermark depending on the background image's dimensions

def resize_watermark():
    background_img = Image.open(file_path)
    width_ratio = background_img.width / watermark.width
    height_ratio = background_img.height / watermark.height
    min_ratio = min(width_ratio, height_ratio)
    resize_factor = 0.3
    new_width = int(watermark.width * min_ratio * resize_factor)
    new_height = int(watermark.height * min_ratio * resize_factor)
    resized_watermark = watermark.resize((new_width, new_height), Image.Resampling.LANCZOS)
    return resized_watermark, new_width, new_height, background_img

# Function that puts the watermark on top of the chosen image

def apply_watermark():
    resized_watermark, new_width, new_height, background_img = resize_watermark()
    x = background_img.width - new_width
    y = background_img.height - new_height
    background_img.paste(resized_watermark, (x, y), mask=resized_watermark)
    background_img.save(file_path)

# Create a tkinter window
root = tk.Tk()
root.geometry("400x100")
root.title("Open JPG File")

# Add a simple description

label = tk.Label(root, text="Please choose a .jpg file to mark with the predefined watermark")
label.pack(expand=True)

# Create a button to open the file dialog
open_button = tk.Button(root, text="Open JPG File", command=open_file)
open_button.pack(expand=True)

root.mainloop()
