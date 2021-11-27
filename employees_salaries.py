# function - method
def calculateSalary(basic_sal, percentageForTax=.15):
    taxs = percentageForTax * basic_sal
    insurance = .07 * basic_sal
    taotal_sal = basic_sal - (taxs+insurance)
    return taotal_sal

def calculateTotalSalaries(*args):  # list of arguments
    total_salaries = 0
    for one_emp_sal in args:
        total_salaries += one_emp_sal
    return total_salaries

# def printName(emp_name): # receive diffent values / arguments
#     # name = 'Mahmoud'
#     print('Hello '+ emp_name)
#
# printName('Kareem')
# printName('Hossam')
# printName('Mohamed')
# emp_1_basicsal = 6000
# emp_2_basicsal = 7000
# emp_3_basicsal = 4000
#
# total_emp_1_sal = calculateSalary(emp_1_basicsal, .2)  # tax 20%
# total_emp_2_sal = calculateSalary(emp_2_basicsal)  # tax 15 %
# total_emp_3_sal = calculateSalary(emp_3_basicsal)  # tax 15 %
# #
# # print(total_emp_1_sal)
# # print(total_emp_2_sal)
# # print(total_emp_3_sal)
# totalSalaries = calculateTotalSalaries(total_emp_1_sal, total_emp_2_sal, total_emp_3_sal)
#
# print(totalSalaries)

