import os 

from PIL import Image

######### Change this to the directory you want to read #########
import_dir = '2023-05-coffee-series/upscaled'

######### Set the output directory path #########
output_dir = '2023-05-coffee-series/dpi'
os.makedirs(output_dir, exist_ok=True) # Create the output directory if it doesn't exist

# Set the path to the input and output images
input_image_path = "input.png"
output_image_path = "output.png"

# Set the new DPI value
new_dpi = (300, 300)

# Go through all files in the import directory
for filename in os.listdir(import_dir):
    if os.path.isfile(os.path.join(import_dir, filename)):
        print("File is: " + filename)
        

        # Set the image file path
        input_image_path = os.path.join(import_dir, filename)
        output_image_path = os.path.join(output_dir, filename)
        print("img path is :" + input_image_path)

        try:
            # Open the input image and read its contents
            with Image.open(input_image_path) as image:
                # Get the existing DPI value
                old_dpi = image.info.get("dpi")

                # If the old DPI value is not None and matches the new DPI value, don't do anything
                if old_dpi is not None and old_dpi == new_dpi:
                    print("DPI value is already set to", old_dpi)
                    exit()

                # Set the new DPI value
                image.info["dpi"] = new_dpi

                # Save the output image with the new DPI value
                image.save(output_image_path, dpi=new_dpi)

                print("DPI value changed from", old_dpi, "to", new_dpi)
        except Exception as e:
            print("Something went wrong", e)