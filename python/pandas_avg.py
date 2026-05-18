import pandas as pd
import matplotlib.pyplot as plt

# employee data
data = {
    "department": [
        "Sales",
        "Engineering",
        "Finance",
        "Marketing",
        "Engineering",
        "HR",
        "Sales",
        "Finance",
        "Marketing",
        "Engineering",
        "Sales",
        "HR",
        "Finance",
        "Marketing",
        "Engineering",
        "Sales",
        "Engineering",
        "Finance",
        "Marketing",
        "HR",
        "Sales",
        "Engineering",
        "Finance",
        "Marketing",
        "Engineering",
        "HR",
        "Sales",
        "Marketing",
        "Finance",
        "Engineering"
    ],

    "salary": [
        310000,
        670000,
        820000,
        280000,
        520000,
        360000,
        760000,
        640000,
        295000,
        580000,
        690000,
        340000,
        610000,
        350000,
        910000,
        330000,
        550000,
        670000,
        260000,
        470000,
        720000,
        410000,
        560000,
        340000,
        710000,
        325000,
        780000,
        370000,
        590000,
        980000
    ]
}

# DataFrame
df = pd.DataFrame(data)

# group by department and calculate average salary
avg_salary = df.groupby("department")["salary"].mean()

# convert to DataFrame
avg_salary = avg_salary.reset_index()

# sort values
avg_salary = avg_salary.sort_values(by="salary", ascending=True)

# print result
print(avg_salary)

# chart size
plt.figure(figsize=(8, 5))

# horizontal bar chart
plt.barh(avg_salary["department"], avg_salary["salary"])

# title
plt.title("Average Salary by Department")

# labels
plt.xlabel("Average Salary")
plt.ylabel("Department")

# grid
plt.grid(axis='x')

# layout
plt.tight_layout()

# show
plt.show()
