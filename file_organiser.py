import os
import shutil

FILE_CATEGORIES = {
  "Images": [".png", ".jpeg", ".jpg", ".gif"],
  "Videos": [".mp4", ".mov",".mkv", ".avi"],
  "Documents": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
  "Archives": [".zip", ".tar"],
  "Programs": [".exe", ".apk", ".msi"],
  "Audio": [".mp3", ".wav"],
}

def organise_folder(folder_path):
  if not os.path.isdir(folder_path):
    print("The specified folder does not exist!")
    return
  print(f"Currently organising files in: {folder_path}")

  for filename in os.listdir(folder_path):
    file_path  = os.path.join(folder_path, filename)

    if os.path.isdir(file_path):
      continue

    name, ext = os.path.splitext(filename)
    ext = ext.lower()

    moved = False

    for category, extensions in FILE_CATEGORIES.items():
     if ext in extensions:
        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)
        
        try:
            shutil.move(file_path, os.path.join(category_folder, filename))
            print(f" Moved {filename} → {category}/")
            moved = True
        except PermissionError:
            print(f" Permission denied: {filename}")
        except Exception as e:
            print(f" Error moving {filename}: {e}")
        
        break


    if not moved:
      others_folder = os.path.join(folder_path, "Others")
      os.makedirs(others_folder, exist_ok=True)

      shutil.move(file_path, os.path.join(others_folder, filename))
      print(f" Moved {filename} → Others/")

  print("\n *******Organisation complete!******")



if __name__ == "__main__":
    folder = input("Enter folder path to organise: ")
    organise_folder(folder)