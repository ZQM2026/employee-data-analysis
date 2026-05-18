import pandas as pd
import matplotlib.pyplot as plt

# data
data = {
    "age": [24, 36, 45, 26, 31, 29, 47, 39, 27, 34,
        42, 25, 37, 30, 49, 28, 35, 40, 23, 36,
        44, 27, 33, 29, 41, 26, 46, 32, 35, 28],
    "salary": [310000, 670000, 820000, 280000, 520000,
        360000, 760000, 640000, 295000, 580000,
        690000, 340000, 610000, 350000, 910000,
        330000, 550000, 670000, 260000, 470000,
        720000, 410000, 560000, 340000, 710000,
        325000, 780000, 370000, 590000, 980000]
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
