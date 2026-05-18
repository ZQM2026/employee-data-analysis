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
        19.8,
        32.3,
        12.0,
        12.5,
        35.3
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
