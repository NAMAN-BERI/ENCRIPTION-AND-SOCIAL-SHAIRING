from PIL import Image

def get_alpha_values(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Get the width and height of the image
    width, height = image.size

    # Create a list to store alpha values
    alpha_values = []

    # Iterate through each pixel
    for y in range(height):
        for x in range(width):
            # Get the RGBA values of the pixel
            r, g, b, a = image.getpixel((x, y))

            # Append the alpha value to the list
            alpha_values.append(a)

    return alpha_values

def decription_image():
    # Example usage
    image_path = "output_modified_image.png"
    alpha_values_list = get_alpha_values(image_path)
    
    # Now alpha_values_list contains the alpha values of all pixels in the image
    
    autokey = 255 - alpha_values_list.pop(0)
    num = ""
    data =[]
    for i in alpha_values_list:
        if i != 255:
            if i != 254:
                num = num + str(253-i)
            else:
                data.append(int(num))
                num = ""
    
    alpha = "abcdefghijklmnopqrstuvwxyz"
    autokey = alpha[autokey]
    
    print("Image decripted successfully.")
    return autokey, data

