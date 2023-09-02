import os
import random
import shutil

# Paths
source_folder = r'/Users/jag_diya/Photos/timescreen'  # Change this to the path of your source images folder
destination_root = r'/Users/jag_diya/Photos/timescreenone'  # Change this to the root path where you want to create the destination folders

# List all image files
image_files = [f for f in os.listdir(source_folder) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

# Shuffle the image list randomly
random.shuffle(image_files)

# Create a list of existing destination folders
existing_destination_folders = [folder_name for folder_name in os.listdir(destination_root) if os.path.isdir(os.path.join(destination_root, folder_name))]

# Iterate over each folder and move 25 random images
for folder_name in existing_destination_folders:
    folder = os.path.join(destination_root, folder_name)

    if len(image_files) >= 3:
        images_to_move = image_files[:3]
        image_files = image_files[3:]
    else:
        images_to_move = image_files
        image_files = []

    # Move images to the destination folder
    if images_to_move:
        for image in images_to_move:
            source_path = os.path.join(source_folder, image)
            destination_path = os.path.join(folder, image)

            # Skip files that are not valid images
            try:
                shutil.move(source_path, destination_path)
            except IsADirectoryError:
                print(f"Skipping {source_path} as it is not a valid image.")

        print(f"Moved {len(images_to_move)} images to {folder}")
    else:
        print(f"No images to move to {folder}")

print("All images moved.")
