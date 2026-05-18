import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# connect database
conn = sqlite3.connect("employee.db")

# SQL query
query = """
SELECT
    d.department_name,
    AVG(e.salary) AS avg_salary
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
GROUP BY d.department_name
ORDER BY avg_salary DESC;
"""

# read SQL query result into DataFrame
df = pd.read_sql_query(query, conn)

# print result
print(df)

# chart size
plt.figure(figsize=(8, 5))

# horizontal bar chart
plt.barh(df["department_name"], df["avg_salary"])

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

# close connection
conn.close()
