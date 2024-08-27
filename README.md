CREATE DATABASE IF NOT EXISTS employee_db;
USE employee_db;
DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_no VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100),
    position VARCHAR(100)
);

INSERT INTO employees (employee_no, name, department, position) VALUES
('2024-1234', 'John Edward Bearneza', 'IT', 'Programmer'),
('2024-9324', 'Hans Axiel Gallego', 'IT', 'Programmer'),
('2024-5678', 'Annie May Abcede', 'IT', 'Project Manager'),
('2024-6438', 'Irene Faith Parcon', 'IT', 'UI/UX');
