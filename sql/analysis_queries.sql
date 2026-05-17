SELECT * FROM employees;
SELECT
    d.department_name,
    ROUND(AVG(e.salary), 2) AS avg_salary
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
GROUP BY d.department_name
ORDER BY avg_salary DESC;
SELECT
    name,
    overtime_hours
FROM employees
ORDER BY overtime_hours DESC
LIMIT 5;

SELECT
    name,
    department_id,
    salary,
    RANK() OVER(
        PARTITION BY department_id
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees;

SELECT
    age,
    salary
FROM employees
ORDER BY age;
