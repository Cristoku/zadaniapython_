costs={
    "January": 2000,
    "February": 2100,
    "March": 1900,
    "April": 2000,
    "May": 1500,
    "June": 1800,
    "July": 2500,
    "August": 4000,
    "September": 2000,
    "October": 1700,
    "November": 2100,
    "December": 3000
}

min_cost= min(costs.values())
max_cost= max(costs.values())
sum_cost= sum(costs.values())
avg_cost= sum_cost/len(costs)

if list(costs.values())[-1] > avg_cost:
    print("Start being more careful with money, your last month was trash")
else:
    print("Your expences in last month wasn't so bad, good job")

print("Minimim expense in one month is ", min_cost)
print("Maximum expense in one month is ", max_cost)
print("Total expences for whole year is ", sum_cost)
print("Avrage expense is ", avg_cost)
print("Months with costs being more than avrage:")

for month, cost in costs.items():
    if cost > avg_cost:
        print(month + ": " + str(cost))