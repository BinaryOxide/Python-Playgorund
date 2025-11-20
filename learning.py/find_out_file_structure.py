import os

def print_tree(start_path, prefix=""):
    items = os.listdir(start_path)
    items.sort()
    for idx, item in enumerate(items):
        path = os.path.join(start_path, item)
        connector = "└── " if idx == len(items) - 1 else "├── "
        print(prefix + connector + item + ("/" if os.path.isdir(path) else ""))
        if os.path.isdir(path):
            extension = "    " if idx == len(items) - 1 else "│   "
            print_tree(path, prefix + extension)

def main():
    location = input('Enter the location: ').strip()

    if not os.path.exists(location):
        print("The provided path does not exist.")
        return
    
    if location.endswith(":"):
        location += "\\"

    root_name = os.path.basename(os.path.normpath(location))
    print(f"\n{location}/")
    print_tree(location)
    print("\nDone!")

if __name__ == "__main__":
    main()
