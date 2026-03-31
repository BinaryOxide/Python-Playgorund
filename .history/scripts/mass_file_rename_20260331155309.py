import os
import shutil

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"}


def clean_path(path):
    return os.path.normpath(path.strip().strip('"').strip("'"))


def get_images_sorted_windows_style(folder):
    files = []

    for file in os.listdir(folder):
        full_path = os.path.join(folder, file)

        if os.path.isfile(full_path):
            ext = os.path.splitext(file)[1].lower()
            if ext in IMAGE_EXTENSIONS:
                stat = os.stat(full_path)
                files.append((full_path, stat.st_mtime))

    # 🔥 Windows-like sort:
    # 1. Date modified
    # 2. If same time → fallback to filename (Explorer does this)
    files.sort(key=lambda x: (x[1], os.path.basename(x[0]).lower()))

    return [f[0] for f in files]


def main():
    print("=== Windows-Style Image Renamer ===\n")

    src_folder = clean_path(input("Enter source folder path: "))
    dest_folder = clean_path(input("Enter destination folder path: "))

    if not os.path.exists(src_folder):
        print("❌ Source folder does not exist!")
        return

    if not os.path.exists(dest_folder):
        print("❌ Destination folder does not exist!")
        return

    files = get_images_sorted_windows_style(src_folder)

    if not files:
        print("❌ No image files found!")
        return

    total = len(files)
    padding = len(str(total))

    print(f"\n📦 Processing {total} images (Windows sort)...\n")

    for index, file_path in enumerate(files, start=1):
        filename = os.path.basename(file_path)
        _, ext = os.path.splitext(filename)

        new_name = f"{str(index).zfill(padding)}_cpp_note_intercentury{ext}"
        new_path = os.path.join(dest_folder, new_name)

        try:
            shutil.copy2(file_path, new_path)
            print(f"✅ {filename} -> {new_name}")
        except Exception as e:
            print(f"❌ Failed: {filename} | {e}")

    print("\n🎉 Done! Matches Windows sorting.")


if __name__ == "__main__":
    main()