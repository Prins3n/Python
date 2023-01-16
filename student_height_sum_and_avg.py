student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_heights = sum(student_heights)
average_heights = total_heights/len(student_heights)
print(round(average_heights))

print(sum(student_heights))

list = 0

for a in student_heights:
  list += 1
print(list)

sum = 0

for a in range(len(student_heights)):
  sum += a
print(sum)

average = sum/list
print(round(average))