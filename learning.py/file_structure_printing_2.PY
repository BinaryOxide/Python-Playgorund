import os

# File type categories
PHOTO_EXT = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp'}
VIDEO_EXT = {'.mp4', '.mkv', '.mov', '.avi', '.flv', '.wmv', '.webm'}
AUDIO_EXT = {'.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'}
ZIP_EXT   = {'.zip', '.rar', '.7z', '.tar', '.gz'}
EXE_EXT   = {'.exe', '.msi'}

def print_folder_structure(path, prefix=""):
    try:
        entries = os.listdir(path)
    except PermissionError:
        return  # skip inaccessible

    dirs = sorted([e for e in entries if os.path.isdir(os.path.join(path, e))])

    for idx, entry in enumerate(dirs):
        full_path = os.path.join(path, entry)
        is_last = idx == len(dirs) - 1
        connector = " └── " if is_last else "├── "
        print(prefix + connector + entry + "/")
        extension = "    " if is_last else "│   "
        print_folder_structure(full_path, prefix + extension)

    if any(os.path.isfile(os.path.join(path, e)) for e in entries):
        connector = " └── " if not dirs else "├── "
        print(prefix + connector + "(files)")

def collect_stats(path):
    folder_count = 0
    total_size = 0
    photo_count = 0
    video_count = 0
    audio_count = 0
    zip_count = 0
    exe_count = 0

    for root, dirs, files in os.walk(path):
        folder_count += len(dirs)
        for file in files:
            full_path = os.path.join(root, file)
            try:
                size = os.path.getsize(full_path)
                total_size += size
            except Exception:
                continue  # skip unreadable files

            ext = os.path.splitext(file)[1].lower()
            if ext in PHOTO_EXT:
                photo_count += 1
            elif ext in VIDEO_EXT:
                video_count += 1
            elif ext in AUDIO_EXT:
                audio_count += 1
            elif ext in ZIP_EXT:
                zip_count += 1
            elif ext in EXE_EXT:
                exe_count += 1

    return {
        "folders": folder_count,
        "size_mb": round(total_size / (1024 * 1024), 2),
        "photos": photo_count,
        "videos": video_count,
        "audios": audio_count,
        "zips": zip_count,
        "exes": exe_count,
    }

def main():
    location = input("Enter the location: ").strip()
    if not os.path.exists(location):
        print("The provided path does not exist.")
        return

    if location.endswith(":"):
        location += "\\"

    abs_path = os.path.abspath(location)
    print(f"\n{abs_path}/")
    
    # Phase 1: Fast visual tree
    print_folder_structure(abs_path)

    print("\nDone!\n")

    # Phase 2: Fast stats
    stats = collect_stats(abs_path)

    print("Summary:")
    print(f"Total folders     : {stats['folders']}")
    print(f"Total space       : {stats['size_mb']} MB")
    print(f"Total photos      : {stats['photos']}")
    print(f"Total videos      : {stats['videos']}")
    print(f"Total audios      : {stats['audios']}")
    print(f"Total zip files   : {stats['zips']}")
    print(f"Total exe count   : {stats['exes']}")

if __name__ == "__main__":
    main()
