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
    "avg_overtime": [
        30.3,
        32.6,
        12.5,
        16.3,
        21.2
    ]
}

# DataFrame
df = pd.DataFrame(data)

# chart size
plt.figure(figsize=(8, 5))

# horizontal bar chart
plt.barh(df["department"], df["avg_overtime"])

# title
plt.title("Average Overtime Hours by Department")

# labels
plt.xlabel("Average Overtime Hours")
plt.ylabel("Department")

# grid
plt.grid(axis='x')

# layout
plt.tight_layout()

# show
plt.show()
