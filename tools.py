import os, re

# Filter list based on a key word in the values
def positive_filter(dict, include_word):
    new = {k: v for k, v in dict.items() if include_word in v}
    return new

# swap key and value around
def key_swap(dictionary):
    new_dict = dict([(value, key) for key, value in dictionary.items()])
    return new_dict

# Filter list based on keyword
def filter_list(keyword, my_list):
    new_list = list(filter(lambda k: keyword in k, my_list))
    return new_list

# Add a "/" to the folder path if it is missing at the end of the string
def correct_path(folder):
    if re.search(r'.*(?<!\/)$', folder):
        folder += "/"
    return folder

# Remove files in temp folder
def remove_temp_files(temp_folder):
    for root, dirs, files in os.walk(temp_folder):
        for file in files:
            os.remove(os.path.join(root, file))


def remove_file_extension(filename):
    # Given a filename, removes the file extension and returns the name without it.
    return filename.rsplit(".", 1)[0]