import shutil
import os
# 1
RootDir1 = r'/Users/jag_diya/Photos/Dees google photos'
TargetFolder = r'/Users/jag_diya/Photos/google_photos'
total_files = 0
file_types_available = set()
file_types_two = set()
for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
        # print(root)
        print(dirs)
        # print(files)
        for name in files:
            # To get all file types
            if "." in name:
                x = [a for a in name.split('.')]
                user = '.'.join(x[-1:])
                file_types_available.add(user)
            # SourceFolder = os.path.join(root, name)
            # print(SourceFolder)
            # shutil.copy2(SourceFolder, TargetFolder)
            avoid = ('.json', '.JPG')
            if not name.endswith(avoid):
                total_files += 1
                SourceFolder = os.path.join(root, name)
                print(os.path.join(root, name))
            shutil.copy2(SourceFolder, TargetFolder) #copies csv to new folder
print(total_files)

print(file_types_available)
print(file_types_two)
