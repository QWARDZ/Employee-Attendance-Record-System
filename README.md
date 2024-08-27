# Employee Database Setup

This document provides the SQL commands required to set up and populate the `employee_db` database for managing employee information.

## SQL Commands

Run the following commands in your MySQL XAMPP ADMIN:

```sql
-- Create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS employee_db;

-- Select the database to use
USE employee_db;

-- Drop the table if it already exists
DROP TABLE IF EXISTS employees;

-- Create the employees table
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_no VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100),
    position VARCHAR(100)
);

-- Insert sample data into the employees table
INSERT INTO employees (employee_no, name, department, position) VALUES
('2024-1234', 'John Edward Bearneza', 'IT', 'Programmer'),
('2024-9324', 'Hans Axiel Gallego', 'IT', 'Programmer'),
('2024-5678', 'Annie May Abcede', 'IT', 'Programmer'),
('2024-6438', 'Irene Faith Parcon', 'IT', 'Programmer'),
