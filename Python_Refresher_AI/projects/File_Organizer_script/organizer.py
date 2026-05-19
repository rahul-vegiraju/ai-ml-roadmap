from pathlib import Path
import shutil

folder = Path("test_folder")

file_types = {
    ".png": "images",
    ".jpg": "images",
    ".pdf": "documents",
    ".txt": "documents",
    ".mp3": "audio"
}

for file in folder.iterdir():

    if file.is_file():

        extension = file.suffix.lower()

        if extension in file_types:

            target_folder = folder / file_types[extension]

            target_folder.mkdir(exist_ok=True)

            shutil.move(str(file), str(target_folder / file.name))

print("Files organized successfully.")
