
INSERT INTO departments VALUES
(1, 'Sales'),
(2, 'Engineering'),
(3, 'HR'),
(4, 'Finance'),
(5, 'Marketing');
INSERT INTO employees VALUES
(1, 'Tanaka', 28, 'Male', 1, 320000, 15, '2021-04-01'),
(2, 'Sato', 35, 'Female', 2, 520000, 30, '2018-06-15'),
(3, 'Suzuki', 42, 'Male', 4, 680000, 10, '2015-09-10'),
(4, 'Yamada', 25, 'Female', 5, 290000, 20, '2022-01-12'),
(5, 'Kobayashi', 31, 'Male', 2, 470000, 25, '2019-03-18'),
(6, 'Ito', 29, 'Female', 3, 350000, 12, '2020-07-21'),
(7, 'Watanabe', 45, 'Male', 1, 720000, 40, '2012-05-11'),
(8, 'Nakamura', 38, 'Female', 4, 610000, 18, '2016-08-30'),
(9, 'Yoshida', 27, 'Male', 5, 310000, 22, '2021-11-03'),
(10, 'Yamamoto', 33, 'Female', 2, 490000, 35, '2017-12-05'),
(11, 'Matsumoto', 41, 'Male', 1, 670000, 28, '2014-04-22'),
(12, 'Inoue', 26, 'Female', 3, 330000, 14, '2022-02-15'),
(13, 'Kimura', 37, 'Male', 4, 590000, 16, '2017-07-07'),
(14, 'Hayashi', 30, 'Female', 5, 360000, 24, '2020-09-01'),
(15, 'Shimizu', 48, 'Male', 2, 820000, 45, '2010-10-18'),
(16, 'Saito', 29, 'Female', 1, 340000, 19, '2021-03-25'),
(17, 'Yamazaki', 34, 'Male', 2, 510000, 31, '2018-11-11'),
(18, 'Mori', 39, 'Female', 4, 630000, 20, '2016-06-09'),
(19, 'Abe', 24, 'Male', 5, 280000, 17, '2023-04-01'),
(20, 'Ikeda', 36, 'Female', 3, 460000, 13, '2018-08-08'),
(21, 'Hashimoto', 43, 'Male', 1, 710000, 38, '2013-01-17'),
(22, 'Ishikawa', 27, 'Female', 2, 390000, 26, '2021-10-13'),
(23, 'Nakajima', 32, 'Male', 4, 540000, 15, '2019-05-19'),
(24, 'Maeda', 29, 'Female', 5, 350000, 21, '2020-12-01'),
(25, 'Fujita', 40, 'Male', 2, 650000, 34, '2015-07-27'),
(26, 'Ogawa', 26, 'Female', 3, 320000, 11, '2022-06-14'),
(27, 'Goto', 44, 'Male', 1, 730000, 42, '2011-09-05'),
(28, 'Okada', 31, 'Female', 5, 380000, 23, '2019-02-28'),
(29, 'Hasegawa', 35, 'Male', 4, 560000, 19, '2017-03-16'),
(30, 'Murakami', 28, 'Female', 2, 410000, 27, '2021-08-20');

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
