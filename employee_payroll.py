"""
This Program:

Keeps track of employees (name, role, email, and hours worked per week)
Calculates their weekly pay based on rank-based hourly rates
Stores this information in a structured way (like a list of objects or a dictionary)

"""
import random 
class Employee:
  RANK_RATES = {
      "Intern": 8,
      "Junior Developer": 12,
      "Senior Developer": 16,
      "Manager": 20
  }
  
  def __init__(self, first_name, last_name, position, hours_worked):
    self.first_name = first_name
    self.last_name = last_name
    self.position = position
    self.hours_worked = hours_worked

    random_num: str = ''.join(str(random.randint(0, 9)) for _ in range(4))
    self.hourly_rate = Employee.RANK_RATES.get(position, 8)
    self.email = first_name.lower() + '.' + last_name.lower() + random_num + '@mangnamo.com'

  def fullname(self):
    return '{} {}'.format(self.first_name, self.last_name)
  
  def weekly_pay(self):
    return f"{self.hours_worked * self.hourly_rate}"

  def display_info(self):
    """Display employee details and pay."""
    print("=" * 30)
    print(f"\nEmployee: {self.fullname()}")
    print(f"Role: {self.position}")
    print(f"Email: {self.email}")
    print(f"Hours Worked: {self.hours_worked}")
    print(f"Hourly Rate: ${self.hourly_rate}")
    print(f"Weekly Pay: ${self.weekly_pay()}")
    print("=" * 30)

employees = [
  Employee("Joseph", "Adewola", "Intern", 35),
  Employee("John", "Smith", "Manager", 40),
  Employee("Lucy", "Adams", "Senior Developer", 45)
]

for emp in employees:
    emp.display_info()