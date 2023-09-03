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

# Introduction
print("Welcome to the Image Distribution Script!")
print(f"We have {len(image_files)} images to distribute.")
print(f"We have {len(existing_destination_folders)} existing folders in the destination root.")

# Function to create a new folder
def create_new_folder():
    new_folder_count = 1
    while True:
        new_folder_name = f"MachineCreated_{new_folder_count}"
        if new_folder_name not in existing_destination_folders:
            new_folder_path = os.path.join(destination_root, new_folder_name)
            os.makedirs(new_folder_path)
            existing_destination_folders.append(new_folder_name)
            return new_folder_path
        new_folder_count += 1

# Iterate over each image and move to the next available folder
while image_files:
    if len(image_files) >= 3:
        images_to_move = image_files[:3]
        image_files = image_files[3:]
    else:
        images_to_move = image_files
        image_files = []

    if not existing_destination_folders:
        # Create a new folder if none exist
        new_folder_path = create_new_folder()
    else:
        # Use the next available folder
        new_folder_path = os.path.join(destination_root, existing_destination_folders.pop(0))

    # Move images to the destination folder
    for image in images_to_move:
        source_path = os.path.join(source_folder, image)
        destination_path = os.path.join(new_folder_path, image)

        # Skip files that are not valid images
        try:
            shutil.move(source_path, destination_path)
        except IsADirectoryError:
            print(f"Skipping {source_path} as it is not a valid image.")

    print(f"Moved {len(images_to_move)} images to {new_folder_path}")
final_destination_folders = [folder_name for folder_name in os.listdir(destination_root) if os.path.isdir(os.path.join(destination_root, folder_name))]
# Conclusion
print("Distribution complete!")
print(f"There are {len(image_files)} images remaining.")
print(f"There are {len(final_destination_folders)} folders in the destination root.")

# End of script
