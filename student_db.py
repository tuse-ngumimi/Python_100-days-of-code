import json
import csv

class StudentDB:
  """
  Simple database for Computer Science students
  """
  DEPT_CODE = "04/05"
  def __init__(self, first_name, last_name, year, cgpa, admission_year, student_num):
    self.first_name: str = first_name
    self.last_name: str = last_name
    self.year: int = year
    self.cgpa: float= cgpa
    self.admission_year = admission_year
    self.student_num: int = student_num
    

    self.matric_no = f"BHU/{self.admission_year}/{StudentDB.DEPT_CODE}/{self.student_num:05d}"

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

    self.email = first_name.lower() + '.' + last_name.lower() + '@binghamuni.edu.ng'
    #self.other_names : str = input("Enter your other names: ")
    
  def generate_matric_no(self):
    formatted_year = str(self.student_num).zfill(4)
    return f"BHU/{self.year}/04/05/{formatted_year}"
  
  def fullname(self):
    return '{} {}'.format(self.first_name, self.last_name)
  
  def display_student_db(self):
    print(f"\nName: {self.fullname()}")
    print(f"Matric No.: {self.matric_no}")
    print(f"CGPA: {self.cgpa}")
    print(f"Email: {self.email}")
    #print(f"CGPA classification: {self.gpa_classification()}")

def update_student(self, **kwargs):
    """
    Update student data dynamically.
    Example:
        student.update_student(first_name="Mary", cgpa=4.21)
    """
    for key, value in kwargs.items():
        if hasattr(self, key):
            setattr(self, key, value)

    if "admission_year" in kwargs or "student_num" in kwargs:
        self.matric_no = f"BHU/{self.admission_year}/{StudentDB.DEPT_CODE}/{self.student_num:05d}"


computer_science = [
    StudentDB("Amira", "Yusuf", "23", 4.34, 24, 123),
    StudentDB("Collins", "Adejare", "23", 3.89, 24, 23)
]

# Display original record
for student in computer_science:
    student.display_student_db()
    
