import os
import bz2

# this path must exist
destination_folder = "C:\\Users\\jiri.pillar\\PycharmProjects\\Facer\\dlib"
compressed_files_path = "C:\\Users\\jiri.pillar\\PycharmProjects\\Facer"

# get list with filenames (strings)
dirListing = os.listdir(compressed_files_path)

for file in dirListing:
    # ^ this is only filename.ext
    if ".bz2" in file:
        # concatenation of directory path and filename.bz2
        existing_file_path = os.path.join(compressed_files_path, file)

        # read the file as you want
        unpackedfile = bz2.BZ2File(existing_file_path)
        data = unpackedfile.read()

        new_file_path = os.path.join(destination_folder, file)
        with bz2.open(new_file_path, 'wb') as f:
            f.write(data)