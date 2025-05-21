import os

def find_large_files(root_dir, size_mb=100):
    """
    Recursively search for files larger than 'size_mb' megabytes in the given directory.
    Prints the file path and its size.
    """
    size_bytes = size_mb * 1024 * 1024
    print(f"Searching for files larger than {size_mb} MB in '{root_dir}'...\n")
    found = False
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                if file_size >= size_bytes:
                    print(f"{file_path} - {file_size // (1024 * 1024)} MB")
                    found = True
            except (FileNotFoundError, PermissionError):
                continue
    if not found:
        print("No large files found.")

if __name__ == "__main__":
    directory = input("Enter the path to the directory you want to scan: ").strip()
    if os.path.isdir(directory):
        try:
            size = int(input("Enter the minimum file size in MB to search for (default 100): ").strip() or "100")
        except ValueError:
            print("Invalid size; using default of 100 MB.")
            size = 100
        find_large_files(directory, size_mb=size)
    else:
        print("Directory not found.")
