import os
import shutil

# Define the source directory containing the images
source_directory = "results/faces/test_latest/images"

# Define the destination directories
input_directory = 'input_dir'
output_directory = 'output_dir'

# Create the destination directories if they don't exist
os.makedirs(input_directory, exist_ok=True)
os.makedirs(output_directory, exist_ok=True)

# Iterate over the files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith('_real_B.png'):
        # Move the file to the input directory
        src = os.path.join(source_directory, filename)
        dst = os.path.join(input_directory, filename[:-11] + '.png')  # Remove '_real_B' suffix
        shutil.copy(src, dst)
    elif filename.endswith('_rec_B.png'):
        # Move the file to the output directory
        src = os.path.join(source_directory, filename)
        dst = os.path.join(output_directory, filename[:-11] + '.png')  # Remove '_rec_B' suffix
        shutil.copy(src, dst)
