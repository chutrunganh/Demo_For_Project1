import os

def delete_files(directory):
    # Potential security issue: directory traversal vulnerability
    # This function deletes files within a specified directory,
    # but it does not properly sanitize the input 'directory'.
    # An attacker could potentially traverse to other directories.
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Potential security issue: unintended file deletion
            # The code does not check if the file_path is within the intended directory
            # and could accidentally delete files outside of it if 'directory' is not properly sanitized.
            os.remove(file_path)

if __name__ == "__main__":
    # User input for directory path
    directory_path = input("Enter the directory path to delete files: ")
    delete_files(directory_path)

