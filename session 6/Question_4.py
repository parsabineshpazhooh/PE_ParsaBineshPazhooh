employees = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },
    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },
    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }}
big_salaries = []
salaries = [k["salary"] for k in employees.values()]
max_salary = max(salaries)
avg_salary = sum(salaries) / len(salaries)
for i in salaries:
    if i > 3000:
        big_salaries.append(i)
min_salary = min(salaries)
for i in employees.values():
    if i["salary"] == min_salary:
        print(i["name"], ':', min_salary)
print(max_salary)
print(avg_salary)
print(big_salaries)