# import random

# string = ("oluwadumininu")
# new_string = random.sample(string, len(string))
# print(''.join(new_string))
 
students = ["Ada", "Jude", "Michael", "Kiki", "Sam"]
# for student in students:
#   print(student)

student_scores = [90, 78, 48, 38, 66, 68, 22, 54, 90, 95, 29, 38, 24, 94, 88]
max_score = 0
for score in student_scores:
  if score > max_score:
    max_score = score
print(max_score)

total_scores = sum(student_scores)

average_scores = sum(student_scores) / len(students)

# sum = 0
# for score in student_scores:
#   sum += score

# print(sum) 

print(total_scores)
print(average_scores)

sum = 0
for number in range(1, 101):
  sum += number
print(sum)

