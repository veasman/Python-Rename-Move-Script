# Basic imports for handling the file system.
import os
import shutil

# Get directory for the folder the script is in.
cur_dir = os.path.abspath(__file__)

# Get the name of the currect script.
cur_script = os.path.basename(__file__)

# The script name is included in the string when you get current
# directory, so set cur_dir to itself without the script name.
# Doing this just makes it easier to change a file's directory later.
cur_dir = cur_dir[:-len(cur_script)]

# Define a new directory to move the files to after renaming.
new_dir = cur_dir + "Personal Collection\\"

# Get a list of all files in the current directory.
files = os.listdir(cur_dir)

# Loop through every file to do some checks
for file in files:

	# Find the files with "redditsave.com-" in the name
    if file.find("redditsave.com-") != -1:

    	# Set new_name to the current file in the loop, then
    	# take out everything before the first "-" (which is "redditsave.com").
        new_name = file
        new_name = new_name[file.index("-") + 1:len(file)]

        # Rename the files to no longer contain "redditsave.com."
        os.rename(file, new_name)
        print(file + " renamed to " + new_name)

        # Move the files to the folder defined earlier.
        shutil.move(cur_dir + new_name, new_dir + new_name)
        print(new_name + " moved from " + cur_dir + " to " + new_dir)
