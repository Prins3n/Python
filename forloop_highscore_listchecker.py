student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)


largest_value = 0
#for hver element i studentscores listen gjør dette.
for a in student_scores:
    #hvis a er større en largest value variabelen gjør dette.
    if a > largest_value:
        #largest_value er nå a.
        largest_value = a
print(largest_value)