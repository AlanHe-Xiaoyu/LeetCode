-- Write your MySQL query statement below
"""
Soln 1
Runtime: 332 ms, faster than 51.52% of MySQL online submissions for Second Highest Salary.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.
"""
SELECT
    (SELECT Salary
    FROM Employee as e
    ORDER BY Salary DESC
    LIMIT 1 OFFSET 1)
AS SecondHighestSalary;


"""
Runtime: 318 ms, faster than 62.63% of MySQL online submissions for Second Highest Salary.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.
"""
SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee AS e
WHERE e.Salary < (SELECT MAX(Salary) FROM Employee);