import pandas as pd
import matplotlib.pyplot as plt

# data
data = {
    "department": [
        "Sales",
        "Engineering",
        "HR",
        "Finance",
        "Marketing"
    ],
    "avg_salary": [
        598333,
        666250,
        373750,
        648333,
        315833
    ]
}

# DataFrame
df = pd.DataFrame(data)

# chart size
plt.figure(figsize=(8, 5))

# horizontal bar chart
plt.barh(df["department"], df["avg_salary"])

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
