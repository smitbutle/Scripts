import os
import hashlib

def hash_file(path, block_size=65536):
    hasher = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for block in iter(lambda: f.read(block_size), b""):
                hasher.update(block)
        return hasher.hexdigest()
    except Exception:
        return None

def find_duplicates(root_dir):
    hashes = {}
    duplicates = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = hash_file(file_path)
            if not file_hash:
                continue
            if file_hash in hashes:
                duplicates.append((file_path, hashes[file_hash]))
            else:
                hashes[file_hash] = file_path
    return duplicates

if __name__ == "__main__":
    directory = input("Enter the directory to search for duplicate files: ").strip()
    if not os.path.isdir(directory):
        print("Directory not found.")
    else:
        dups = find_duplicates(directory)
        if dups:
            print("Duplicate files found:")
            for dup, original in dups:
                print(f"DUPLICATE: {dup}\nORIGINAL:  {original}\n")
        else:
            print("No duplicate files found.")
