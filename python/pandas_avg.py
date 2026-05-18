import pandas as pd
import matplotlib.pyplot as plt

# employee data
data = {
    "department": [
        "Sales", "Engineering", "Finance", "Marketing", "Engineering",
        "HR", "Sales", "Finance", "Marketing", "Engineering"
    ],
    "salary": [
        320000, 520000, 680000, 290000, 470000,
        350000, 720000, 610000, 310000, 490000
    ]
}

# DataFrame
df = pd.DataFrame(data)

# group by department and calculate average salary
avg_salary = df.groupby("department")["salary"].mean()

# convert to DataFrame
avg_salary = avg_salary.reset_index()

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
