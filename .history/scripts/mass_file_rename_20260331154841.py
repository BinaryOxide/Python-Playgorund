import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS

# Supported image formats
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"}


def clean_path(path):
    return os.path.normpath(path.strip().strip('"').strip("'"))


def get_exif_datetime(path):
    """Extract DateTimeOriginal from EXIF"""
    try:
        img = Image.open(path)
        exif = img._getexif()

        if exif is not None:
            for tag, value in exif.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == "DateTimeOriginal":
                    # Format: "YYYY:MM:DD HH:MM:SS"
                    return value
    except:
        pass

    return None


def parse_exif_time(exif_str):
    """Convert EXIF string to sortable format"""
    from datetime import datetime
    return datetime.strptime(exif_str, "%Y:%m:%d %H:%M:%S")


def get_images_sorted(folder):
    files = []

    for file in os.listdir(folder):
        full_path = os.path.join(folder, file)

        if os.path.isfile(full_path):
            ext = os.path.splitext(file)[1].lower()

            if ext in IMAGE_EXTENSIONS:
                exif_time = get_exif_datetime(full_path)

                if exif_time:
                    sort_time = parse_exif_time(exif_time)
                else:
                    # fallback
                    sort_time = os.path.getmtime(full_path)

                files.append((full_path, sort_time))

    files.sort(key=lambda x: x[1])
    return [f[0] for f in files]


def main():
    print("=== EXIF-Based Image Renamer ===\n")

    src_folder = clean_path(input("Enter source folder path: "))
    dest_folder = clean_path(input("Enter destination folder path: "))

    if not os.path.exists(src_folder):
        print("❌ Source folder does not exist!")
        return

    if not os.path.exists(dest_folder):
        print("❌ Destination folder does not exist!")
        return

    files = get_images_sorted(src_folder)

    if not files:
        print("❌ No image files found!")
        return

    total = len(files)
    padding = len(str(total))

    print(f"\n📦 Processing {total} images (capture time sorted)...\n")

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

    print("\n🎉 Done! Sorted by capture time.")


if __name__ == "__main__":
    main()