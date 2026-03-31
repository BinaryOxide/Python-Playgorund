import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"}


def clean_path(path):
    return os.path.normpath(path.strip().strip('"').strip("'"))


def get_date_taken(path):
    try:
        img = Image.open(path)
        exif = img._getexif()

        if exif:
            for tag, value in exif.items():
                if TAGS.get(tag) == "DateTimeOriginal":
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except:
        pass
    return None


def get_sort_time(path):
    date_taken = get_date_taken(path)

    if date_taken:
        return date_taken
    else:
        return datetime.fromtimestamp(os.path.getmtime(path))


def get_images_sorted(folder):
    files = []

    for file in os.listdir(folder):
        full_path = os.path.join(folder, file)

        if os.path.isfile(full_path):
            ext = os.path.splitext(file)[1].lower()
            if ext in IMAGE_EXTENSIONS:
                sort_time = get_sort_time(full_path)
                files.append((full_path, sort_time))

    files.sort(key=lambda x: (x[1], os.path.basename(x[0]).lower()))
    return [f[0] for f in files]


def main():
    print("=== TRUE Windows-Style Sort ===\n")

    src = clean_path(input("Source folder: "))
    dst = clean_path(input("Destination folder: "))

    if not os.path.exists(src) or not os.path.exists(dst):
        print("❌ Invalid path")
        return

    files = get_images_sorted(src)

    total = len(files)
    pad = len(str(total))

    for i, file in enumerate(files, 1):
        ext = os.path.splitext(file)[1]
        new_name = f"{str(i).zfill(pad)}_cpp_note_intercentury{ext}"

        shutil.copy2(file, os.path.join(dst, new_name))
        print(f"{os.path.basename(file)} → {new_name}")

    print("\n✅ Done")


if __name__ == "__main__":
    main()