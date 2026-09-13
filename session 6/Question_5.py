students = {
    "Ali": [18, 17, 20],
    "Sara": [15, 19, 18],
    "Reza": [12, 14, 10],
    "Mina": [20, 20, 19]
}
status_Ali = ""
status_Sara = ""
status_Reza = ""
status_Mina = ""
# averages
avg_Ali = sum(students["Ali"]) / 3
avg_Sara = sum(students["Sara"]) / 3
avg_Reza = sum(students["Reza"]) / 3
avg_Mina = sum(students["Mina"]) / 3
# Max of averages
max_avg_all = max(avg_Ali, avg_Sara, avg_Reza, avg_Mina)
# Max mark
max_Ali = max(students["Ali"][0:2])
max_Sara = max(students["Sara"][0:2])
max_Reza = max(students["Reza"][0:2])
max_Mina = max(students["Mina"][0:2])
# Best student
Best_student = ""
for i in students.keys():
    if sum(students[i]) > sum(students["Reza"]):
        Best_student = i
# Failed or Passed
if avg_Ali >= 15:
    status_Ali = "status : Passed"
elif avg_Ali < 15:
    status_Ali = "status : Failed"

if avg_Sara >= 15:
    status_Sara = "status : Passed"
elif avg_Sara < 15:
    status_Sara = "status : Failed"

if avg_Reza >= 15:
    status_Reza = "status : Passed"
elif avg_Reza < 15:
    status_Reza = "status : Failed"

if avg_Mina >= 15:
    status_Mina = "status : Passed"
elif avg_Mina < 15:
    status_Mina = "status : Failed"
# The report
print(f"Ali\nAverage : {avg_Ali}\n{status_Ali}\nMax mark : {max_Ali}")
print('*' * 15)
print(f"Sara\nAverage : {avg_Sara}\n{status_Sara}\nMax mark : {max_Sara}")
print('*' * 15)
print(f"Reza\nAverage : {avg_Reza}\n{status_Reza}\nMax mark : {max_Reza}")
print('*' * 15)
print(f"Mina\nAverage : {avg_Mina}\n{status_Mina}\nMax mark : {max_Mina}")
print('*' * 15)
print(f"{Best_student} is Best student with average of mark {max_avg_all}")