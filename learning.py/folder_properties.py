import os

# Define file extensions for categorization
PHOTO_EXT = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp'}
VIDEO_EXT = {'.mp4', '.mkv', '.mov', '.avi', '.flv', '.wmv', '.webm'}
AUDIO_EXT = {'.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'}
ZIP_EXT   = {'.zip', '.rar', '.7z', '.tar', '.gz'}
EXE_EXT   = {'.exe', '.msi'}

def collect_folder_info(path):
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
            file_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()
            try:
                total_size += os.path.getsize(file_path)
            except Exception:
                continue  # skip unreadable files

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
    location = input("Enter folder location: ").strip()
    if not os.path.exists(location):
        print("The path does not exist.")
        return

    if location.endswith(":"):
        location += "\\"

    print("\nCollecting folder information...\n")
    stats = collect_folder_info(os.path.abspath(location))

    print("Properties:")
    print(f"Total folders     : {stats['folders']}")
    print(f"Total space       : {stats['size_mb']} MB")
    print(f"Total photos      : {stats['photos']}")
    print(f"Total videos      : {stats['videos']}")
    print(f"Total audios      : {stats['audios']}")
    print(f"Total zip files   : {stats['zips']}")
    print(f"Total exe count   : {stats['exes']}")

if __name__ == "__main__":
    main()
