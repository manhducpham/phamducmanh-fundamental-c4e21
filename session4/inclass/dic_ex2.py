import pyexcel

dic1 = {
    'No': 1,
    'Name': 'Huy',
    'Salary per hour': 25,
    'Number of working hours': 14,
}
dic2 = {
    'No': 2,
    'Name': 'Hoa',
    'Salary per hour': 20,
    'Number of working hours': 7,
}
dic3 = {
    'No': 3,
    'Name': 'Tam',
    'Salary per hour': 15,
    'Number of working hours': 20,
}
part_time_salary = [dic1, dic2, dic3]
n = len(part_time_salary)

# for k in dic1:
#     print(k, end = "\t")
    
# print()
# for i in range(n):
#     for v in part_time_salary[i].values():
#         print(v,  end = "\t")
#     print()
# total_budget = 0
# for i in range(n):
#     part_time_salary[i]["Total Salary"] = part_time_salary[i]["Salary per hour"] * part_time_salary[i]["Number of working hours"]
#     # print(part_time_salary[i]["Total Salary"])
#     total_budget += part_time_salary[i]["Total Salary"]
# print(total_budget)
total_wage = 0
#lam gon hon scale len
# for salary in part_time_salary:
#     name = salary['Name']
#     hour = salary['Salary per hour']
#     level = salary['Number of working hours']
#     wage = hour * level
#     total_wage += wage
#     print(name, "'s wage: ", wage)
# print("Total wage: ", total_wage)
# tao ra bang moi
wage_list = []
for salary in part_time_salary:
    name = salary['Name']
    hour = salary['Salary per hour']
    level = salary['Number of working hours']
    wage = hour * level
    wage_info = {
        'Name': name,
        'Wage': wage,
    }
    wage_list.append(wage_info)
    total_wage += wage
    print(name, "'s wage: ", wage)
print("Total wage: ", total_wage)
print(wage_list)
pyexcel.save_as(records = wage_list, dest_file_name = "wage_list.xlsx")