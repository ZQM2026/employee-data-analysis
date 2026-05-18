import pandas as pd
import matplotlib.pyplot as plt

# data
data = {
    "age": [28, 35, 42, 25, 31, 29, 45, 38, 27, 33,
        41, 26, 37, 30, 48, 29, 34, 39, 24, 36,
        43, 27, 32, 29, 40, 26, 44, 31, 35, 28],
    "salary": [320000, 520000, 680000, 290000, 470000,
        350000, 720000, 610000, 310000, 490000,
        670000, 330000, 590000, 360000, 820000,
        340000, 510000, 630000, 280000, 460000,
        710000, 390000, 540000, 350000, 650000,
        320000, 730000, 380000, 560000, 410000]
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
