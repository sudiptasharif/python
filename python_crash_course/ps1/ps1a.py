down_payment_rate = 0.25
total_months = 12
r = 0.04
n = 0
current_savings = 0

annual_salary_prompt = "Enter your annual salary: "
portion_saved_prompt = "Enter the percent of your salary to save, as a decimal: "
total_home_cost_prompt = "Enter the cost of your dream home: "

annual_salary = float(input(annual_salary_prompt))
percent_portion_to_save = float(input(portion_saved_prompt))
total_cost = float(input(total_home_cost_prompt))

monthly_salary = annual_salary / total_months
portion_saved = monthly_salary * percent_portion_to_save
portion_down_payment = total_cost * down_payment_rate

while current_savings <= portion_down_payment:
    current_savings += portion_saved + (current_savings * (r/total_months))
    n += 1

print("Number of months: ", n)

