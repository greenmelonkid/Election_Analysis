import os
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
outfile = open(file_to_save, "w")
outfile.write("Hello World")
outfile.close()

# Create a filename variable to direct of indirect path to the file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World")

# Write three counties to the file.
with open(file_to_save, "w") as txt_file:

   txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

