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
    "employees": [
        6,
        7,
        5,
        6,
        6
    ]
}

# DataFrame
df = pd.DataFrame(data)

# chart size
plt.figure(figsize=(7, 7))

# pie chart
plt.pie(
    df["employees"],
    labels=df["department"],
    autopct='%1.1f%%'
)

# title
plt.title("Employee Distribution by Department")

# show
plt.show()
