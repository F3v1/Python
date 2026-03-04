import os
import shutil

EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

DEFAULT_FOLDER = "Others"

def organize_folder(path):
    if not os.path.exists(path):
        print("Path does not exist.")
        return

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            moved = False

            for folder, extensions in EXTENSIONS.items():
                if file_ext in extensions:
                    folder_path = os.path.join(path, folder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    shutil.move(file_path, os.path.join(folder_path, file))
                    print(f"Moved {file} to {folder}")
                    moved = True
                    break

            if not moved:
                # Move file to 'Others'
                folder_path = os.path.join(path, DEFAULT_FOLDER)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                shutil.move(file_path, os.path.join(folder_path, file))
                print(f"Moved {file} to {DEFAULT_FOLDER}")

if __name__ == "__main__":
    folder_path = input("Enter folder path to organize: ")
    organize_folder(folder_path)
    print("Organization complete!")
