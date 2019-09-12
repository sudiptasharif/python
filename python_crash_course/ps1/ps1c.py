down_payment_rate = 0.25
total_months = 12
six_months = 6
r = 0.04  # annual return
n = 0  # number of months
k = 0  # bisection search count
current_savings = 0
semi_annual_raise = .07
total_cost = 1000000
max_months = 36
p_max = 10000  # percent max
p_min = 0  # percent min
p = 0  # percent of portion needed to save per month
p_found = False  # a bool flag to indicate if a percent found

annual_salary_prompt = "Enter your annual salary: "
annual_salary = float(input(annual_salary_prompt))
portion_down_payment = total_cost * down_payment_rate

p = p_min + ((p_max - p_min) / 2)
while p > p_min:
    k += 1  # increment the bisection search counter
    percent_portion_to_save = p / 10000
    monthly_salary = annual_salary / total_months

    while n < max_months:
        if n % six_months == 0 and n > 0:
            monthly_salary += monthly_salary * semi_annual_raise

        portion_saved = monthly_salary * percent_portion_to_save
        current_savings += portion_saved + (current_savings * (r / total_months))
        n += 1

    # print("portion_down_payment = ", portion_down_payment, "current_savings = ", current_savings)
    # print("p_min = ", p_min, "p_mid = ", p, "p_max = ", p_max)
    if abs(portion_down_payment - current_savings) <= 100:
        p_found = True
        break
    elif current_savings < portion_down_payment:
        p_min = p
    else:
        p_max = p

    p = int(p_min + ((p_max - p_min) / 2))
    n = 0  # reset months to 0
    current_savings = 0

if p_found:
    print("Best saving rate: ", percent_portion_to_save)
    print("Steps in bisection search: ", k)
else:
    print("It is not possible to pay the down payment in three years.")




