import os
import shutil

# Supported image formats
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"}


def clean_path(path):
    """Remove quotes, spaces and normalize path"""
    path = path.strip().strip('"').strip("'")
    return os.path.normpath(path)


def get_images_sorted_by_date(folder):
    """Get image files sorted by modification time (oldest first)"""
    files = []

    for file in os.listdir(folder):
        full_path = os.path.join(folder, file)

        if os.path.isfile(full_path):
            ext = os.path.splitext(file)[1].lower()
            if ext in IMAGE_EXTENSIONS:
                time = os.path.getmtime(full_path)
                files.append((full_path, time))

    files.sort(key=lambda x: x[1])  # sort by time
    return [f[0] for f in files]


def main():
    print("=== Image Renamer & Copier ===\n")

    # Get user input
    src_folder = clean_path(input("Enter source folder path: "))
    dest_folder = clean_path(input("Enter destination (empty) folder path: "))

    # Debug output
    print(f"\n[DEBUG] Source: {src_folder}")
    print(f"[DEBUG] Destination: {dest_folder}\n")

    # Validate paths
    if not os.path.exists(src_folder):
        print("❌ Source folder does not exist!")
        return

    if not os.path.exists(dest_folder):
        print("❌ Destination folder does not exist!")
        return

    # Check destination is empty
    if os.listdir(dest_folder):
        print("⚠️ Warning: Destination folder is NOT empty!")

    files = get_images_sorted_by_date(src_folder)

    if not files:
        print("❌ No image files found!")
        return

    total = len(files)
    padding = len(str(total))  # auto padding

    print(f"📦 Found {total} images. Processing...\n")

    for index, file_path in enumerate(files, start=1):
        filename = os.path.basename(file_path)
        name, ext = os.path.splitext(filename)

        new_name = f"{str(index).zfill(padding)}_img{ext}"
        new_path = os.path.join(dest_folder, new_name)

        try:
            shutil.copy2(file_path, new_path)  # preserves metadata
            print(f"✅ {filename} -> {new_name}")
        except Exception as e:
            print(f"❌ Failed: {filename} | Error: {e}")

    print("\n🎉 Done! All images copied & renamed successfully.")


if __name__ == "__main__":
    main()