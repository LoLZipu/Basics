sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
a = input("Enter the missing sale for week 2: ")
sales_w2.append(int(float(a)))
sales = sales_w1 + sales_w2
best_day = max(sales)*1.5
worst_day = min(sales)*1.5
total = best_day + worst_day
print(f"""Best Day Profit is ${best_day}
Worst Day Profit is ${worst_day}
Combined Profit is ${total}""")