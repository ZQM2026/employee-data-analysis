import pandas as pd
import matplotlib.pyplot as plt

# data
data = {
    "age": [28, 35, 42, 25, 31, 29, 45, 38],
    "salary": [320000, 520000, 680000, 290000,
               470000, 350000, 720000, 610000]
}

# DataFrame
df = pd.DataFrame(data)

# scatter
plt.scatter(df["age"], df["salary"])

# title
plt.title("Age vs Salary")

# X
plt.xlabel("Age")

# Y
plt.ylabel("Salary")

# show
plt.show()
