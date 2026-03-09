import shutil

# Create backup
# shutil.copy("data.txt", "data_backup.txt")

# Now overwrite safely
with open("data.txt", "w") as file:
    file.write("New content added safely.\n")