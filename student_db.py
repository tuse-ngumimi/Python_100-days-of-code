import csv

class StudentDB:
  """
  Simple database for Computer Science students
  """
  DEPT_CODE = "04/05"

  def __init__(self, first_name, last_name, year, cgpa, admission_year, student_num):
    self.first_name = first_name
    self.last_name = last_name
    self.year = year
    self.cgpa = float(cgpa)
    self.admission_year = int(admission_year)
    self.student_num = int(student_num)
    
    self.matric_no = f"BHU/{self.admission_year}/{StudentDB.DEPT_CODE}/{self.student_num:05d}"
    self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@binghamuni.edu.ng"

  def gpa_classification(self):
    if self.cgpa >= 4.50:
     return "First Class"
    elif self.cgpa >= 3.50:
     return "Second Class Upper"
    elif self.cgpa >= 2.50:
     return "Second Class Lower"
    elif self.cgpa >= 1.50:
     return "Third Class"
    else:
     return "Fail"

   #self.other_names : str = input("Enter your other names: ") 
   #def generate_matric_no(self):
   #formatted_year = str(self.student_num).zfill(4)
   #return f"BHU/{self.year}/04/05/{formatted_year}"
  
  def fullname(self):
    return f"{self.first_name} {self.last_name}"
  
  def add_to_dict(self):
     """
     Coverts the plain student data to a csv file format
     """
     return {
         "first_name": self.first_name,
         "last_name": self.last_name,
         "level": self.year,
         "cgpa": self.cgpa,
         "grade": self.gpa_classification(),
         "admission_year": self.admission_year,
         "student_number": self.student_num,
         "matric_no": self.matric_no,
         "email": self.email,
     }
  
class StudentCSVManager:
  FILE = "students_db.csv"

  @staticmethod
  def save_students_db(student: StudentDB):
    """
    Adds new students entry to the CSV file
    """
    file_exists = False
    try:
      with open(StudentCSVManager.FILE, "r"):
        file_exists = True
    except FileNotFoundError:
      pass

    with open(StudentCSVManager.FILE, "a", newline="") as f:
       writer = csv.DictWriter(f, fieldnames=student.add_to_dict().keys())
       if not file_exists:
            writer.writeheader()
       writer.writerow(student.add_to_dict())
    
  @staticmethod
  def load_students_db():
        """
        Load all students from CSV.
        """
        students = []
        try:
            with open(StudentCSVManager.FILE, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    students.append(row)
        except FileNotFoundError:
            pass
        return students
 
def main():
   while True:
      print("\n===== STUDENT DATABASE MENU =====")
      print("1. Add new student")
      print("2. View all students")
      print("3. Exit")

      choice = input("\nEnter your choice: ")

      if choice == "1":
        print("\n--- Add New Student ---")
        first = input("First Name: ")
        last = input("Last Name: ")
        year = input("Year (e.g. 100 level, 400 level): ")
        cgpa = input("CGPA: ")
        admission = input("Admission Year (e.g. 21, 20, 24): ")
        number = input("Student Number: ")

        student = StudentDB(first, last, year, cgpa, admission, number)
        StudentCSVManager.save_students_db(student)
        print("\nStudent added successfully!")

      elif choice == "2":
         print("\n--- All Students ---")
         students = StudentCSVManager.load_students_db()
         if not students:
            print("No student records found.")
         else:
            for s in students:
                print(f"{s['first_name']} {s['last_name']} | {s['matric_no']} | CGPA: {s['cgpa']}")

      elif choice == "3":
          print("Goodbye!")
          break

      else:
          print("Invalid option. Try again.")

if __name__ == '__main__':
    main()
