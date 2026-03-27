
import csv

VALID_BLOOD_GROUPS = {'A', 'B', 'AB', 'O' }

def validate_row(row):
  errors = []

  if not row['name   '].strip():
    errors.append('Name is missing')
  
  age_str = row[' age'].strip()
  if not age_str.isdigit():
      errors.append('Age is not a valid number')
  else:
    age = int(age_str)
    if not (1 <= age <= 120):
      errors.append('Invalid age range')

  if not row[' heart_rate'].strip().isdigit() or not (40 <= int(row[' heart_rate']) <= 200):
      errors.append('Heart rate is invalid')
      
  if row[' blood_type'].strip().upper() not in VALID_BLOOD_GROUPS:
    errors.append('Invalid blood group')
  

  if not row[' cholesterol'].strip().isdigit() or int(row[' cholesterol']) <= 0:
    errors.append('Cholesterol is invalid')

  if row[' has_diabetes'].strip() not in {'0', '1'}:
    errors.append('Invalid diabetes reading')

  return errors

valid_rows = []
error_rows = []

with open('practice_patients.csv', encoding='utf-8') as f:
  csv_reader = csv.DictReader(f)
  for row in csv_reader:
    errors = validate_row(row)
    if errors:
      error_rows.append({'row': row, 'reasons': errors})
    else:
      valid_rows.append(row)

print(f'Valid rows  : {len(valid_rows)}')
print(f'Invalid rows: {len(error_rows)}')
print()
for e in error_rows:
    print(f"Row {e['row']} → {e['reasons']}")

print(error_rows)