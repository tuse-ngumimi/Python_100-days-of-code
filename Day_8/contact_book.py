import datetime

class FileAlreadyExistsError(Exception):
  def __init__(self, name: str, phone_num: int):
    self.message = (print(f"{name} already exists in contact book."))
    super().__init__(self.message)

def ensure_file_exists(filename: str) -> None:
    """Ensure the contacts file exists, create if missing."""
    try:
        with open(filename, "r", encoding="utf-8"):
            pass
    except FileNotFoundError:
        print("File not found. Creating a new Contacts.txt file...")
        with open(filename, "w", encoding="utf-8"):
            pass
  
def read_contacts(filename: str):
   try:
      with open(filename, "r", encoding= "utf-8") as f:
         pass
   except FileNotFoundError:
        print("File not found. Creating a new visitors.txt file...")
        with open(filename, "w", encoding="utf-8"):
            pass
      
