import os
import re
import shutil

# Supported image formats
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"}


def clean_path(path):
    """Remove quotes and normalize path."""
    path = path.strip().strip('"').strip("'")
    return os.path.normpath(path)


def natural_key(text):
    """
    Human-friendly sort:
    CamScanner_2.jpg before CamScanner_10.jpg
    """
    return [
        int(chunk) if chunk.isdigit() else chunk.lower()
        for chunk in re.split(r"(\d+)", text)
    ]


def get_images_sorted_windows_style(folder):
    """
    Sort by modified time first, then by natural filename order
    for files that share the same timestamp.
    """
    files = []

    for entry in os.scandir(folder):
        if not entry.is_file():
            continue

        ext = os.path.splitext(entry.name)[1].lower()
        if ext not in IMAGE_EXTENSIONS:
            continue

        stat = entry.stat()
        # Use nanoseconds for maximum precision
        mtime = stat.st_mtime_ns
        files.append((entry.path, mtime, entry.name))

    # Sort like Explorer-style grouping:
    # 1) modified time
    # 2) natural filename order
    files.sort(key=lambda x: (x[1], natural_key(x[2])))

    return [x[0] for x in files]


def main():
    print("=== Image Renamer & Copier ===\n")

    src_folder = clean_path(input("Enter source folder path: "))
    dest_folder = clean_path(input("Enter destination (empty) folder path: "))

    if not os.path.exists(src_folder):
        print("❌ Source folder does not exist!")
        return

    if not os.path.exists(dest_folder):
        print("❌ Destination folder does not exist!")
        return

    if os.listdir(dest_folder):
        print("⚠️ Warning: Destination folder is NOT empty!")

    files = get_images_sorted_windows_style(src_folder)

    if not files:
        print("❌ No image files found!")
        return

    total = len(files)
    padding = len(str(total))

    print(f"\n📦 Found {total} images. Processing...\n")

    for index, file_path in enumerate(files, start=1):
        filename = os.path.basename(file_path)
        _, ext = os.path.splitext(filename)

        new_name = f"{str(index).zfill(padding)}_cpp_note_intercentury{ext}"
        new_path = os.path.join(dest_folder, new_name)

        try:
            shutil.copy2(file_path, new_path)
            print(f"✅ {filename} -> {new_name}")
        except Exception as e:
            print(f"❌ Failed: {filename} | Error: {e}")

    print("\n🎉 Done! Files copied in stable Windows-like order.")


if __name__ == "__main__":
    main()