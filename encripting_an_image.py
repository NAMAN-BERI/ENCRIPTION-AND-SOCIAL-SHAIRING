from PIL import Image

def modify_alpha(image_path, output_path,stego_key,auto_key):
    # Open the image file
    image = Image.open(image_path)

    # Get the width and height of the image
    width, height = image.size

    # Create a new image with RGBA mode
    new_image = Image.new("RGBA", (width, height))
    
    # ADDING AUTO KEY
    new_alpha = 255 - auto_key
    
    # INITIALIZING VARIABLES 
    check = True
    a = 0
    b = 0
    
    # Iterate through each pixel
    for y in range(height):
        for x in range(width):
            # Get the original pixel color with alpha
            original_color = image.getpixel((x, y))

            # Modify the alpha channel with the new_alpha value
            modified_color = original_color[:3] + (new_alpha,)

            # Set the modified pixel color in the new image
            new_image.putpixel((x, y), modified_color)
            
            # ADDING DATA OF STEGO KEY
            if check:
                if b == len(str(stego_key[a])):
                    a += 1
                    b = 0
                    new_alpha = 254
                else:
                    new_alpha = 255 - int(str(stego_key[a])[b]) - 2
                    b += 1
            else:
                new_alpha = 255
            if a == len(stego_key) and check:
                check = False

    # Save the new image
    new_image.save(output_path)

def encripting_image(stego_key,auto_key):
    # Replace 'input_image.png' with the path to your input image with alpha channel (PNG format)
    input_image_path = 'download_image.jpg'

    # Replace 'output_modified_image.png' with the desired output path
    output_image_path = 'output_modified_image.png'

    # Specify the new alpha value (0 for fully transparent, 255 for fully opaque)
    # Example: Set the new alpha to 128
    alpha = "abcdefghijklmnopqrstuvwxyz"
    auto_key = alpha.index(auto_key)

    # Call the modify_alpha function
    modify_alpha(input_image_path, output_image_path,stego_key,auto_key)

    print("Image encripted successfully.")
