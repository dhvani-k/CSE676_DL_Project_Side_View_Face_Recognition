from PIL import Image
import os

# Folder path containing the PNG images
folder_path = "faces/val"

# Output folder path for resized images
output_folder_path = "new_faces/val"

# Ensure the output folder exists
os.makedirs(output_folder_path, exist_ok=True)

# Iterate over each file in the folder
for file_name in os.listdir(folder_path):
    # Filter only PNG images
    if file_name.endswith(".png"):
        # Open the image file
        image_path = os.path.join(folder_path, file_name)
        image = Image.open(image_path)

        # Resize the image to 256x256 pixels
        resized_image = image.resize((512, 256))

        # Save the resized image
        output_path = os.path.join(output_folder_path, file_name)
        resized_image.save(output_path)

        # Close the image file
        image.close()
