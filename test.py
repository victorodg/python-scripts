import os

# define the directory path
dir_path = "/"

# loop through each file and subdirectory in the directory
for root, dirs, files in os.walk(dir_path):
    for filename in files:
        # check if the file name contains "sync-conflict"
        if "sync-conflict" in filename:
            # create the file path
            file_path = os.path.join(root, filename)
            # delete the file
            os.remove(file_path)
