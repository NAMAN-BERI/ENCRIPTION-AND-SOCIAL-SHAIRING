import requests
import io
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Global variables to store image data
current_image_data = None
next_window = None
root = None  # Define root as a global variable

# define a function to retrieve and display an image based on the selected category
def display_image(category):
    global current_image_data

    # make a request to the Unsplash API to get a random image
    url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=CpGRuOLkqZ-TeH4Ss1Vk2Bk8sODjwh7PS2D4E0nN4AA"
    data = requests.get(url).json()
    img_data = requests.get(data["urls"]["regular"]).content
    
    photo = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)).resize((600, 400), resample=Image.LANCZOS))
    label.config(image=photo)
    label.image = photo

    # Store the current image data
    current_image_data = data

    # Enable the download button
    download_button.config(state="normal")

# function to enable/disable the "Generate Image" button
def enable_button(*args):
    generate_button.config(state="normal" if category_var.get() != "Choose Category" else "disabled")
    # Disable the download button when generating a new image
    download_button.config(state="disabled")

# function to handle image download
def download_image():
    global current_image_data

    if current_image_data:
        # Get the image URL from the stored image data
        image_url = current_image_data["urls"]["regular"]

        # Download the image
        response = requests.get(image_url)
        with open("download_image.jpg", "wb") as file:
            file.write(response.content)

# create the GUI elements
def create_gui():
    global category_var, generate_button, download_button, label, next_button, root

    root = tk.Tk()  # Initialize root as a global variable



    # create a dropdown menu for selecting the category
    category_var = tk.StringVar(value="Choose Category")
    category_options = ["Choose Category", "Food", "Animals", "People", "Music", "Art", "Vehicles", "Random"]
    category_dropdown = ttk.OptionMenu(root, category_var, *category_options, command=enable_button)
    category_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    category_dropdown.config(width=14)

    # create a button for generating the image
    generate_button = ttk.Button(root, text="Generate Image", state="disabled", command=lambda: display_image(category_var.get()))
    generate_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # create a button for downloading the image
    download_button = ttk.Button(root, text="Download Image", state="disabled", command=download_image)
    download_button.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

    label = tk.Label(root, background="white")
    label.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    # make the columns/rows expandable
    root.columnconfigure([0, 1, 2, 3], weight=1)
    root.rowconfigure(1, weight=1)
    root.mainloop()

if __name__ == '__main__':
    create_gui()
