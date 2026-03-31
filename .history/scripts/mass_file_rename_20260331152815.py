import os
import shutil
from datetime import datetime

def get_files_sorted_by_date(folder):
    files = []
    
    for file in os.listdir(folder):
        full_path = os.path.join(folder, file)
        
        if os.path.isfile(full_path):
            # Get modification time
            time = os.path.getmtime(full_path)
            files.append((full_path, time))
    
    # Sort by time (oldest first)
    files.sort(key=lambda x: x[1])
    
    return [f[0] for f in files]


def main():
    print("=== Image Renamer & Copier ===\n")
    
    src_folder = input("Enter source folder path: ").strip()
    dest_folder = input("Enter destination (empty) folder path: ").strip()
    
    if not os.path.exists(src_folder):
        print("❌ Source folder does not exist!")
        return
    
    if not os.path.exists(dest_folder):
        print("❌ Destination folder does not exist!")
        return
    
    files = get_files_sorted_by_date(src_folder)
    
    if not files:
        print("❌ No files found!")
        return
    
    total = len(files)
    padding = len(str(total))  # auto padding (e.g. 001, 0001)
    
    print(f"\nProcessing {total} files...\n")
    
    for index, file_path in enumerate(files, start=1):
        filename = os.path.basename(file_path)
        name, ext = os.path.splitext(filename)
        
        new_name = f"{str(index).zfill(padding)}{ext}"
        new_path = os.path.join(dest_folder, new_name)
        
        shutil.copy2(file_path, new_path)  # preserves metadata
        
        print(f"{filename} -> {new_name}")
    
    print("\n✅ Done! All files copied & renamed successfully.")


if __name__ == "__main__":
    main()