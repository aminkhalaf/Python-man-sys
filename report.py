# get employess salaries, median ages
from employees_salaries import calculateSalary, calculateTotalSalaries
from employees_data import medianOfEmployeesAges

# sample from DB
employees_ages = [25, 30, 30]
emp_1_basicsal = 6000
emp_2_basicsal = 7000
emp_3_basicsal = 4000

# calculateSalary, calculateTotalSalaries, medianOfEmployeesAges
emp1_total = calculateSalary(emp_1_basicsal)
emp2_total = calculateSalary(emp_2_basicsal)
emp3_total = calculateSalary(emp_3_basicsal)

totalSalaries = calculateTotalSalaries(emp1_total, emp2_total, emp3_total)
print(totalSalaries)

print(medianOfEmployeesAges(employees_ages))